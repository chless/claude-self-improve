"""Core logic for the ``link`` subcommand."""

from pathlib import Path


def run_link(target: str = ".") -> int:
    """Create the Claude Code memory symlink for *target*."""
    target_path = Path(target).resolve()
    memory_dir = target_path / ".claude" / "memory"

    if not memory_dir.exists():
        print(
            "Error: .claude/memory/ not found. "
            "Run `claude-self-improve init` first."
        )
        return 1

    # Claude Code stores per-project memory at
    # ~/.claude/projects/<escaped-path>/memory/
    # where the escaped path replaces / with -
    escaped = str(target_path).replace("/", "-")
    claude_memory = (
        Path.home() / ".claude" / "projects" / escaped / "memory"
    )

    claude_memory.parent.mkdir(parents=True, exist_ok=True)

    if claude_memory.exists() or claude_memory.is_symlink():
        if claude_memory.is_symlink():
            claude_memory.unlink()
        else:
            print(
                f"Warning: {claude_memory} exists and is not a symlink. "
                "Skipping."
            )
            return 1

    claude_memory.symlink_to(memory_dir)
    print(f"Linked: {claude_memory} -> {memory_dir}")
    return 0
