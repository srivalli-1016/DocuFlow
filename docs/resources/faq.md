---
title: FAQ
description: Answers to common questions about DocuFlow, its cost and how to adapt it.
---

# FAQ

## Is DocuFlow free to run?

Yes. It uses open source tools, GitHub Actions and GitHub Pages. Public repositories can use GitHub Actions and Pages at
no cost. Private repositories may have plan limits; check GitHub's current pricing and limits for your plan.

## Do I need any secrets or tokens?

No. The workflows use the temporary `GITHUB_TOKEN` that GitHub creates for each run, with only the permissions each job
declares.

## Why does the link check sometimes fail without a change on my side?

External websites go offline, move pages or block automated requests. lychee retries temporary errors three times and
accepts HTTP 429 rate limit responses, but a persistent failure is reported. See
[Broken Link Checking](../automation/broken-link-checking.md).

## Can I use a different link checker or linter?

Yes. Replace the relevant job in `docs-validation.yml` and update the local commands in the documentation. Keep the
`result` job, which aggregates the outcome.

## Why are actions pinned to commit SHAs?

A tag can be moved to different code. A full commit SHA cannot. Pinning prevents a compromised or changed release from
running in your workflow. Update pins deliberately and keep the version in a comment.

## Why does a docs-only change not trigger deployment?

It does when files under `docs/`, `mkdocs.yml` or `requirements.txt` change. Changes to files such as `README.md` or
issue templates do not alter the website, so they do not redeploy. Use **Run workflow** to deploy manually.

## Can I host the site somewhere other than GitHub Pages?

Yes. `mkdocs build --strict` produces static files in `site/`. Upload that folder to any static host and adjust
`deploy-docs.yml` accordingly.

## How do I add a plugin?

Add the pinned package to `requirements.txt`, list it under `plugins` in `mkdocs.yml`, then run
`mkdocs build --strict`. Keep dependencies minimal so builds stay fast and predictable.

## How do I change the colors or logo?

Edit the variables at the top of `docs/assets/css/docuflow.css` and replace `docs/assets/images/logo.svg`. See
[Configuration](../developer-guide/configuration.md).

## Does the site work offline?

The built site is static and works without a server, except for Mermaid diagrams and web fonts, which the theme loads
from the internet in the browser.
