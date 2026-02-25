"""Core logic for the ``init`` subcommand."""

import importlib.resources
import os
import shutil
import stat
from pathlib import Path


def run_init(target: str = ".", force: bool = False) -> int:
    """Copy the governance template into *target*/.claude/."""
    target_path = Path(target).resolve()
    claude_dir = target_path / ".claude"

    # 1. Guard against overwriting
    if claude_dir.exists() and not force:
        print(
            f"Error: {claude_dir} already exists.\n"
            "Use --force to overwrite, or remove it manually first."
        )
        return 1

    # 2. Warn (don't block) if not a git repo
    if not (target_path / ".git").exists():
        print(
            f"Warning: {target_path} is not a git repository.\n"
            "The governance framework works best inside a git repo.\n"
        )

    # 3. Locate bundled template
    source_dir = (
        importlib.resources.files("claude_self_improve.templates") / "claude"
    )

    # 4. Copy templates → .claude/
    if claude_dir.exists():
        shutil.rmtree(claude_dir)

    with importlib.resources.as_file(source_dir) as src_path:
        shutil.copytree(src_path, claude_dir)

    # 5. Make hook scripts executable
    hooks_dir = claude_dir / "hooks"
    if hooks_dir.exists():
        for hook in hooks_dir.iterdir():
            if hook.suffix == ".sh":
                hook.chmod(
                    hook.stat().st_mode
                    | stat.S_IXUSR
                    | stat.S_IXGRP
                    | stat.S_IXOTH
                )

    # 6. Success output
    print(f"Initialized .claude/ governance framework in {target_path}\n")
    print("Created:")
    _print_tree(claude_dir, prefix="  ")
    print()
    print("Next steps:")
    print("  1. Review and customize .claude/CLAUDE.md for your project")
    print("  2. Commit .claude/ to your repository:")
    print(
        "     git add .claude/ && git commit -m "
        "'feat: add AI agent governance framework'"
    )
    print("  3. Set up memory symlink (one-time per machine):")
    print("     claude-self-improve link")
    print(
        "  4. Start a Claude Code session — governance hooks "
        "activate automatically"
    )
    return 0


def _print_tree(directory: Path, prefix: str = "") -> None:
    """Print a simple directory tree."""
    entries = sorted(
        directory.iterdir(), key=lambda p: (p.is_file(), p.name)
    )
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            extension = "    " if is_last else "│   "
            _print_tree(entry, prefix=prefix + extension)
