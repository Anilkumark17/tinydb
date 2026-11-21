# Stage 3, implementation

| | |
| --- | --- |
| Agent | Implementer, a new model process |
| Job | `builder` job (and `rework` after a `code` verdict) |
| Code | `stages._implement()`, called by `stages.builder()` |
| Prompt | [`implementer.md`](../../prompts/implementer.md) |
| Tools | `list_dir`, `read_file`, `replace_in_file`, `write_file` (not `tests/`, `.github/`, `autose/`, `.git`; ADR-005, ADR-021). No shell, no push. |
| Input | `spec.md`, `design.md`, review feedback on a rework round |
| Output artifact | `diff.patch` |
| Check | `stages._builds()`: `uv sync` and `import tinydb` succeed. A failure stops the run (ADR-007). |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
