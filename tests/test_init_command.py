"""Tests for the init command logic."""

import json
import os

import pytest

from claude_self_improve.init_command import run_init

EXPECTED_FILES = [
    ".claude/CLAUDE.md",
    ".claude/settings.json",
    ".claude/hooks/session-init.sh",
    ".claude/hooks/pre-edit-governance.sh",
    ".claude/hooks/post-edit-tracker.sh",
    ".claude/hooks/stop-reflection-gate.sh",
    ".claude/commands/README.md",
    ".claude/commands/meta-anti-patterns.md",
    ".claude/commands/meta-commit.md",
    ".claude/commands/meta-evolve.md",
    ".claude/commands/meta-learn.md",
    ".claude/commands/meta-propose-skill.md",
    ".claude/commands/meta-scope-guard.md",
    ".claude/commands/meta-self-audit.md",
    ".claude/memory/MEMORY.md",
    ".claude/memory/ANTI_PATTERN.md",
    ".claude/memory/skill-candidates.md",
    ".claude/memory/topic-index.md",
    ".claude/memory/sessions/.gitkeep",
]


def test_init_creates_claude_directory(tmp_path):
    assert run_init(target=str(tmp_path)) == 0
    assert (tmp_path / ".claude").is_dir()


def test_init_creates_all_expected_files(tmp_path):
    run_init(target=str(tmp_path))
    for f in EXPECTED_FILES:
        assert (tmp_path / f).exists(), f"Missing: {f}"


def test_init_hooks_are_executable(tmp_path):
    run_init(target=str(tmp_path))
    hooks_dir = tmp_path / ".claude" / "hooks"
    for hook in hooks_dir.iterdir():
        if hook.suffix == ".sh":
            assert os.access(hook, os.X_OK), f"Not executable: {hook}"


def test_init_aborts_if_claude_exists(tmp_path, capsys):
    (tmp_path / ".claude").mkdir()
    result = run_init(target=str(tmp_path))
    assert result == 1
    captured = capsys.readouterr()
    assert "already exists" in captured.out


def test_init_force_overwrites(tmp_path):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "old_file.txt").write_text("old")
    result = run_init(target=str(tmp_path), force=True)
    assert result == 0
    assert not (tmp_path / ".claude" / "old_file.txt").exists()
    assert (tmp_path / ".claude" / "CLAUDE.md").exists()


def test_init_warns_if_not_git_repo(tmp_path, capsys):
    run_init(target=str(tmp_path))
    captured = capsys.readouterr()
    assert "not a git repository" in captured.out


def test_init_no_warning_in_git_repo(tmp_path, capsys):
    (tmp_path / ".git").mkdir()
    run_init(target=str(tmp_path))
    captured = capsys.readouterr()
    assert "not a git repository" not in captured.out


def test_settings_json_is_valid(tmp_path):
    run_init(target=str(tmp_path))
    settings = json.loads(
        (tmp_path / ".claude" / "settings.json").read_text()
    )
    assert "hooks" in settings
    for event in ("SessionStart", "PreToolUse", "PostToolUse", "Stop"):
        assert event in settings["hooks"]


def test_no_domain_specific_content(tmp_path):
    """Template files must not contain scalable-dft references."""
    run_init(target=str(tmp_path))
    claude_dir = tmp_path / ".claude"
    for path in claude_dir.rglob("*"):
        if path.is_file() and path.suffix in (".md", ".json", ".sh"):
            content = path.read_text().lower()
            assert "scalable_dft" not in content, (
                f"Found 'scalable_dft' in {path.name}"
            )
            assert "scalable-dft" not in content, (
                f"Found 'scalable-dft' in {path.name}"
            )
            assert "omol" not in content, (
                f"Found 'omol' in {path.name}"
            )
            assert "orca" not in content, (
                f"Found 'orca' in {path.name}"
            )
