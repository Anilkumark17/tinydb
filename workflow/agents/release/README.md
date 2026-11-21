# Stage 5, release

| | |
| --- | --- |
| Agent | Release script, no model (ADR-001) |
| Job | `release` job (and `release_again`) |
| Code | `release.release()` |
| Prompt | none |
| Tools | `git push` and `gh pr create` with `AUTOSE_PAT` (ADR-011); `contents: write` and `pull-requests: write` only in this job |
| Input | Branch, `spec.md` title, passing `test_report.md` |
| Output artifact | `pr.md` and the PR URL |
| Check | PR is open against `master`, and no pull-request CI check is newly red compared with `master` (ADR-016, ADR-019). |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
