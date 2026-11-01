---
title: Quick Start
description: Preview the site, edit a page and run every check in about ten minutes.
---

# Quick Start

This walkthrough assumes you completed [Installation](installation.md) and your virtual environment is active.

## 1. Start the development server

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000/>. The page reloads whenever you save a file.

## 2. Edit a page

Open `docs/getting-started/introduction.md`, change a sentence and save. The browser refreshes automatically.

## 3. Add a new page

Create `docs/user-guide/my-first-page.md`:

```markdown
---
title: My first page
description: A short page used to learn the workflow.
---

# My first page

This page was added from the Quick Start.
```

Register it in `mkdocs.yml` under the `User Guide` section:

```yaml
nav:
  - Documentation:
      - User Guide:
          - My first page: user-guide/my-first-page.md
```

## 4. Run the checks

Run the same commands that GitHub Actions runs:

```bash
npx --yes markdownlint-cli@0.45.0 "**/*.md"
mkdocs build --strict
lychee --config lychee.toml --no-progress docs README.md CONTRIBUTING.md
python scripts/check_config.py
```

Every command must finish without errors before you open a pull request.

## 5. Open a pull request

```bash
git switch -c docs/my-first-page
git add docs/user-guide/my-first-page.md mkdocs.yml
git commit -m "docs: add my first page"
git push --set-upstream origin docs/my-first-page
```

Open a pull request on GitHub. The workflows start automatically; the
[Pull Request Workflow](../automation/pull-request-workflow.md) page explains what each check reports.

!!! note

    Delete the example page before committing if you only followed this guide to learn the process.
