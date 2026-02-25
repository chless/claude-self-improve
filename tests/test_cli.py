"""Tests for the CLI entry point."""

import pytest

from claude_self_improve.cli import main


def test_no_command_returns_1(capsys):
    assert main([]) == 1
    captured = capsys.readouterr()
    assert "claude-self-improve" in captured.out


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "0.1.0" in captured.out


def test_init_subcommand_recognized(tmp_path):
    """init runs without crashing on a fresh directory."""
    result = main(["init", "--target", str(tmp_path)])
    assert result == 0


def test_link_without_init_fails(tmp_path, capsys):
    """link fails if .claude/memory/ doesn't exist."""
    result = main(["link", "--target", str(tmp_path)])
    assert result == 1
    captured = capsys.readouterr()
    assert "not found" in captured.out
