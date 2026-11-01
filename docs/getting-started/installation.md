---
title: Installation
description: Install the tools needed to preview and validate DocuFlow on your own computer.
---

# Installation

You need Git and Python 3.12. Node.js is optional and only needed to run the Markdown linter locally.

## Requirements

| Tool | Version | Needed for |
| --- | --- | --- |
| Git | Any recent version | Cloning and contributing |
| Python | 3.12 recommended | MkDocs and the theme |
| Node.js | 20 or newer | Optional: running markdownlint locally |
| lychee | 0.24 or newer | Optional: running the link checker locally |

## Clone the repository

```bash
git clone <repository-url>
cd docuflow
```

Replace `<repository-url>` with the HTTPS or SSH address shown on your repository's GitHub page.

## Create a virtual environment and install dependencies

=== "macOS and Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

=== "Windows PowerShell"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

!!! tip "PowerShell execution policy"

    If activation fails with a message about running scripts, run
    `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` in the same window and try again.

## Verify the installation

```bash
mkdocs --version
```

The command prints the MkDocs version. If the command is not found, the virtual environment is not active. Activate it
again and retry.

## Optional: linting and link checking tools

markdownlint runs through `npx`, so nothing is installed globally:

```bash
npx --yes markdownlint-cli@0.45.0 "**/*.md"
```

lychee is a single binary. Install it with your package manager, for example `brew install lychee` on macOS or
`cargo install lychee` where Rust is available, or download a release from the
[lychee releases page](https://github.com/lycheeverse/lychee/releases).

Next: [Quick Start](quick-start.md).
