---
title: Troubleshooting
description: Common DocuFlow errors, what they mean and how to fix them.
---

# Troubleshooting

## Setup problems

### `mkdocs: command not found`

The virtual environment is not active. Activate it (see [Installation](../getting-started/installation.md)) and run
`pip install -r requirements.txt` if the problem remains.

### PowerShell refuses to activate the environment

Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` in the same window, then activate again.

### `Address already in use` when running `mkdocs serve`

Another process uses port 8000. Stop it or run `mkdocs serve --dev-addr 127.0.0.1:8001`.

## Build errors

### `Doc file '...' contains a link '...', but the target is not found among documentation files`

The relative path is wrong or the target page was renamed. Link to the Markdown file relative to the current page, for
example `../automation/broken-link-checking.md`.

### `The following pages exist in the docs directory, but are not included in the "nav" configuration`

Add the page to `nav` in `mkdocs.yml`, or remove the file.

### `contains a link '...#section', but the doc ... does not contain an anchor`

The heading was renamed or mistyped. Anchors are the lowercase heading text with hyphens instead of spaces.

### `Aborted with N warnings in strict mode!`

This is a summary. Scroll up to read the `WARNING` lines above it and fix each one.

## Lint errors

| Message | Fix |
| --- | --- |
| `MD040 fenced-code-language` | Add a language after the opening fence, or `text` |
| `MD013 line-length` | Wrap the line at 120 characters |
| `MD022 blanks-around-headings` | Add a blank line before and after the heading |
| `MD031 blanks-around-fences` | Add a blank line before and after the code block |
| `MD007 ul-indent` | Indent nested bullets by four spaces |
| `MD025 single-title` | Keep a single `#` heading per page |

## Link check errors

### `Network error` or `Timeout` on an external link

lychee retried three times. Open the link in a browser. If it works, re-run the workflow. If it is down, replace it or
wait for the host to recover.

### `Cannot find fragment`

The target heading does not exist. Check spelling and remember that renaming a heading changes its anchor.

## GitHub Actions problems

### The deploy workflow fails at `configure-pages` with `Get Pages site failed`

Pages is not enabled. In **Settings** then **Pages**, set the source to **GitHub Actions** and re-run.

### The deploy job fails with a permissions error

Confirm the repository setting **Actions** then **General** then **Workflow permissions** allows the workflow to run,
and that `deploy-docs.yml` still declares `pages: write` and `id-token: write` on the deploy job.

### A required check never appears on the pull request

GitHub only lists a status check in branch protection after the workflow has run once in the repository. Open a pull
request first, wait for the workflows to finish, then add **Validation result** and **Configuration checks** to the rule.
Also confirm that Actions is enabled under **Settings** then **Actions**.

### The site loads without styles after deployment

`site_url` is wrong. Check the **Deploy Documentation** log for the value used by the build, or set the repository
variable `DOCS_SITE_URL`.
