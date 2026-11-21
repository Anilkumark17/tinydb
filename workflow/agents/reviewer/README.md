# Stage 6, independent review

| | |
| --- | --- |
| Agent | Reviewer, its own job, prompt and model process (ADR-008) |
| Job | `review` job (and `review_again`); also `review-check.yml` for seeded PRs (ADR-022) |
| Code | `stages.review()`; a script posts it with `release.post_review()` |
| Prompt | [`reviewer.md`](../../prompts/reviewer.md) |
| Tools | `list_dir`, `read_file`, `run_tests` (fixed pytest command). No GitHub token, no push. |
| Input | Issue text, the diff, a fresh checkout of the PR head. Not `spec.md`, `design.md` or the builder transcript. |
| Output artifact | `review.md` |
| Check | `checks.check_verdict()`: first line is `verdict: approve`, `code` or `approach`, and a non-approve verdict names a file from the diff. At most 2 rounds. The workflow never merges. |

Runtime code: [`../runtime/`](../runtime/) (a copy of `autose/` at the repository root, which is what Actions runs). Workflow: [`../../.github/workflows/autose.yml`](../../.github/workflows/autose.yml). Stage map: [`architecture/views/stage-map.md`](../../../architecture/views/stage-map.md).
