#!/bin/bash

set -o errexit -o nounset

rev=$(git rev-parse --short HEAD)
BRANCH=$(if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo $TRAVIS_BRANCH; else echo $TRAVIS_PULL_REQUEST_BRANCH; fi)
echo "TRAVIS_BRANCH=$TRAVIS_BRANCH, BRANCH=$BRANCH"
curr_branch=$TRAVIS_BRANCH

cp -f index.html build/index.html
cp -f assets/favicon.ico build/gitbook/images/favicon.ico
cp -f assets/icon_sipeed.png build/gitbook/images/apple-touch-icon-precomposed-152.png

git clone -b gh-pages https://github.com/sipeed/Tang-Nano-DOC.git ./old
rm -rf ./old/.git/
echo "current build branch: --$curr_branch--"
if [[ "$curr_branch" == "master" ]]; then
    echo "master"
    if [[ -d './old/dev' ]]; then
        echo "copy dev"
        cp -r ./old/dev ./build/
    fi
    cd ./old
    v_folder=`find ./ -maxdepth 1 -name 'v*.*'`
    echo "version folder:$v_folder"
    if [[ "x$v_folder" != "x" ]]; then
        echo "copy version folder"
        cp -r $v_folder ../build/
    fi
    cd ..
elif [[ "$curr_branch" == "dev" ]]; then
    echo "dev"
    rm -rf ./old/dev
    mkdir ./old/dev
    cp -r ./build/* ./old/dev
    rm -rf ./build
    mv ./old ./build
else
    echo "not master or dev"
    rm -rf ./old/$curr_branch
    mkdir ./old/$curr_branch
    cp -r ./build/* ./old/$curr_branch
    rm -rf ./build
    mv ./old ./build
fi

cd build

git init

git config user.name $GIT_NAME

git config user.email $GIT_EMAIL

git remote add upstream "https://$GITHUB_TOKEN@github.com/sipeed/Tang-Nano-DOC.git"

# comment below because we don't need history of gh-pages, and use git push --force to cover history
# git fetch upstream

# git reset upstream/gh-pages

# echo "gprs.ai-thinker.com" > CNAME

git add -A

git commit -m "rebuild pages at ${rev}"

git push upstream HEAD:gh-pages --force

