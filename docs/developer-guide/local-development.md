---
title: Local Development
description: Run the DocuFlow site locally, use live reload and reproduce every CI check on your machine.
---

# Local Development

## Daily workflow

=== "macOS and Linux"

    ```bash
    source .venv/bin/activate
    mkdocs serve
    ```

=== "Windows PowerShell"

    ```powershell
    .venv\Scripts\Activate.ps1
    mkdocs serve
    ```

The site is served at <http://127.0.0.1:8000/> and rebuilds when files change. Stop it with ++ctrl+c++.

## Useful options

| Command | Effect |
| --- | --- |
| `mkdocs serve --dev-addr 127.0.0.1:8001` | Use a different port when 8000 is busy |
| `mkdocs serve --dirty` | Rebuild only changed pages for faster reloads on large sites |
| `mkdocs build --strict` | Build into `site/`, failing on any warning |
| `mkdocs build --clean` | Remove stale files from `site/` first |

## Set the site and repository URLs

Both are optional locally. To test the repository link in the header, export the variable before serving:

=== "macOS and Linux"

    ```bash
    export DOCS_REPO_URL="https://github.com/<your-username>/<your-repository>"
    mkdocs serve
    ```

=== "Windows PowerShell"

    ```powershell
    $env:DOCS_REPO_URL = "https://github.com/<your-username>/<your-repository>"
    mkdocs serve
    ```

## Reproduce CI locally

Run these in order. They match the workflow steps exactly.

```bash
python scripts/check_config.py
npx --yes markdownlint-cli@0.45.0 "**/*.md"
mkdocs build --strict
lychee --config lychee.toml --no-progress docs README.md CONTRIBUTING.md
lychee --config lychee.toml --offline --no-progress --root-dir "$PWD/site" site
```

On Windows PowerShell replace `"$PWD/site"` with `"$PWD\site"`.

## Test the responsive layout

Open the browser developer tools and enable the device toolbar, or resize the window below 960 pixels. The navigation
becomes a drawer and the landing page columns stack.

## Preview a production build

```bash
mkdocs build --strict
python -m http.server --directory site 8080
```

Open <http://127.0.0.1:8080/>. This serves the same files that GitHub Pages will serve.
