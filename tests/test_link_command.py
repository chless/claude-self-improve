"""Tests for the link command logic."""

from pathlib import Path

from claude_self_improve.init_command import run_init
from claude_self_improve.link_command import run_link


def _init_project(tmp_path):
    """Initialize a project with .claude/ at tmp_path."""
    run_init(target=str(tmp_path))
    return tmp_path


def test_link_creates_symlink(tmp_path, monkeypatch):
    project = _init_project(tmp_path / "project")
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", staticmethod(lambda: fake_home))

    result = run_link(target=str(project))
    assert result == 0

    escaped = str(project.resolve()).replace("/", "-")
    symlink = fake_home / ".claude" / "projects" / escaped / "memory"
    assert symlink.is_symlink()
    assert symlink.resolve() == (project / ".claude" / "memory").resolve()


def test_link_replaces_existing_symlink(tmp_path, monkeypatch):
    project = _init_project(tmp_path / "project")
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", staticmethod(lambda: fake_home))

    # Create an existing symlink pointing elsewhere
    escaped = str(project.resolve()).replace("/", "-")
    link_parent = fake_home / ".claude" / "projects" / escaped
    link_parent.mkdir(parents=True)
    old_target = tmp_path / "old"
    old_target.mkdir()
    (link_parent / "memory").symlink_to(old_target)

    result = run_link(target=str(project))
    assert result == 0

    symlink = link_parent / "memory"
    assert symlink.is_symlink()
    assert symlink.resolve() == (project / ".claude" / "memory").resolve()


def test_link_fails_if_target_not_symlink(tmp_path, monkeypatch, capsys):
    project = _init_project(tmp_path / "project")
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", staticmethod(lambda: fake_home))

    # Create a real directory (not a symlink) at the memory path
    escaped = str(project.resolve()).replace("/", "-")
    real_dir = fake_home / ".claude" / "projects" / escaped / "memory"
    real_dir.mkdir(parents=True)

    result = run_link(target=str(project))
    assert result == 1
    captured = capsys.readouterr()
    assert "not a symlink" in captured.out


def test_link_escaped_path(tmp_path, monkeypatch):
    project = _init_project(tmp_path / "project")
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(Path, "home", staticmethod(lambda: fake_home))

    run_link(target=str(project))

    # The escaped path should replace / with -
    resolved = str(project.resolve())
    escaped = resolved.replace("/", "-")
    link_dir = fake_home / ".claude" / "projects" / escaped
    assert link_dir.exists()


def test_link_without_memory_fails(tmp_path, capsys):
    result = run_link(target=str(tmp_path))
    assert result == 1
    captured = capsys.readouterr()
    assert "not found" in captured.out
