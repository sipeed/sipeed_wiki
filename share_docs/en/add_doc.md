# Share article

## Prepare

- This site is built by teedoc, so we need to install it first.

### About teedoc

If you have trouble using this site, pleasr refer to https://teedoc.github.io/en/

### build locally

* Install teedoc

```
pip3 install teedoc --upgrade
```

* Get site source files

```
git clone https://github.com/sipeed/sipeed_wiki.git
```

* Install related plugins

```
cd sipeed_wiki
teedoc install
```

* build and serve locally

```
teedoc serve
```

then visit [http://127.0.0.1:2333](http://127.0.0.1:2333) to see your local site

## Add article

Normally all docs are put in the folder named docs which is in the root path.

When finishing writing the document you want to share under the appropriate corresponding directory, edit the file with name **sidebar** to make your file to be shown in the corresponding place on the web page.

Then you can then view the effect in the locally built site.

If you think you have finish this job, just create pull request and we'll merge it .
