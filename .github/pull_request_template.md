<!-- markdownlint-disable MD041 -->
## Summary

<!-- What does this pull request change, and why? One or two sentences. -->

## Related issue

<!-- Link the issue, for example "Closes #123". Write "None" if there is no issue. -->

## Affected documentation pages

<!-- List page paths, for example docs/automation/broken-link-checking.md -->

## Type of change

- [ ] New page
- [ ] Update to an existing page
- [ ] Fix (typo, broken link, wrong command)
- [ ] Workflow or configuration change
- [ ] Design or theme change

## Proposed changes

<!-- Summarize the edits so a reviewer knows what to look for. -->

## Validation checklist

- [ ] I previewed the change with `mkdocs serve`
- [ ] `python scripts/check_config.py` passes
- [ ] `npx --yes markdownlint-cli@0.45.0 "**/*.md"` passes
- [ ] `mkdocs build --strict` passes
- [ ] Links were checked with lychee, or I explained why not
- [ ] New pages are listed in `nav` in `mkdocs.yml`
- [ ] I updated the Changelog for user-visible changes
- [ ] Commands and file names in the text were tested and are accurate
