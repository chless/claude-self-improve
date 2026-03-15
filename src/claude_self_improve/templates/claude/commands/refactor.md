# Refactor

**Triggers:** When the user asks to refactor, restructure, or clean up code. Invoke as `/refactor <scope>`.

## Scope Argument

`$ARGUMENTS` specifies what to refactor. Interpret it as one of:

| Argument | Scope | Example |
|----------|-------|---------|
| A file path | Single file | `/refactor src/mypackage/processor.py` |
| A directory path | Subpackage | `/refactor src/mypackage/utils` |
| `repo` or empty | Entire repository | `/refactor repo` or `/refactor` |

## Procedure

### 1. Scope Discovery

- **Single file:** Read the file. Read its tests (`tests/` mirror path). Read its imports to understand dependencies.
- **Subpackage:** Read the directory README if it exists. List all source files. Read `__init__.py` for public API. Identify the test directory counterpart.
- **Entire repo:** Start with the Package Structure in CLAUDE.md. Identify modules by size/complexity. Prioritize high-churn or high-complexity areas.

### 2. Diagnosis

Identify refactoring opportunities. Check for:

- **Duplication** — repeated logic that should be extracted into a shared function
- **Long functions** — functions exceeding ~50 lines that should be decomposed
- **Naming** — unclear variable/function names that don't communicate intent
- **Responsibility violations** — code violating the project's architectural boundaries
- **Import hygiene** — circular dependencies, unused imports, wrong import ordering
- **Dead code** — unreachable branches, commented-out code, unused parameters
- **Missing types** — functions without type hints

### 3. Plan

Present the refactoring plan to the user before making changes:
- List each change with file path and what will change
- Group changes by type (extract function, rename, move, delete)
- Flag any changes that might break external consumers
- Estimate how many files will be touched

### 4. Execute

After user approval:
- Make one logical change at a time — don't batch unrelated refactors into a single edit
- Preserve existing tests — if a test breaks, the refactor is wrong, not the test
- Update imports across the codebase when moving/renaming
- Update `__init__.py` exports if public API changed
- Update CLAUDE.md Package Structure if directory layout changed

### 5. Verify

- Run tests (or the subset matching the scope)
- Check that no imports are broken
- If scope was a subpackage or repo, run linting on affected files

---
*Created: 2026-02-19 | Source: user request*
