---
title: Automatic Deployment
description: Configure GitHub Pages and understand how deploy-docs.yml publishes the MkDocs site.
---

# Automatic Deployment

`deploy-docs.yml` publishes the site whenever documentation changes reach `main`.

## One-time repository setup

1. Create a repository on GitHub and push this project to it.
2. Open **Settings** then **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open **Actions**, select **Deploy Documentation** and choose **Run workflow** to publish the first time.
5. When the run finishes, the deploy job prints the site address and the **Pages** settings page shows it.

!!! warning "Deployment is not instant"

    Nothing is published until the workflow has run successfully. If the run fails, read the log; the most common
    cause is the Pages source not being set to GitHub Actions.

## What the workflow does

```mermaid
flowchart LR
    A[Checkout] --> B[Set up Python 3.12]
    B --> C[pip install -r requirements.txt]
    C --> D[configure-pages]
    D --> E[mkdocs build --strict]
    E --> F[upload-pages-artifact]
    F --> G[deploy-pages]
```

Key points:

- **Triggers:** pushes to `main` that change `docs/`, `mkdocs.yml`, `requirements.txt` or the workflow itself, plus
  manual dispatch.
- **Permissions:** `contents: read` for checkout, `pages: write` and `id-token: write` for the deployment job only.
- **Concurrency:** group `pages` with `cancel-in-progress: false`, so a running deployment finishes before the next
  starts.
- **Environment:** `github-pages`, which records each deployment and exposes the URL.
- **Configuration:** `actions/configure-pages` supplies the site address; the workflow passes it to MkDocs as
  `DOCS_SITE_URL`, and the repository URL as `DOCS_REPO_URL`. Nothing is hardcoded.

## Verify automatic deployment

1. Make a small edit on a branch and merge it through a pull request.
2. Open **Actions**. A **Deploy Documentation** run starts within seconds of the merge.
3. After it succeeds, reload the published site and confirm your edit.

## Custom domains

Set a custom domain in **Settings** then **Pages**. Then set the repository variable `DOCS_SITE_URL`, or edit the
workflow, so generated links use the new address.

## Rolling back

Revert the merge commit on `main`. The workflow runs again and publishes the previous content. You can also re-run an
older successful workflow run from the Actions tab.
