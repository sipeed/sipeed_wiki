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
git clone https://github.com/sipeed/sipeed_wiki.git
cd sipeed_wiki
uv sync
uv run teedoc serve
```

`uv sync` creates/updates the `.venv` from [`pyproject.toml`](./pyproject.toml) and `uv.lock`, which already includes `teedoc` and all plugins used by this site (so `teedoc install` is not needed).
Install [uv](https://docs.astral.sh/uv/) first if you don't have it.

More build tool usage see [teedoc](http://github.com/teedoc/teedoc)

## For administrator

GitHub action will automatically push changed doc to cloud server.
But if you did some special things like force commit, some files maybe missing on server, manually trigger the publish_upload_all action to build doc and upload all files to server.



