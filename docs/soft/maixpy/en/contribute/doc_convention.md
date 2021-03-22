---
title: Document contribution specification
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: document contribution specification
---


There are several situations you may need to read this document:
* Found that the document is wrong or there is content that needs to be added, and will want to participate in the modification
* Submit tutorial/experience/open source project sharing etc.



In order to make the document look uniform in style, the content is not repeated and there is no error, and the writing needs to follow the same specification, all contributors **must** write documents according to this article;
If you have any doubts about the template format and content, please go to the project repository [MaixPy_DOC](https://github.com/sipeed/MaixPy_DOC) to submit `ISSUE`.


🙇‍ Thank you for your enthusiastic support!


## To participate in the contribution, you need to master the knowledge in advance

* Use of git and github
* Use of github PR (pull request)

There is a brief introduction in the introductory tutorial, please learn by yourself for detailed usage

If you are not confident to master these skills, you can submit [issue](https://github.com/sipeed/MaixPy_DOC/issues) to explain the problem or contribute experience, etc. We will help you to add

## Introduction to the file system


The document is built using gitbook, and simple and efficient Markdown is used to write content. It is recommended to use `Typora` or `VS Code` with `MarkDown Preview Enhanced` plug-in as the document editor


The source code of the document is hosted at [github](https://github.com/sipeed/MaixPy_DOC)

For the local preview method, see [README.md](https://github.com/sipeed/MaixPy_DOC/blob/master/README.md) of the document source code

The documents are available in two languages, Chinese and English, respectively, placed in the `zh` and `en` folders, where `SUMMARY.md` is the directory item on the left side of the document, and the other `md` files are specific document files, root The `assets` directory under the directory contains image resource files common to two languages



## Markdown syntax

If you haven’t touched the basic grammar of Markdown, please spend half an hour to learn it. I recommend the github tutorial: [github Markdown Tutorial](https://guides.github.com/features/mastering-markdown/)

In this article, we need to pay attention to the following points:

### The grammar tags of the heading category must be separated by spaces, and a blank line is required between the headline and the main body, for example:

```markdown
## This is a secondary heading

* This is list item 1
* This is list item 2

```
The following is not correct, and it may cause parsing errors and malformed formats.

```markdown
##This is the secondary title
*This is list item 1
*This is list item 2
```

### All pages have only one first-level title

Since the catalog needs to be automatically generated, it is mainly to ensure that the automatically generated catalog is correct.
Write each page like this

```
                (At least one blank line is required, 2 lines are recommended)

## Level 2 heading 1 (The first level heading cannot be used here, and a # sign cannot be used. There is also no need to write a serial number, the serial number will be automatically generated)
                ( Skip a line )
text
                (At least one blank line)
### Third-level heading (similar to second-level heading, no need to write, it will be automatically generated)

text

## Secondary Title 2

text


```

### Title number

All titles **do not need to write a number, **will be automatically generated** for example

```
## Title One

### Subtitle 1

## Title Two
```
final effect:

```
1. Title One
  1.1 Subheading 1

2. Title Two
 
```

If manually written, the final display will be repeated, so be careful!


### Link

Due to the large number of pages and the need to link to resources such as pictures, relative paths are used when writing links.
For example, the directory structure is as follows
```
assets/ (Put common resource files)
|
      ----pic000.png
en/
|
   ----- get_started/
|
                  ---- assets/ (Put the common resource file of md file in get_started directory)
|
                             ------ pic.png
|
                  ---- get_hardware.md
|
                  ---- how_to_read.md
zh/
```

If you paste an image in `get_hardware.md`, put the image in the `assets` folder, and use the following code to reference the image
```
![pic](assets/pic.png)
![pic](../../assets/pic000.png)
```


### Mixed Chinese and English

When writing Chinese documents, try to use spaces to separate Chinese mixed with English, and try to use full-width symbols for punctuation.
Mainly to make the document more conspicuous.
such as:

---------

```markdown
In Micropython, we often use `deinit` to represent the destructor, not to set the default value like STM32
```
In Micropython, we often use `deinit` to represent the destructor, not to set the default value like STM32

----------

```markdown
In Micropython, we often use deinit to represent the destructor instead of setting the default value like STM32
```

In Micropython, we often use deinit to represent the destructor instead of setting the default value like STM32

---------


## table of Contents

* Multiple languages ​​are placed in different directories, `en` and `zh` directories

* The generated document directory is edited in the folder `SUMMARY.md` of the corresponding language

* The source document folder should correspond to a folder as much as possible for a functional module, and the resource files (pictures) should be placed in the `assets` folder directory under the root directory of the corresponding md document, so that both Chinese and English documents can refer to the same pictures and generate The URL is the same, and it is more convenient to add, delete and modify at the same time.
* At the same time, in order to be able to use both Chinese and English documents, try not to mark Chinese or English in the picture. You can mark the label, and then the document is explained with the label. The pictures for a specific language are placed in the `assets` directory under the current path:

```
assets/ (Put public resource files, both Chinese and English can be cited)
en/
|
   ----- get_started/
|
                  ---- assets/ (resource files of md files in the get_started directory, only for English use)
|
                  ---- get_hardware.md
|
                  ---- how_to_read.md
zh/
```

## file name

* The file name is special except `README.md`, other file names use lowercase + underscore naming method, such as `get_hardware.md`



## Chinese and English (multilingual) page file directory structure and file name are the same

Since there is a multi-language switch option in the last generated page, after clicking switch, the same path of the corresponding language will be directly accessed, so the directory structure and file name in Chinese and English must be the same.

For example, when English is accessing `en/get_started/how_to_read.md`, after clicking the language switch button, it will automatically visit `zh/get_started/how_to_read.md`, if this file does not exist, it will report a `404` error!


## Contents and links

Try to guide readers to use the table of contents, and use the jump links in the text with caution. If the links jump chaotically, the document will look messy and it will be more difficult to read.

## Module documentation content

* The header of the file contains module introduction, resource introduction, usage notes, and routines
* Need to point out the constructor, function, constant, etc.
* **Note that you can't be lazy, just simply translate the function name again, you need to explain in detail the function of the function, the value range of the parameters and the points of attention**

## Multi-version management

In addition to supporting Chinese and English (multi-language) documents (not automatic translation, manual modification is required), multi-version management is also done.

Each version is a branch, and there are requirements for the branch name, which are:
* `master` branch is the main branch
* `dev` branch is the development branch
* Other historical versions of releases start with lowercase `v`, for example, create a branch called `v1.2`

After creating a new branch, you need to modify the version link in `book.json` in the directory of each language version, otherwise readers cannot find the entry

You can preview locally under the newly created branch (see the root directory `README.md` for preview method). Note that the page previewed at this time is the content of the current branch. If you want to preview the content of other branches locally, you need to switch to other branches before previewing That's it.

After confirming that the correct modification is completed, push the branch to the remote (github), the automatic build system will automatically build and publish to the pages branch, and the effect can be seen after the construction is completed and the URL is accessed.
