# profile-site

Kaz Sato's public portfolio. Deployed at:

- https://pf.kaz.ac/ (Japanese)
- https://pf.kaz.ac/en/ (English)

This repo is intentionally **not** where the content is drafted from
scratch — `~/Work/myprofile/` (private, not on GitHub) is where source
material and research live. But `index.html` itself (below) is the
**source of truth for the page content**; the English version and the
live site are both generated/deployed *from* it.

## Where content actually lives

| File | What it is |
|---|---|
| `index.html` | **The source.** All Japanese body text — hero copy, the "what I can help with" cards, selected work, debug case studies, publications list, about, contact. Edit this directly. |
| `../profile-updater/timeline_data.yaml` | The timeline entries (separate source, own repo — see its README). |
| `translate_map.py` | Japanese → English dictionary. Every translatable string in `index.html` must have an entry here, or `build_en.py` refuses to build. |
| `en/index.html` | **Generated.** Built by `build_en.py` from `index.html` + `translate_map.py`. Never hand-edit — it gets overwritten. |

## Updating content

1. Edit `index.html` directly (the Japanese text).
2. If you added/changed any visible text, add its translation to
   `translate_map.py`. `build_en.py` will tell you exactly what's missing
   if you forget — it aborts rather than silently leaving Japanese text on
   the English page.
3. If the timeline changed: see `../profile-updater/README.md` first
   (`timeline_data.yaml` → `translate_map.py` → `build_en_yaml.py` →
   `gen_timeline.py`), then come back here.
4. Preview locally before pushing (see below).
5. `git add -A && git commit && git push` — GitHub Actions deploys
   automatically (see below).

## Local preview

```
./preview.sh          # serves on localhost:8420
./preview.sh 3000      # or a specific port
```

Rebuilds `en/index.html` first, then serves this directory with Python's
stdlib `http.server` — the same plain static-file behavior nginx uses on
the VPS (`try_files $uri $uri/ =404` + `index index.html`), so what you
see locally matches production. Doesn't touch git or the live site.

- 日本語: http://localhost:8420/
- English: http://localhost:8420/en/

Ctrl-C to stop.

## Deploy (automatic via GitHub Actions)

`.github/workflows/deploy.yml` runs on every push to `main`: it SSHes into
the VPS using a deploy-only key (`VPS_DEPLOY_KEY` repo secret) that's
restricted server-side to `cd /var/www/pf.kaz.ac && git pull` — nothing
else, even if the key ever leaked. No manual VPS step needed; `git push`
is the whole deploy.

To check a deploy: `gh run list --repo satbah/profile-site --limit 3`
