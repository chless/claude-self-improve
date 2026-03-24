"""Core logic for the ``register``, ``unregister``, and ``children`` subcommands."""

from __future__ import annotations

import json
import shutil
import subprocess
from datetime import date
from pathlib import Path


def _is_remote_url(source: str) -> bool:
    """Return True if *source* looks like a git URL (not a plain local path)."""
    return "://" in source or source.startswith("git@")


def _default_alias(source: str) -> str:
    """Derive a short alias from a path or URL."""
    name = source.rstrip("/").rsplit("/", 1)[-1]
    # Strip .git suffix from remote URLs
    if name.endswith(".git"):
        name = name[:-4]
    return name


def _load_children(config_path: Path) -> dict:
    if config_path.exists():
        return json.loads(config_path.read_text())
    return {"children": [], "integration_log": []}


def _save_children(config_path: Path, data: dict) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(data, indent=2) + "\n")


def run_register(
    target: str = ".",
    child_source: str = "",
    alias: str | None = None,
) -> int:
    """Register a child repo (local path or remote git URL)."""
    target_path = Path(target).resolve()
    config_path = target_path / ".claude" / "memory" / "children.json"

    if not (target_path / ".claude").exists():
        print("Error: .claude/ not found. Run `claude-self-improve init` first.")
        return 1

    if not child_source:
        print("Error: child_source is required.")
        return 1

    resolved_alias = alias or _default_alias(child_source)
    data = _load_children(config_path)

    # Check duplicate alias
    for child in data["children"]:
        if child["alias"] == resolved_alias:
            print(f"Error: alias '{resolved_alias}' is already registered.")
            return 1

    if _is_remote_url(child_source):
        # Clone remote repo
        clone_dir = target_path / ".claude" / "children" / resolved_alias
        if clone_dir.exists():
            print(
                f"Error: clone directory already exists: {clone_dir}\n"
                "Remove it manually or use a different alias."
            )
            return 1
        clone_dir.parent.mkdir(parents=True, exist_ok=True)
        print(f"Cloning {child_source} into {clone_dir} ...")
        result = subprocess.run(
            ["git", "clone", "--depth=50", child_source, str(clone_dir)],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(f"Error: git clone failed:\n{result.stderr}")
            return 1

        child_path = clone_dir
        source_type = "remote"
    else:
        child_path = Path(child_source).resolve()
        source_type = "local"

    # Validate child repo
    if not child_path.is_dir():
        print(f"Error: {child_path} is not a directory.")
        return 1
    if not (child_path / ".git").exists():
        print(f"Error: {child_path} is not a git repository (no .git/).")
        return 1
    if not (child_path / ".claude").exists():
        print(
            f"Error: {child_path} has no .claude/ directory.\n"
            "The child must use claude-self-improve governance."
        )
        # Clean up clone if we created one
        if source_type == "remote":
            shutil.rmtree(child_path, ignore_errors=True)
        return 1

    # Check duplicate path
    resolved_str = str(child_path)
    for child in data["children"]:
        if child["path"] == resolved_str:
            print(f"Error: path '{resolved_str}' is already registered.")
            # Clean up clone if we created one
            if source_type == "remote":
                shutil.rmtree(child_path, ignore_errors=True)
            return 1

    entry = {
        "alias": resolved_alias,
        "source": source_type,
        "path": resolved_str,
        "url": child_source if source_type == "remote" else None,
        "registered": str(date.today()),
        "last_integrated": None,
        "last_integrated_commit": None,
    }
    data["children"].append(entry)
    _save_children(config_path, data)

    print(f"Registered child '{resolved_alias}' ({source_type}): {child_path}")
    return 0


def run_unregister(target: str = ".", alias: str = "") -> int:
    """Remove a registered child repo by alias."""
    target_path = Path(target).resolve()
    config_path = target_path / ".claude" / "memory" / "children.json"

    if not config_path.exists():
        print("Error: no children.json found. Nothing to unregister.")
        return 1

    data = _load_children(config_path)

    found = None
    for i, child in enumerate(data["children"]):
        if child["alias"] == alias:
            found = i
            break

    if found is None:
        print(f"Error: no child registered with alias '{alias}'.")
        return 1

    removed = data["children"].pop(found)

    # Clean up clone directory for remote children
    if removed.get("source") == "remote":
        clone_dir = Path(removed["path"])
        if clone_dir.exists():
            shutil.rmtree(clone_dir)
            print(f"Removed clone directory: {clone_dir}")

    _save_children(config_path, data)
    print(f"Unregistered child '{alias}'.")
    return 0


def run_list_children(target: str = ".") -> int:
    """List all registered child repos."""
    target_path = Path(target).resolve()
    config_path = target_path / ".claude" / "memory" / "children.json"

    if not config_path.exists():
        print("No children registered. Use `claude-self-improve register` to add one.")
        return 0

    data = _load_children(config_path)

    if not data["children"]:
        print("No children registered. Use `claude-self-improve register` to add one.")
        return 0

    print(f"{'Alias':<20} {'Source':<8} {'Last Integrated':<18} {'Path/URL'}")
    print("-" * 80)
    for child in data["children"]:
        alias = child["alias"]
        source = child.get("source", "local")
        last = child.get("last_integrated") or "never"
        location = child.get("url") or child["path"]
        print(f"{alias:<20} {source:<8} {last:<18} {location}")

    return 0
