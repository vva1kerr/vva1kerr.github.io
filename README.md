# md-site

A zero-build GitHub Pages site that renders markdown files from a `docs/` folder.

## Structure

```
md-site/
├── index.html        ← the whole app (don't touch)
├── manifest.json     ← list of pages (edit this)
└── docs/
    ├── home.md
    ├── notes.md
    └── projects.md   ← drop your .md files here
```

## Adding a new page

1. Drop your `.md` file into `docs/`
2. Add an entry to `manifest.json`:

```json
{ "id": "mypage", "label": "My Page", "file": "docs/mypage.md" }
```

3. `git add . && git commit -m "add page" && git push`

That's it. No build step, no npm, no Jekyll.

## GitHub Pages setup

1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Set source to **Deploy from a branch → main → / (root)**
4. Your site will be at `https://yourusername.github.io/repo-name/`

## Direct links

Pages are linkable via hash: `yoursite.github.io/#notes`

bash scripts/gen-manifest.sh