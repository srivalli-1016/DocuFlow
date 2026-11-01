---
title: Pull Request Workflow
description: What happens on a pull request, how to read the checks and how to require them with branch protection.
---

# Pull Request Workflow

## The flow

1. Create a branch: `git switch -c docs/describe-the-change`.
2. Edit pages and run the local checks from [Quick Start](../getting-started/quick-start.md).
3. Push and open a pull request against `main`. Fill in the template.
4. Wait for the checks. Fix failures by pushing more commits; the checks run again.
5. Request a review. Merge when approved and green.

## The checks

| Check | Workflow | Verifies |
| --- | --- | --- |
| Markdown lint | `docs-validation.yml` | Markdown formatting |
| Strict build | `docs-validation.yml` | The site builds without warnings |
| Link check | `docs-validation.yml` | Internal and external links |
| Validation result | `docs-validation.yml` | One combined status for the three above |
| Configuration checks | `pr-quality.yml` | YAML syntax, navigation targets, workflow permissions and pinned actions |
| Pull request description | `pr-quality.yml` | The validation checklist from the template is still present |

The two workflows run in parallel. Nothing expensive is repeated: linting, building and link checking run once, in
`docs-validation.yml`.

## Require the checks with branch protection

!!! note "Administrator access required"

    Only repository administrators can change branch protection.

1. Open **Settings** then **Branches**.
2. Under **Branch protection rules**, choose **Add branch protection rule**.
3. Enter `main` as the branch name pattern.
4. Enable **Require a pull request before merging** and set at least one approval.
5. Enable **Require status checks to pass before merging** and **Require branches to be up to date before merging**.
6. Search for and add **Validation result** and **Configuration checks**.
7. Optionally enable **Do not allow bypassing the above settings** and save.

Status check names only appear in the search box after the workflows have run at least once in the repository, so open
a pull request first.

!!! tip "Rulesets"

    GitHub also offers repository rulesets (**Settings** then **Rules**) with the same options. Use whichever your
    organization prefers.

## Pull requests from forks

Workflows triggered by forks receive a read-only token and no secrets. DocuFlow needs neither, so contributors can open
pull requests from forks and get full validation. GitHub may require a maintainer to approve the first workflow run from
a new contributor.

## When a check fails

Open the failing check from the pull request, read the log and reproduce it locally. The
[Troubleshooting](../developer-guide/troubleshooting.md) page lists frequent causes.
