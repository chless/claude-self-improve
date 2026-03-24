"""Tests for the register/unregister/children command logic."""

import json

from claude_self_improve.init_command import run_init
from claude_self_improve.register_command import (
    _is_remote_url,
    run_list_children,
    run_register,
    run_unregister,
)


def _setup_parent(tmp_path):
    """Initialize a parent repo with .claude/."""
    run_init(target=str(tmp_path))
    return tmp_path


def _setup_child(tmp_path, name="child-repo"):
    """Create a minimal child repo with .git/ and .claude/."""
    child = tmp_path / name
    child.mkdir()
    (child / ".git").mkdir()
    (child / ".claude").mkdir()
    return child


def test_register_creates_children_json(tmp_path):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "child")
    result = run_register(target=str(parent), child_source=str(child))
    assert result == 0
    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    assert len(data["children"]) == 1
    assert data["children"][0]["alias"] == "child"


def test_register_validates_child_has_claude_dir(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    child = tmp_path / "no-claude"
    child.mkdir()
    (child / ".git").mkdir()
    result = run_register(target=str(parent), child_source=str(child))
    assert result == 1
    captured = capsys.readouterr()
    assert "no .claude/ directory" in captured.out


def test_register_validates_child_has_git(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    child = tmp_path / "no-git"
    child.mkdir()
    (child / ".claude").mkdir()
    result = run_register(target=str(parent), child_source=str(child))
    assert result == 1
    captured = capsys.readouterr()
    assert "not a git repository" in captured.out


def test_register_default_alias(tmp_path):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "health-coach")
    run_register(target=str(parent), child_source=str(child))
    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    assert data["children"][0]["alias"] == "health-coach"


def test_register_custom_alias(tmp_path):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "my-repo")
    run_register(target=str(parent), child_source=str(child), alias="custom-name")
    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    assert data["children"][0]["alias"] == "custom-name"


def test_register_duplicate_alias_fails(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    child1 = _setup_child(tmp_path, "child1")
    child2 = _setup_child(tmp_path, "child2")
    run_register(target=str(parent), child_source=str(child1), alias="same")
    result = run_register(target=str(parent), child_source=str(child2), alias="same")
    assert result == 1
    captured = capsys.readouterr()
    assert "already registered" in captured.out


def test_register_duplicate_path_fails(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "child")
    run_register(target=str(parent), child_source=str(child), alias="first")
    result = run_register(target=str(parent), child_source=str(child), alias="second")
    assert result == 1
    captured = capsys.readouterr()
    assert "already registered" in captured.out


def test_register_stores_source_local(tmp_path):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "child")
    run_register(target=str(parent), child_source=str(child))
    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    assert data["children"][0]["source"] == "local"
    assert data["children"][0]["url"] is None


def test_register_remote_url_clones(tmp_path):
    """Remote URL triggers git clone into .claude/children/."""
    import subprocess

    parent = _setup_parent(tmp_path / "parent")
    # Create a bare repo to act as remote
    remote = tmp_path / "remote.git"
    remote.mkdir()

    env = {
        "HOME": str(tmp_path),
        "PATH": "/usr/local/bin:/usr/bin:/bin",
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Test",
        "GIT_AUTHOR_EMAIL": "test@test.com",
        "GIT_COMMITTER_NAME": "Test",
        "GIT_COMMITTER_EMAIL": "test@test.com",
    }

    subprocess.run(
        ["git", "init", "--bare", str(remote)],
        capture_output=True,
        check=True,
        env=env,
    )
    # Seed the remote with a commit that includes .claude/
    work = tmp_path / "work"
    work.mkdir()
    subprocess.run(
        ["git", "init", str(work)],
        capture_output=True,
        check=True,
        env=env,
    )
    (work / ".claude").mkdir()
    (work / ".claude" / "CLAUDE.md").write_text("# test")
    subprocess.run(
        ["git", "-C", str(work), "add", "."],
        capture_output=True,
        check=True,
        env=env,
    )
    subprocess.run(
        ["git", "-C", str(work), "commit", "-m", "init"],
        capture_output=True,
        check=True,
        env=env,
    )
    subprocess.run(
        ["git", "-C", str(work), "remote", "add", "origin", str(remote)],
        capture_output=True,
        check=True,
        env=env,
    )
    subprocess.run(
        ["git", "-C", str(work), "push", "origin", "HEAD"],
        capture_output=True,
        check=True,
        env=env,
    )

    remote_url = f"file://{remote}"
    result = run_register(
        target=str(parent),
        child_source=remote_url,
        alias="remote-child",
    )
    assert result == 0

    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    entry = data["children"][0]
    assert entry["source"] == "remote"
    assert entry["alias"] == "remote-child"
    assert entry["url"] == remote_url
    # Clone directory should exist
    clone_dir = parent / ".claude" / "children" / "remote-child"
    assert clone_dir.exists()
    assert (clone_dir / ".claude" / "CLAUDE.md").exists()


