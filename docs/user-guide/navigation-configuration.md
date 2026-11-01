---
title: Navigation Configuration
description: How the nav tree in mkdocs.yml controls tabs, the sidebar and previous/next links.
---

# Navigation Configuration

Navigation is defined in the `nav` section of `mkdocs.yml`. Without it, MkDocs lists every file alphabetically; with
it, you control order, labels and grouping.

## Structure

```yaml
nav:
  - Home: index.md
  - Documentation:
      - Getting Started:
          - Introduction: getting-started/introduction.md
          - Installation: getting-started/installation.md
      - Automation:
          - GitHub Actions Overview: automation/github-actions-overview.md
  - Features: features.md
```

- A top-level entry becomes a tab in the header because `navigation.tabs` is enabled.
- A nested entry under a tab becomes a heading in the sidebar because `navigation.sections` is enabled.
- The label is on the left of the colon and the path, relative to `docs/`, is on the right.

## Add a page

1. Create the Markdown file in the matching folder.
2. Add a line under the correct section of `nav`.
3. Run `mkdocs build --strict`.

A file that exists in `docs/` but is missing from `nav` produces an `omitted_files` warning, which the strict build
turns into a failure. This prevents orphaned pages.

## Reorder or rename

Move the line to change the order. Change only the label to rename a page without changing its URL. The previous and
next links at the bottom of each page follow the order in `nav`.

## Theme features that affect navigation

| Feature | Effect |
| --- | --- |
| `navigation.tabs` | Top-level entries appear as header tabs |
| `navigation.sections` | Second-level entries render as sidebar headings |
| `navigation.footer` | Previous and next links under the content |
| `navigation.top` | Back-to-top button after scrolling |
| `navigation.tracking` | The address bar follows the active heading |

## Verify

`python scripts/check_config.py` checks that every path in `nav` points to a real file, so mistakes are caught before
the build starts.
