---
title: Contributing
description: How to propose, write and submit documentation changes to DocuFlow.
---

# Contributing

Thank you for improving the documentation. Small fixes are as welcome as new pages.

## Ways to help

- Fix a typo, unclear sentence or outdated command.
- Report a problem or request a page with the issue forms. Choose **New issue** in the repository and pick **Bug report**
  or **Documentation request**.
- Add a missing explanation, an example or a troubleshooting entry.

## Set up

Follow [Installation](../getting-started/installation.md), then work on a branch:

```bash
git switch -c docs/short-description
```

## Make the change

1. Edit or add Markdown files under `docs/`.
2. Follow [Writing Documentation](../user-guide/writing-documentation.md) for structure and style.
3. Register new pages in `mkdocs.yml`.
4. Add a line to the [Changelog](../resources/changelog.md) under **Unreleased** for user-visible changes.

## Validate before you push

```bash
python scripts/check_config.py
npx --yes markdownlint-cli@0.45.0 "**/*.md"
mkdocs build --strict
lychee --config lychee.toml --no-progress docs README.md CONTRIBUTING.md
```

## Commit messages

Use a short imperative summary with a prefix:

| Prefix | Use for |
| --- | --- |
| `docs:` | Content changes |
| `ci:` | Workflow changes |
| `style:` | CSS, JavaScript or design changes |
| `chore:` | Dependency or tooling updates |

## Open a pull request

Fill in the pull request template: describe what changed, link the issue, name the affected pages and tick the
validation checklist. Reviewers look at correctness, clarity and whether the checks pass.

## Changing workflows

Pin every action to a full commit SHA with the version in a comment, keep `permissions` minimal and never add secrets
or `pull_request_target`. `scripts/check_config.py` enforces these rules.

## Code of conduct

Be respectful and assume good intent. Give feedback on the work, not the person.
