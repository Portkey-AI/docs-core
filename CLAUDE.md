# Portkey Docs Repository

This repository contains the documentation for [Portkey AI](https://portkey.ai), hosted at https://portkey.ai/docs. Built using [Mintlify](https://mintlify.com).

## Quick Start

```bash
npm install -g mint
mint dev
```

## Adding New Pages

1. Create an `.mdx` file in the appropriate folder
2. Add frontmatter with `title` and optional `description`
3. Add the page path to `docs.json` in the correct navigation group (`docs.json` is the source of truth for navigation, tabs and page hierarchy)
4. Run `mint dev` to preview

## File Naming Conventions

- Use kebab-case for file names: `my-new-page.mdx`
- Index pages for sections are named after the section: `observability.mdx` (not `index.mdx`)
- Sub-features go in folders: `/observability/logs.mdx`
