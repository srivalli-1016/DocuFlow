---
title: Writing Documentation
description: Conventions for structuring, naming and writing DocuFlow pages.
---

# Writing Documentation

Good pages are easy to find, easy to scan and easy to keep correct. These conventions apply to every page in `docs/`.

## File and folder naming

- Use lowercase words separated by hyphens: `broken-link-checking.md`.
- Put a page in the folder that matches its navigation section.
- Keep names stable. Renaming a file changes its URL and breaks inbound links.

## Page anatomy

Every page starts with front matter and a single level-one heading:

```markdown
---
title: Broken Link Checking
description: How DocuFlow finds and reports broken links.
---

# Broken Link Checking

Open with one or two sentences that say what the page covers.

## First section
```

- `title` is used for the browser tab and search results.
- `description` is used in the page metadata.
- The `#` heading appears exactly once, directly after the front matter.
- Headings go down one level at a time: `##` then `###`, never `##` then `####`.

## Writing style

- Lead with the outcome. Say what the reader will achieve before explaining how.
- Prefer short paragraphs and numbered steps for procedures.
- Use the second person ("you") and the active voice.
- Show commands in code blocks and name the file they belong to.
- Explain error messages with the exact text a reader would see.

## Linking between pages

Link to other pages with a relative path to the Markdown file, never a full URL:

```markdown
See [Local Development](../developer-guide/local-development.md).
```

MkDocs rewrites the path to the correct URL and the strict build fails if the target does not exist. Link to a section
with an anchor: `../automation/broken-link-checking.md#configuration`.

!!! warning "Avoid absolute site paths"

    Links such as `/user-guide/page/` break when the site is hosted under a repository path like `/docuflow/`.

## Before you commit

1. Preview the page with `mkdocs serve`.
2. Run markdownlint and `mkdocs build --strict`.
3. Add the page to the navigation if it is new. See
   [Navigation Configuration](navigation-configuration.md).
