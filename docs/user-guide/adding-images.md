---
title: Adding Images
description: Store, reference and describe images so they work on every page and every theme.
---

# Adding Images

## Where images live

Place images in `docs/assets/images/`. Use descriptive lowercase file names such as `pipeline.svg`. Prefer SVG for
diagrams and logos, and compressed PNG or WebP for screenshots.

## Reference an image

Use a path relative to the page that contains it. From a page in `docs/user-guide/`:

```markdown
![Pipeline from Write to Deploy](../assets/images/pipeline.svg)
```

Here is that image rendered:

![Pipeline from Write to Deploy](../assets/images/pipeline.svg)

## Write useful alt text

- Describe what the image shows, not that it is an image.
- Leave the alt text empty only for decorative images.
- Repeat any text that appears inside a screenshot when it matters to the explanation.

## Size and alignment

The `attr_list` extension adds attributes after the image:

```markdown
![Logo](../assets/images/logo.svg){ width="96" }
![Logo](../assets/images/logo.svg){ align=right width="96" }
```

## Captions

```markdown
<figure markdown="span">
  ![Pipeline](../assets/images/pipeline.svg)
  <figcaption>The six stages of the DocuFlow pipeline</figcaption>
</figure>
```

## Checks that apply

The strict build fails when an image path is wrong, and lychee verifies the file exists. Large binary files slow down
cloning, so keep each image under 500 KB where possible.
