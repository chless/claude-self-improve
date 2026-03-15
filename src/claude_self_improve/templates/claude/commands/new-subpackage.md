# New Subpackage Creation Checklist

**Triggers:** When creating any new directory under `src/`, adding a new module group, or restructuring packages.

## Procedure

1. **Check parent directory README** — Read any `README.md` in the parent directory before adding code. It may contain conventions or constraints.
2. **Create the directory** with `__init__.py` containing appropriate exports.
3. **Write `README.md` in the new directory** — this MUST happen in the same step as creating the code. The README must include:
   - Purpose of the subpackage
   - Module descriptions (one paragraph each)
   - CLI usage with example commands (if applicable)
   - Expected input/output formats
   - Programmatic usage snippets
   - Dependencies list
4. **Update parent `__init__.py`** if the new subpackage should be part of the public API.
5. **Update `.claude/CLAUDE.md`** Package Structure section to reflect the new directory.
6. **Create corresponding test directory** mirroring the source structure under `tests/`.
7. **Update `docs/README.md`** if the subpackage introduces user-facing functionality.

## Examples

### Creating `data/analysis/`
**Situation:** Need a new subpackage for result analysis.
**Action:** Create directory, `__init__.py`, `analysis.py`, AND `README.md` all in the same step.
**Result:** Complete subpackage with documentation from the start.

---
*Created: 2026-02-19 | Source: project convention from CLAUDE.md "When Adding New Modules" section*
