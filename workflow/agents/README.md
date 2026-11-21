# Agents

One folder per stage, as the assignment layout asks. Each folder says which agent handles the stage, its tools, inputs, artifact and check.

| Stage | Folder | Agent |
| --- | --- | --- |
| 1 Requirements | [requirements/](requirements/) | analyst |
| 2 Design | [design/](design/) | analyst |
| 3 Implementation | [implementation/](implementation/) | implementer |
| 4 Testing | [testing/](testing/) | tester |
| 5 Release | [release/](release/) | script, no model |
| 6 Review | [reviewer/](reviewer/) | reviewer |

The code is shared by the roles, so it is kept once in [runtime/](runtime/), a copy of `autose/` at the repository root. GitHub Actions only runs workflows from the root `.github/workflows/`, and those import `autose/`, so the root copies are the ones that run. Prompts are in [../prompts/](../prompts/).
