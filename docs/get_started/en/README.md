---
title: teedoc
keywords: teedoc, markdown, jupyter notebook, html, document generation, alternative gitbook, website generation, static website
desc: teedoc, convert markdown or jupyter notbook into html static webpage
---


Official website: [teedoc.github.io](https://teedoc.github.io/)
Source file of this document: [github.com/teedoc/teedoc.github.io](https://github.com/teedoc/teedoc.github.io)
Source code: [https://github.com/teedoc/teedoc](https://github.com/teedoc/teedoc) Welcome star

Convert documents in `Markdown` or `Jupyter Notebook` format to `HTML` web pages

`teedoc` can be used in the following scenarios:
* Build a document website, and preferably support multiple documents and custom pages
* Build a `WiKi` website
* Build personal or corporate knowledge base
* Build personal or corporate website




## Features

- [x] Simple to use, cross-platform, only dependent on `Python3`
- [x] The deployment is simple, the generated website is a fully static page, which can be deployed directly by copying to the server or uploading to a third party organization
- [x] Easy to write, using Markdown syntax
- [ ] Jupyter notebook support
- [x] Multi-document support
- [x] Plug-in support
- [x] Multi-theme support (implemented by plugin)
- [x] Control the style accurate to the page through css (implemented by customizing the id and class of each page)
- [x] Multi-level directory support
- [x] Multi-language support (manual translation) (Internationalization/i18n)
- [ ] Multilingual support (automatic translation)
- [x] Multi-version support (implementation method is the same as multi-language)
- [x] Search support
- [x] SEO friendly
- [x] Real-time preview of changes
- [x] Multi-threaded construction, faster construction speed
- [ ] Blog support


## Similar tools

In fact, there are already many tools of this type. Just choose one according to your needs.

* docusaurus: The UI layout of teedoc is almost similar to it, but it uses vue to write, teedoc is native js, if you are using vue, you can consider this
* gitbook: a tool that used to be very useful, but it is no longer maintained by the official website
* docsify: Only one page is needed. Markdown is rendered in the browser instead of pre-rendered into HTML. The advantage is that it is lightweight, but SEO is not friendly. You can use its SSR function, written in nodejs
* readthedocs: A tool used by many open source projects. It also has a website service like gitbook. You can start writing documents after registering and logging in. You can also download the software to generate the website yourself, which is friendly to RST format support

If you have choice difficulties, you are recommended to use teedoc if you meet some of the following conditions:
* Does the function meet your needs?
* Does the interface meet your aesthetics (you can customize css, or change the theme plug-in)
* Familiar with Python? You can customize the plugin at any time


## Some usage suggestions

* Add `Generate with teedoc` in footer to help more people discover teedoc and promote project growth
* Use the template project to start a new document project, you can run it first, and then modify it according to your own needs, so that you can get started faster
