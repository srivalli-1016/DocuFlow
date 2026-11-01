---
title: Project Structure
description: A tour of every directory and file in the DocuFlow repository.
---

# Project Structure

```text
docuflow/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   └── documentation_request.yml
│   ├── workflows/
│   │   ├── deploy-docs.yml
│   │   ├── docs-validation.yml
│   │   └── pr-quality.yml
│   └── pull_request_template.md
├── docs/
│   ├── assets/
│   │   ├── css/docuflow.css
│   │   ├── images/
│   │   └── js/docuflow.js
│   ├── getting-started/
│   ├── user-guide/
│   ├── automation/
│   ├── developer-guide/
│   ├── resources/
│   ├── features.md
│   └── index.md
├── scripts/check_config.py
├── .markdownlint.json
├── .markdownlintignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── lychee.toml
├── mkdocs.yml
└── requirements.txt
```

## What each part does

| Path | Purpose |
| --- | --- |
| `docs/` | All site content. Every Markdown file here becomes a page. |
| `docs/assets/` | Custom CSS, JavaScript and images used by the theme. |
| `mkdocs.yml` | Site name, theme, extensions and the navigation tree. |
| `requirements.txt` | Pinned Python dependencies. |
| `.markdownlint.json` | Markdown style rules enforced in CI. |
| `lychee.toml` | Link checker retries, accepted status codes and exclusions. |
| `scripts/check_config.py` | Validates configuration files and workflow security rules. |
| `.github/workflows/` | The three GitHub Actions workflows. |
| `.github/ISSUE_TEMPLATE/` | Forms for bug reports and documentation requests. |
| `.github/pull_request_template.md` | The checklist shown in every pull request. |
| `CONTRIBUTING.md` | Short contribution guide that links to the full one on this site. |

## Generated files

`site/` holds the built website. It is created by `mkdocs build` and is listed in `.gitignore`, so never commit it. The
deployment workflow rebuilds it from source on every release.
