---
title: Points to note when writing documents
keywords: teedoc, document writing, points to note
desc: teedoc, which converts markdown or jupyter notbook into html static web pages, introduces the points to note when writing documents with teedoc
---


## Relative path problem

When writing the link path in `config.json`, try to write the specification, such as `/get_started/zh/` instead of `/get_started/zh`

That is, if the corresponding path is not a file, but a directory, you must add a `/` at the end to let the browser know that this is a directory,
In this way, we write relative paths in the `md` file, such as `../assets/image/screenshot.png`, which will be converted to `/get_started/assets/image/screenshot.png`
If it is `/get_started/zh`, the browser will parse it as `/assets/image/screenshot.png`, which is the wrong address, and the picture will not be found!

Of course, you can also choose to use an absolute path
