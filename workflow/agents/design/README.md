# Stage 2, design

| | |
| --- | --- |
| Agent | Analyst, same process as stage 1, after `spec.md` passes |
| Job | `analyst` job |
| Code | `stages.analyst()` writes `design.md` second |
| Prompt | [`analyst.md`](../../prompts/analyst.md) Task 2 |
| Tools | `list_dir`, `read_file` |
| Input | `spec.md`, `ARCHITECTURE.md` (A2), the tree |
| Output artifact | `design.md` |
| Check | `checks.check_design()`: names at least one existing file and a function defined in it. |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
