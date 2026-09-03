# profile-site

Kaz Sato's public portfolio — deployable output only. `index.html` is the
whole site (all images are embedded as data: URIs, no separate assets).

This repo is intentionally **not** where the content is authored. It's the
publish target: `~/Work/myprofile/` (private, not on GitHub) is where the
portfolio is drafted and reviewed; an approved version gets copied here as
`index.html` and pushed.

## Deploy (current: manual, same pattern as `line_msg`)

On the VPS, this repo is checked out into nginx's served directory. To
publish an update:

```
# locally, after copying the reviewed index.html here
git add index.html
git commit -m "..."
git push

# on the VPS
ssh <vps> "cd /path/to/profile-site && git pull"
```

## Roadmap

- [ ] GitHub Actions workflow that SSHes into the VPS and runs `git pull`
      automatically on push to `main`, using a deploy-only SSH key scoped
      to just that command. See `profile-updater`'s README for the fuller
      pipeline this fits into (draft → review → merge → auto-deploy).
