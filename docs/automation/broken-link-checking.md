---
title: Broken Link Checking
description: How lychee checks internal and external links, and how DocuFlow handles flaky networks.
---

# Broken Link Checking

DocuFlow uses [lychee](https://lychee.cli.rs/) in two passes.

## Pass 1: source files

```bash
lychee --config lychee.toml --no-progress docs README.md CONTRIBUTING.md
```

This pass checks Markdown links between files, anchors inside files and every external URL. It catches a deleted page
or a renamed heading before the site is built.

## Pass 2: built site

```bash
lychee --config lychee.toml --offline --no-progress --root-dir "$PWD/site" site
```

This pass reads the generated HTML and verifies every internal link and local asset such as CSS, JavaScript and images.
It runs offline inside the **Strict build** job, right after the site is built, so it is fast and cannot fail because of
the network. Pass 1 runs in the separate **Link check** job.

## Configuration

Settings live in `lychee.toml`:

| Setting | Value | Reason |
| --- | --- | --- |
| `max_retries` | 3 | Retry temporary failures |
| `retry_wait_time` | 3 seconds | Give the remote host time to recover |
| `timeout` | 20 seconds | Avoid hanging on slow hosts |
| `accept` | 200 to 299, and 429 | A 429 means the host rate limited the request, not that the page is gone |
| `include_fragments` | true | Verify `#anchor` targets in local files |
| `exclude_loopback` | true | `127.0.0.1` and `localhost` only exist on your machine |

## What fails the check

- A relative link to a file that does not exist.
- An anchor that does not match a heading.
- An external URL that returns 404, 410 or another error after three retries.
- A DNS or connection failure that persists across retries.

## Exclusions

Exclusions are listed with a comment explaining why. Current ones cover documentation example domains such as
`example.com` and placeholder repository URLs the reader is told to replace. Add an exclusion only when a link is
intentionally unreachable, never to silence a real failure.

## External links are not guaranteed

Websites change and networks fail. A green link check proves links worked when the check ran, not forever. If an
external host is down for a long time, the check fails honestly; re-run the workflow after the outage or replace the
link with a stable source such as an archive copy.

!!! warning "Rate limits"

    Some sites block automated requests. If a trusted site always fails in CI, first confirm the link in a browser,
    then consider an exclusion with a written justification.
