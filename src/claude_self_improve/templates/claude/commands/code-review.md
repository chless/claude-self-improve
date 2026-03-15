# Code Review

**Triggers:** When the user asks to review code quality, check conventions, or audit a module. Invoke as `/code-review <scope>`.

## Scope Argument

`$ARGUMENTS` specifies what to review. Interpret it as one of:

| Argument | Scope | Example |
|----------|-------|---------|
| A file path | Single file | `/code-review src/mypackage/processor.py` |
| A directory path | Subpackage | `/code-review src/mypackage/utils` |
| `repo` or empty | Entire repository | `/code-review repo` or `/code-review` |

## Procedure

### 1. Scope Discovery

- **Single file:** Read the file end-to-end. Read its test file. Read files it imports from.
- **Subpackage:** Read directory README. List all source files. Read `__init__.py`. Identify the test directory counterpart.
- **Entire repo:** Use CLAUDE.md Package Structure as the map. Sample key files from each subpackage rather than reading everything.

### 2. Review Checklist

Evaluate each dimension and report findings with file:line references.

**Correctness**
- Logic errors, off-by-one, unhandled edge cases
- Resource leaks (open files, subprocesses, temp directories)
- Race conditions in concurrent code (multiprocessing, threading)

**Architecture**
- Project architectural boundaries respected
- Configs not hardcoded in modules
- Import conventions followed
- No circular dependencies

**Style & Conventions**
- Type hints on all function signatures
- Docstrings for public functions/classes
- Line length within project limits
- Language style guide compliance

**Testing**
- Test file exists mirroring source structure
- Key paths covered (happy path, error cases, edge cases)
- Tests are self-contained (no reliance on external services without mocking)

**Documentation**
- Module-level docstring present
- Directory README exists and is current (for subpackage scope)
- Scripts documented if applicable

**Security & Robustness**
- No hardcoded paths, credentials, or secrets
- User input validated at system boundaries
- Subprocess calls use lists, not shell strings
- Temp files cleaned up

### 3. Report

Present findings organized by severity:

1. **Blockers** — bugs, security issues, data corruption risks
2. **Should fix** — convention violations, missing tests, architectural drift
3. **Consider** — style improvements, optional refactors, documentation gaps

For each finding:
- File path and line number
- What the issue is
- Suggested fix (concrete, not vague)

### 4. Summary

End with a one-paragraph overall assessment: is this code ready for production use, or what needs to happen first?

---
*Created: 2026-02-19 | Source: user request*
