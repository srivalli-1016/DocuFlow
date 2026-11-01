---
title: DocuFlow
description: Documentation that builds itself. Write Markdown, validate with GitHub Actions, publish to GitHub Pages.
hide:
  - navigation
  - toc
---

<section class="df-hero" markdown="1">
<div class="df-wrap" markdown="1">
<div markdown="1">

<h1>Documentation That Builds Itself.</h1>

<p class="df-sub">Write Markdown. Automate validation. Deploy beautiful documentation with GitHub Actions.</p>

<div class="df-actions" markdown="1">

[Explore Documentation](getting-started/introduction.md){ .df-btn .df-btn--primary }
[View on GitHub](https://github.com){ .df-btn .df-btn--ghost data-df-repo="" }

</div>

<p class="df-tagline">Write. Validate. Automate. Publish.</p>

</div>
<div class="df-glass" aria-label="Jobs in the docs-validation workflow">
  <div class="df-glass__title"><span>Pull request to main</span><code>docs-validation.yml</code></div>
  <div class="df-job"><strong>Markdown lint</strong><span>markdownlint-cli with .markdownlint.json</span></div>
  <div class="df-job"><strong>Strict build</strong><span>mkdocs build --strict, then an offline link check</span></div>
  <div class="df-job"><strong>Link check</strong><span>lychee on source files and external URLs</span></div>
  <div class="df-job"><strong>Validation result</strong><span>One status to require in branch protection</span></div>
</div>
</div>
</section>

<section class="df-section" id="features" markdown="1">
<div class="df-wrap" markdown="1">

<h2>What DocuFlow automates</h2>

<p class="df-lead">
Every step between a Markdown edit and a published page is a check you can read, run locally and trust.
</p>

<div class="df-grid" markdown="1">

<div class="df-card" markdown="1">

:material-check-decagram:{ .lg }

### Automated Documentation Validation

markdownlint enforces heading order, list style, fenced code languages and line length on every change.

[Read how validation works](automation/documentation-validation.md)

</div>

<div class="df-card" markdown="1">

:material-link-variant:{ .lg }

### Broken Link Detection

lychee checks internal files, anchors and external URLs, retrying temporary network errors before it fails.

[Read about link checking](automation/broken-link-checking.md)

</div>

<div class="df-card" markdown="1">

:material-sync:{ .lg }

### GitHub Actions CI/CD

Three workflows with least-privilege permissions and actions pinned to full commit SHAs.

[See the workflows](automation/github-actions-overview.md)

</div>

<div class="df-card" markdown="1">

:material-source-pull:{ .lg }

### Pull Request Quality Checks

Reviewers get a clear pass or fail for formatting, build, links and configuration before they read a word.

[Follow the pull request flow](automation/pull-request-workflow.md)

</div>

<div class="df-card" markdown="1">

:material-rocket-launch:{ .lg }

### Automatic Publishing

Merging to main builds the real MkDocs site and publishes it with the official GitHub Pages actions.

[Set up deployment](automation/automatic-deployment.md)

</div>

<div class="df-card" markdown="1">

:material-magnify:{ .lg }

### Powerful Documentation Search

Full-text search with suggestions and highlighting runs in the browser, so there is no search server to host.

[Learn about the site features](features.md)

</div>

</div>

</div>
</section>

<section class="df-section" id="how-it-works" markdown="1">
<div class="df-wrap" markdown="1">

<h2>How it works</h2>

<p class="df-lead">Select a stage to see what happens and which file controls it.</p>

<div data-df-pipeline>
  <div class="df-steps" role="tablist" aria-label="Documentation pipeline stages">
    <button class="df-step" role="tab" id="df-tab-0" aria-controls="df-panel-0">Write Markdown</button>
    <button class="df-step" role="tab" id="df-tab-1" aria-controls="df-panel-1">Push Changes</button>
    <button class="df-step" role="tab" id="df-tab-2" aria-controls="df-panel-2">Validate</button>
    <button class="df-step" role="tab" id="df-tab-3" aria-controls="df-panel-3">Review</button>
    <button class="df-step" role="tab" id="df-tab-4" aria-controls="df-panel-4">Merge</button>
    <button class="df-step" role="tab" id="df-tab-5" aria-controls="df-panel-5">Deploy</button>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-0" aria-labelledby="df-tab-0">
    <h3>Write Markdown</h3>
    <p>Edit or add a page under <code>docs/</code>, preview it with <code>mkdocs serve</code>, and register new pages
    in <code>mkdocs.yml</code>.</p>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-1" aria-labelledby="df-tab-1">
    <h3>Push Changes</h3>
    <p>Commit to a branch and open a pull request against <code>main</code>. The template asks for the affected page
    and a validation checklist.</p>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-2" aria-labelledby="df-tab-2">
    <h3>Validate</h3>
    <p><code>docs-validation.yml</code> runs markdownlint, a strict MkDocs build and the lychee link checker.
    <code>pr-quality.yml</code> validates configuration and workflow security rules.</p>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-3" aria-labelledby="df-tab-3">
    <h3>Review</h3>
    <p>Reviewers read the diff with the check results beside it. Branch protection can require the checks to pass
    before a merge is allowed.</p>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-4" aria-labelledby="df-tab-4">
    <h3>Merge</h3>
    <p>Merging to <code>main</code> triggers the deployment workflow whenever <code>docs/</code>,
    <code>mkdocs.yml</code> or <code>requirements.txt</code> changed.</p>
  </div>
  <div class="df-panel" role="tabpanel" id="df-panel-5" aria-labelledby="df-tab-5">
    <h3>Deploy</h3>
    <p><code>deploy-docs.yml</code> builds the site, uploads it as a Pages artifact and publishes it with
    <code>actions/deploy-pages</code>.</p>
  </div>
</div>

</div>
</section>

<section class="df-section df-cta" markdown="1">
<div class="df-wrap" markdown="1">

<h2>Run it on your machine in five commands</h2>

<p class="df-lead" style="margin-left:auto;margin-right:auto">
Clone, create a virtual environment, install and serve. The site opens at 127.0.0.1:8000.
</p>

<div class="df-actions" markdown="1">

[Start the Quick Start](getting-started/quick-start.md){ .df-btn .df-btn--primary }
[Contribute](developer-guide/contributing.md){ .df-btn .df-btn--ghost }

</div>

</div>
</section>