def test_unregister_removes_entry(tmp_path):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "child")
    run_register(target=str(parent), child_source=str(child))
    result = run_unregister(target=str(parent), alias="child")
    assert result == 0
    config = parent / ".claude" / "memory" / "children.json"
    data = json.loads(config.read_text())
    assert len(data["children"]) == 0


def test_unregister_nonexistent_fails(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    result = run_unregister(target=str(parent), alias="ghost")
    assert result == 1
    captured = capsys.readouterr()
    assert "ghost" in captured.out


def test_unregister_remote_cleans_clone(tmp_path):
    """Unregistering a remote child removes the cloned directory."""
    parent = _setup_parent(tmp_path / "parent")
    # Simulate a remote registration by writing children.json directly
    clone_dir = parent / ".claude" / "children" / "my-remote"
    clone_dir.mkdir(parents=True)
    (clone_dir / "marker.txt").write_text("cloned")

    config_path = parent / ".claude" / "memory" / "children.json"
    data = {
        "children": [
            {
                "alias": "my-remote",
                "source": "remote",
                "path": str(clone_dir),
                "url": "https://example.com/repo.git",
                "registered": "2026-01-01",
                "last_integrated": None,
                "last_integrated_commit": None,
            }
        ],
        "integration_log": [],
    }
    config_path.write_text(json.dumps(data))

    result = run_unregister(target=str(parent), alias="my-remote")
    assert result == 0
    assert not clone_dir.exists()


def test_list_children_empty(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    result = run_list_children(target=str(parent))
    assert result == 0
    captured = capsys.readouterr()
    assert "No children registered" in captured.out


def test_list_children_shows_entries(tmp_path, capsys):
    parent = _setup_parent(tmp_path / "parent")
    child = _setup_child(tmp_path, "health-coach")
    run_register(target=str(parent), child_source=str(child))
    result = run_list_children(target=str(parent))
    assert result == 0
    captured = capsys.readouterr()
    assert "health-coach" in captured.out
    assert "local" in captured.out


def test_register_without_init_fails(tmp_path, capsys):
    """Register fails if parent has no .claude/ directory."""
    child = _setup_child(tmp_path, "child")
    result = run_register(target=str(tmp_path), child_source=str(child))
    assert result == 1
    captured = capsys.readouterr()
    assert ".claude/ not found" in captured.out


# --- _is_remote_url edge cases ---


def test_is_remote_url_https():
    assert _is_remote_url("https://github.com/user/repo.git") is True


def test_is_remote_url_ssh():
    assert _is_remote_url("ssh://git@host/repo") is True


def test_is_remote_url_git_at():
    assert _is_remote_url("git@github.com:user/repo.git") is True


def test_is_remote_url_local_path():
    assert _is_remote_url("/home/user/project") is False


def test_is_remote_url_local_bare_repo():
    """Local bare repo ending in .git should NOT be treated as remote."""
    assert _is_remote_url("/home/user/project.git") is False


def test_is_remote_url_file_scheme():
    """file:// URLs are valid git URLs and trigger clone behavior."""
    assert _is_remote_url("file:///tmp/repo") is True
