Sipeed wiki source code
=====

Related site: [wiki.sipeed.com](https://wiki.sipeed.com)

If you want change document or add one, do the following choice.

## Contributing and article sharing

You are welcome to contribute to the wiki, fixing error, adding content, or sharing your article are all welcome.

Fork this repo and change docs, then create a `Pull Request`.

More contribute doc :
* [中文](./share_docs/zh/readme.md)
* [English](./share_docs/en/readme.md)


## Preview locally

```bash
git clone https://github.com/sipeed/sipeed_wiki.git
pip install teedoc
cd sipeed_wiki
teedoc install
teedoc serve
```

More build tool usage see [teedoc](http://github.com/teedoc/teedoc)

## For administator

GitHub action will automatically push changed doc to cloud server.
But if you did some special things like force commit, some files maybe missing on server, manually trigger the publish_upload_all action to build doc and upload all files to server.



