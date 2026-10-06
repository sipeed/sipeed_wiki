Sipeed wiki source docs
=====

Sipeed official Wiki: [wiki.sipeed.com](https://wiki.sipeed.com)


## Contributing and article sharing

You are welcome to contribute to the wiki, fixing error, adding content, or sharing your article are all welcome.

Fork this repo and change docs, then create a `Pull Request`.

More contribute doc :
* [中文](./share_docs/zh/readme.md)
* [English](./share_docs/en/readme.md)


## Preview locally

```bash
git clone --depth=1 https://github.com/sipeed/sipeed_wiki.git
cd sipeed_wiki
uv sync
uv run teedoc serve
```

`uv sync` creates/updates the `.venv` from [`pyproject.toml`](./pyproject.toml) and `uv.lock`, which already includes `teedoc` and all plugins used by this site (so `teedoc install` is not needed).
Install [uv](https://docs.astral.sh/uv/) first if you don't have it.

### Why `--depth=1`

This is a documentation site, so most of the repo is images. Git keeps every past revision
of every one of them forever, including large originals that have since been replaced by
compressed versions. A full clone therefore downloads roughly **1 GB of history** even
though you only ever need the current version of each file.

`--depth=1` fetches just the latest commit and skips all of that. Editing docs and opening
a pull request works exactly the same from a shallow clone. Use a full clone only when you
actually need the history (`git log`, `git blame`, `git bisect`) — you can always deepen a
shallow clone later with `git fetch --unshallow`.

When adding images, please keep them small (ideally under 300 KB, 500 KB max): anything
committed here stays in the history for good, so an oversized image costs every future
contributor bandwidth even after it is deleted. See [AGENTS.md](./AGENTS.md) for the full
image and authoring guidelines.

More build tool usage see [teedoc](http://github.com/teedoc/teedoc)

## For administrator

GitHub action will automatically push changed doc to cloud server.
But if you did some special things like force commit, some files maybe missing on server, manually trigger the publish_upload_all action to build doc and upload all files to server.



