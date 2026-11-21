# Stage 4, testing

| | |
| --- | --- |
| Agent | Tester, a separate model process that does not see the implementer's messages (ADR-003) |
| Job | `builder` job |
| Code | `stages._test()`, then `uv run pytest tests` |
| Prompt | [`tester.md`](../../prompts/tester.md) |
| Tools | `list_dir`, `read_file`, `write_file` under `tests/` only |
| Input | `spec.md`, `design.md`, the diff, the pytest log on a retry |
| Output artifact | `test_report.md` |
| Check | The pytest exit code over new and existing tests. A failure goes back to the implementer: 2 retries, then 1 return to design, then stop. |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
