# Stage 1, requirements

| | |
| --- | --- |
| Agent | Analyst (one process for stages 1 and 2, ADR-001) |
| Job | `analyst` job |
| Code | `stages.analyst()` writes `spec.md` first |
| Prompt | [`analyst.md`](../../prompts/analyst.md) Task 1, built from the A1 skill [`a1-specgate.md`](../../prompts/a1-specgate.md) |
| Tools | `list_dir`, `read_file` (read-only; `experiment/` refused) |
| Input | Issue title and body, wrapped as untrusted data; `ARCHITECTURE.md`; the tree |
| Output artifact | `spec.md` |
| Check | `checks.check_spec()`: every acceptance criterion names an action and an observable result. Script, not the model. |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
