---
title: Configuration
description: Reference for mkdocs.yml, the lint rules, the link checker and the environment variables DocuFlow reads.
---

# Configuration

## mkdocs.yml

| Key | Purpose |
| --- | --- |
| `site_name`, `site_description` | Title and metadata |
| `site_url` | Public address; read from `DOCS_SITE_URL` |
| `repo_url` | Repository link in the header; read from `DOCS_REPO_URL` |
| `theme` | Material for MkDocs settings: palette, fonts, features |
| `plugins` | Only `search` is enabled |
| `extra_css`, `extra_javascript` | DocuFlow styling and behavior |
| `markdown_extensions` | Syntax extensions such as admonitions, tabs and Mermaid |
| `validation` | Which problems become warnings, and therefore strict-build failures |
| `nav` | Navigation tree |

### Environment variables

```yaml
site_url: !ENV [DOCS_SITE_URL, ""]
repo_url: !ENV [DOCS_REPO_URL, ""]
```

The `!ENV` tag reads a variable and falls back to the second value. Leaving them empty is valid for local work. In
GitHub Actions, `deploy-docs.yml` sets both.

### Change colors

Colors are CSS variables at the top of `docs/assets/css/docuflow.css`. Change `--df-blue` and `--df-violet` for the
accent gradient and the `--md-primary-fg-color` values per scheme for the header.

## .markdownlint.json

Documented in [Documentation Validation](../automation/documentation-validation.md). To relax a rule for one file, add
an HTML comment such as `<!-- markdownlint-disable MD013 -->` followed by an explanation.

!!! note "Why MD046 is disabled"

    The `code-block-style` rule reports indented blocks as code. Admonition and tab bodies are indented by design, so
    the rule would flag valid content. Fenced style is still enforced through MD040 (language required) and MD048
    (backtick fences).

## lychee.toml

Documented in [Broken Link Checking](../automation/broken-link-checking.md).

## requirements.txt

Dependencies are pinned to exact versions. To upgrade:

1. Change the version number.
2. Run `pip install -r requirements.txt`.
3. Run `mkdocs build --strict` and fix any new warnings.
4. Note the change in the [Changelog](../resources/changelog.md).

## Repository variables

| Variable | Used by | Purpose |
| --- | --- | --- |
| `DOCS_SITE_URL` | `deploy-docs.yml` | Optional override, for example when using a custom domain |

No secrets are required.
