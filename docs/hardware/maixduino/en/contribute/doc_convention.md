Documentation Convention
=======

Documents are built using gitbook and written in simple and efficient Markdown

The documentation source code is hosted on [GitHub](https://github.com/sipeed/Maixduino_DOC)

## Markdown syntax

If you've never used the basic syntax of Markdown, please take half an hour to learn. We recommend the GitHub tutorial: [GitHub Markdown Tutorial](https://guides.github.com/features/mastering-markdown/)

In this article, we need to pay attention to the following points:

### The syntax tags of the title class must be separated by spaces. A blank line is required between the headline and the body, such as:

```markdown
## This is a secondary title

* This is list item 1
* This is list item 2

```
The following example is not correct, it may cause the parser to parse the file with errors.

```markdown
##This is a secondary title
*This is list item 1
*This is list item 2
```

### All pages have only one top level title

Because the need to automatically generate a directory, mainly to ensure that the automatically generated directory is correct.
Write each page like this
```
Page title/top level title
=======                          (There is at least three equals here)
                                 (At least one more blank line is required, 2 lines are recommended)

## Secondary title 1             (You cannot use a first-level title here, and you cannot use a ##. You don't need to write a serial number, it will automatically generate a serial number.)
                                 ( Skip a line )
text
                                 (at least one line)
### Three-level title            (similar to the second-level title, it does not need to be written, it will be generated automatically)

text

## Secondary title 2

text


```

### Link

Due to the large number of pages and the need to link resources such as images, relative paths are used when writing links.
The directory structure is as follows:
```
assets/                                     (put public resource files)
       |
       ----pic000.png
en/
    |
    ----- get_started/
                   |
                   ---- assets/            (put the resource file common to the md file in the get_started directory)
                              |
                              ------ pic.png
                   |
                   ---- get_hardware.md
zh/
```

If you want to show the images in `get_hardware.md`, put the image in the `assets` folder, then use the following code to reference the image:
```
![pic](assets/pic.png)
![pic](../../assets/pic000.png)
```

### Chinese and English mixed

When writing Chinese documents, the Chinese characters should be separated by spaces as much as possible. Punctuation should use full-width symbols as much as possible.
Mainly to make it stand out and make the document more elegant.
For example, the following comparison:

---------

```markdown
The `setup` function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc.
```
The `setup` function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc.

----------

```markdown
The setup function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc.
```
The setup function is called when a sketch starts. Use it to initialize variables, pin modes, start using libraries, etc.

---------

## Directory and file name

* The generated document directory is edited in the corresponding language folder `SUMMARY.md`

* The source document folder should be a function module corresponding to a folder, and the resource file (picture) is placed in the `assets` folder directory of the current path of the corresponding md document, which is more convenient when adding, deleting, and modifying.

```
assets/                                 (put public resource files)
en/
   |
   ----- get_started/
                  |
                  ---- assets/          (put the resource file common to the md file in the get_started directory)
                  |
                  ---- get_hardware.md
zh/
```

* The file name is not limited to `README.md`, other file names are named with lowercase + underscore, such as `get_hardware.md`


## Catalog and links

Try to guide readers to use the directory, and use the jump link in the text with caution. If the link jumps in a mess, it will cause the document to look messy and it will be difficult to read.


## Chinese and English (multi-language) page file directory structure and file name are the same

Since there are multiple language switching options in the last generated page, clicking the switch will directly access the same path of the corresponding language, so the Chinese and English directory structure and file name must be the same.

For example, English is accessing `en/get_started/blink.md`. After clicking the button for language switching, it will automatically access `zh/get_started/blink.md`. If this file does not exist, it will report a `404` error!



## Module Document Content

* Need to include a module introduction in the file header
* Need to explain the constructor, function, constant, etc.
* **Explain that you can't be lazy. Simply translate the function name again. You need to explain the function of the function, the range of parameters, and the point of attention**


## Multi-version management

In addition to the Chinese and English (multi-language) support (not automatic translation, manual modification), the document also has multi-version management.

Each version is a branch with requirements for the branch name, which are:

* `master` branch is the main branch
* `dev` branch for development branch
* Other published historical versions start with a lowercase `v`, such as creating a branch called `v1.2`

After creating a new branch, you need to modify the version link in `book.json` in the directory of each language version, otherwise the reader can't find the entry.

You can preview it locally under the newly created branch (see the root directory `README.md` for the preview method). Note that the previewed page is the current branch. If you want to preview other branches locally, you need to switch to other points before previewing. Just fine.

After confirming that the error is modified, push the branch to the remote (github), the automatic build system will be automatically built and published to the pages branch, and the effect will be seen when the access URL is built.
