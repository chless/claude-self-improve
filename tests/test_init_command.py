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
    ".claude/hooks/motivation-tracker.sh",
    ".claude/hooks/stop-reflection-gate.sh",
    ".claude/commands/README.md",
    ".claude/commands/meta-anti-patterns.md",
    ".claude/commands/meta-commit.md",
    ".claude/commands/meta-evolve.md",
    ".claude/commands/meta-learn.md",
    ".claude/commands/meta-motivation.md",
    ".claude/commands/meta-propose-skill.md",
    ".claude/commands/meta-scope-guard.md",
    ".claude/commands/meta-self-audit.md",
    ".claude/commands/meta-absorb-repo.md",
    ".claude/commands/meta-intelligence-review.md",
    ".claude/commands/meta-intelligence-inject.md",
    ".claude/commands/refactor.md",
    ".claude/commands/code-review.md",
    ".claude/commands/new-subpackage.md",
    ".claude/memory/MEMORY.md",
    ".claude/memory/ANTI_PATTERN.md",
    ".claude/memory/cognitive-architecture.md",
    ".claude/memory/episodic-memory.md",
    ".claude/memory/procedural-memory.md",
    ".claude/memory/skill-candidates.md",
    ".claude/memory/topic-index.md",
    ".claude/memory/absorbed-intelligence.md",
    ".claude/memory/review-registry.md",
    ".claude/memory/reviews/.gitkeep",
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


def test_three_pillar_architecture(tmp_path):
    """Three pillars must organize the entire governance system."""
    run_init(target=str(tmp_path))
    claude_md = (tmp_path / ".claude" / "CLAUDE.md").read_text()
    memory_md = (tmp_path / ".claude" / "memory" / "MEMORY.md").read_text()
    arch_md = (tmp_path / ".claude" / "memory" / "cognitive-architecture.md").read_text()
    # CLAUDE.md organized by pillars
    assert "Pillar 1: Motivation" in claude_md
    assert "Pillar 2: Learning" in claude_md
    assert "Pillar 3: Memory" in claude_md
    # Each pillar has meta-skills and hooks sections
    assert "Meta-Skills (Motivation)" in claude_md
    assert "Meta-Skills (Learning)" in claude_md
    assert "Meta-Skills (Memory)" in claude_md
    # Session lifecycle shows all three pillars
    assert "SESSION START" in claude_md
    # MEMORY.md has pillar-organized registry
    assert "Cognitive Architecture" in memory_md
    assert "meta-motivation" in memory_md
    assert "meta-learn" in memory_md
    assert "Pillar" in memory_md  # Pillar column in registry
    # Memory hierarchy documented
    assert "Episodic" in memory_md
    assert "Semantic" in memory_md
    assert "Procedural" in memory_md
    # Architecture doc has unified learning
    assert "Unified Learning Loop" in arch_md
    assert "BEFORE" in arch_md
    assert "DURING" in arch_md
    assert "AFTER" in arch_md


def test_motivation_hook_in_settings(tmp_path):
    """Motivation tracker hook must be configured in settings.json."""
    run_init(target=str(tmp_path))
    settings = json.loads(
        (tmp_path / ".claude" / "settings.json").read_text()
    )
    post_hooks = settings["hooks"]["PostToolUse"]
    bash_hooks = [h for h in post_hooks if h.get("matcher") == "Bash"]
    assert len(bash_hooks) == 1
    assert "motivation-tracker.sh" in bash_hooks[0]["hooks"][0]["command"]


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


def test_cross_repo_intelligence_integration(tmp_path):
    """Cross-repo absorption must be integrated into all three pillars."""
    run_init(target=str(tmp_path))
    claude_md = (tmp_path / ".claude" / "CLAUDE.md").read_text()
    memory_md = (tmp_path / ".claude" / "memory" / "MEMORY.md").read_text()
    arch_md = (
        tmp_path / ".claude" / "memory" / "cognitive-architecture.md"
    ).read_text()
    absorbed = (
        tmp_path / ".claude" / "memory" / "absorbed-intelligence.md"
    ).read_text()
    # meta-absorb-repo registered in CLAUDE.md under Learning
    assert "meta-absorb-repo" in claude_md
    # Registered in MEMORY.md meta-skill registry under Learning pillar
    assert "meta-absorb-repo" in memory_md
    # cognitive-architecture.md has cross-repo section
    assert "Cross-Repo" in arch_md
    # absorbed-intelligence.md references cross-repo patterns
    assert "Cross-Repo Patterns" in absorbed
    assert "Absorption Log" in absorbed


def test_stateful_intelligence_network(tmp_path):
    """Peer review and injection must be integrated into the framework."""
    run_init(target=str(tmp_path))
    claude_md = (tmp_path / ".claude" / "CLAUDE.md").read_text()
    memory_md = (tmp_path / ".claude" / "memory" / "MEMORY.md").read_text()
    arch_md = (
        tmp_path / ".claude" / "memory" / "cognitive-architecture.md"
    ).read_text()
    registry = (
        tmp_path / ".claude" / "memory" / "review-registry.md"
    ).read_text()
    review_md = (
        tmp_path / ".claude" / "commands" / "meta-intelligence-review.md"
    ).read_text()
    inject_md = (
        tmp_path / ".claude" / "commands" / "meta-intelligence-inject.md"
    ).read_text()
    # Both skills registered in CLAUDE.md
    assert "meta-intelligence-review" in claude_md
    assert "meta-intelligence-inject" in claude_md
    # Both in MEMORY.md registry
    assert "meta-intelligence-review" in memory_md
    assert "meta-intelligence-inject" in memory_md
    # Architecture has stateful intelligence section
    assert "Stateful Intelligence" in arch_md
    # Registry has review/injection tracking
    assert "Reviews Received" in registry
    assert "Injections Sent" in registry
    # Review skill has provenance fields
    assert "Reviewer Identity" in review_md
    assert "Commit" in review_md
    # Inject skill has provenance fields
    assert "Source Identity" in inject_md
    assert "provenance" in inject_md.lower()
    # Reviews directory exists
    assert (tmp_path / ".claude" / "memory" / "reviews").is_dir()
