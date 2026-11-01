# Contributing to DocuFlow

Thank you for helping improve DocuFlow. Documentation fixes, new pages and workflow improvements are all welcome.

The complete guide lives in the documentation site at `docs/developer-guide/contributing.md`. This page is the short
version.

## Quick steps

1. Fork or clone the repository and create a branch: `git switch -c docs/short-description`.
2. Set up your environment (see [Installation](docs/getting-started/installation.md)).
3. Edit Markdown files under `docs/` and register new pages in `mkdocs.yml`.
4. Run the checks locally:

    ```bash
    python scripts/check_config.py
    npx --yes markdownlint-cli@0.45.0 "**/*.md" ".github/**/*.md"
    mkdocs build --strict
    lychee --config lychee.toml --no-progress docs README.md CONTRIBUTING.md
    ```

5. Commit with a prefix such as `docs:`, `ci:`, `style:` or `chore:`.
6. Open a pull request against `main` and complete the template, including the validation checklist.

## Rules for workflow changes

- Pin every action to a full commit SHA and keep the version in a trailing comment.
- Keep `permissions` as small as possible.
- Do not add repository secrets or `pull_request_target`.

`python scripts/check_config.py` enforces these rules and also runs in pull requests.

## Reporting problems

Use the **Bug report** or **Documentation request** issue forms. Include the page, the expected result and the actual
result.

## Conduct

Be respectful, assume good intent and review the work rather than the person.
