---
title: 写文档的注意点
keywords: teedoc, 写文档, 注意点
desc: teedoc， 将 markdown 或者 jupyter notbook 转换成 html 静态网页， 介绍了使用 teedoc 写文档时的注意点
---


## 相对路径问题

在`config.json`中写链接路径时，尽量写规范，比如`/get_started/zh/`， 而不是`/get_started/zh`

即如果对应的路径不是文件，而是一个目录， 则必须在后面加一个`/`，让浏览器知道这是一个目录，
这样我们在`md`文件中写相对路径比如`../assets/image/screenshot.png`就会转换为`/get_started/assets/image/screenshot.png`
如果是`/get_started/zh`， 浏览器就会解析为`/assets/image/screenshot.png`，就是错误的地址，就会找不到图片！

当然，你也可以选择使用绝对路径







