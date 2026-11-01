---
title: Documentation Validation
description: How the docs-validation workflow lints Markdown, builds the site strictly and reports one result.
---

# Documentation Validation

`docs-validation.yml` is the main quality gate. It has four jobs.

| Job | Name in the Checks tab | What it does |
| --- | --- | --- |
| `lint` | Markdown lint | Runs markdownlint against every Markdown file |
| `build` | Strict build | Runs `mkdocs build --strict`, then checks links in the built site offline |
| `links` | Link check | Runs lychee on source files, including external URLs |
| `result` | Validation result | Fails if any other job failed or was cancelled |

## Triggers

```yaml
on:
  pull_request:
    branches: [main]
  push:
    branches-ignore: [main]
    paths: ["docs/**", "mkdocs.yml", "requirements.txt", "*.md", ".markdownlint.json", "lychee.toml"]
  workflow_dispatch:
```

Pull requests are always validated, with no path filter, so the required **Validation result** check reports on every
pull request. Pushes to other branches are validated only when documentation or its configuration changed.

Pushes to `main` are not validated here because they were validated when the pull request ran, and the deployment
workflow builds the site again before publishing.

## Markdown lint

Rules live in `.markdownlint.json`. The most important ones:

| Rule | Setting | Why |
| --- | --- | --- |
| MD003 | ATX headings | One heading style across the repository |
| MD004 | Dash bullets | Consistent lists |
| MD007 | Four-space nesting | Required by Python-Markdown |
| MD013 | 120 characters, code and tables exempt | Readable diffs without breaking commands |
| MD040 | Code fences need a language | Reliable syntax highlighting |
| MD048 | Backtick fences | One fence style |

Run it locally:

```bash
npx --yes markdownlint-cli@0.45.0 "**/*.md"
```

!!! tip "Fix automatically"

    Add `--fix` to let markdownlint repair many violations, then review the diff.

## Strict build

`mkdocs build --strict` turns warnings into errors. A page missing from `nav`, a broken relative link, a wrong anchor or
an unknown configuration key fails the build. The `validation` block in `mkdocs.yml` selects which problems count as
warnings.

## The result job

Required status checks work best with one stable name. The `result` job depends on the other three with
`if: always()`, writes a summary table and exits non-zero unless all of them succeeded. Require **Validation result** in
branch protection and you never need to update the rule when jobs are added or renamed.

## Reading failures

1. Open the failing job and expand the failing step.
2. markdownlint prints `file:line rule description`. Fix that line.
3. MkDocs prints `WARNING - Doc file ... contains a link ... not found`. Correct the path.
4. Re-run the same command locally to confirm before pushing.

See [Troubleshooting](../developer-guide/troubleshooting.md) for common messages.
