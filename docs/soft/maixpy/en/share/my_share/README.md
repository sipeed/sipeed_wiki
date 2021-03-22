---
title: MaixPy Experience Sharing —— XXX
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy experience sharing-XXX
---


This catalog is mainly used for sharing your own experience or tutorials, and it can also be moved with the author's permission to reprint, and famous sources.


## To participate in sharing, you need to master the knowledge in advance

* Use of git and github
* Use of github PR (pull request)

There is a brief introduction in the introductory tutorial, please learn by yourself for detailed usage

If you are not confident to master these skills, you can submit [issue](https://github.com/sipeed/MaixPy_DOC/issues) to explain the problem or contribute experience, etc. We will help you to add


## How to add


### Clone document to local

```
git clone https://github.com/sipeed/MaixPy_DOC
cd MaixPy_DOC
```


### New directory

Need to create a new directory dedicated to writing shared articles,
Create a folder in the `MaixPy_DOC/docs/maixpy/zh/share/my_share/` directory, the folder name can only be in lowercase English and underscore, you can name it with your English name, such as `tom` or `lihua`,
The following uses `MaixPy_DOC/docs/maixpy/zh/share/my_share/tom` as an example

Of course, if you write an English document, you need to put it in the `MaixPy_DOC/docs/maixpy/en/share/my_share/tom` folder

Create a file in this folder, name it `readme.md`, and use the `markdown` syntax to write and share in it,
Create a `MaixPy_DOC/docs/maixpy/zh/share/my_share/tom/assets` directory to store pictures,
The relative path is used to reference the pictures in the document. For example, if the path of an image is `MaixPy_DOC/docs/maixpy/zh/share/my_share/tom/assets/cover.jpg`, it will be in `MaixPy_DOC/docs/maixpy/zh/share/my_share/tom/readme.md `Use the following syntax to quote pictures in
```
![Cover](./assets/cover.jpg)
```

Note, don’t enlarge files in the folder, and don’t use too big pictures, otherwise the document warehouse will be huge


### Write documentation

To make the document look well-formed and easier to read,
To write a document **must** follow the grammar and format requirements: **See [document specification](../../contribute/doc_convention.md)**

**Document template**, write an article according to the template, you can modify it according to your own situation

```markdown


| Author | Contact | Personal Homepage |
| --- | --- | --- |
| XXX | XXXX@XXX.com | [github/sipeed](http://github.com/sipeed) |


## Introduction:

Describe the background of this sharing, the final effect display, etc., you can use pictures, GIFs or videos to display, but don’t put too large images in the `assets` folder, otherwise users will not be able to load them for a long time due to internet speed problems. , It loses its meaning



## Preparation:

### Preliminary knowledge

### Software and hardware environment to be prepared

#### Hardware

Graphic description of the development board, peripheral modules, etc. used

#### Software

Graphic description of the software tools used, MaixPy version
If you use third-party software tools, you can attach the relevant name or download link



## Process, specific title customization



## Process, specific title customization



## Results

It is recommended to add pictures to show the actual running effect



## to sum up

Summary of this sharing


## Questions and feedback

Can provide feedback



## Reference

Indicate the articles and source code cited in the article in a list here

* Cited article 1: https://www.sipeed.com

```


### Add this share to the directory column on the left side of the document


Open `MaixPy_DOC/docs/maixpy/zh/SUMMARY.md`, add your own share at the end, such as



```
## Community & Share

-[Featured Tutorial](./share/recommend_articles.md)
-[Open source project](./share/open_projects.md)
-Everyone's experience sharing
  * [Participation in experience sharing/sharing template](./share/my_share/README.md)
  * [jerry's model training tutorial](./share/my_share/jerry/README.md)

```

The effect after adding your own card is:

```
## Community & Share

-[Featured Tutorial](./share/recommend_articles.md)
-[Open source project](./share/open_projects.md)
-Everyone's experience sharing
  * [Participation in experience sharing/sharing template](./share/my_share/README.md)
  * [Model Training Tutorial-jerry](./share/my_share/jerry/README.md)
  * [How to design your own model-tom](./share/my_share/tom/README.md)
```

Note that there are two spaces in front of **\***, not `tab`


### Submit

After writing, submit the modification, and then submit the PR on github. After the PR is passed, the official document page will have this article
