---
title: SEO (optimized for search engines)
keywords: teedoc, SEO, search optimization, search engine indexing
desc: How to use teedoc to do SEO (speed up search engines to include websites and pages)
---

`SEO`: `Search Engine Optimization`, which is search engine optimization. In order to make your website indexed by search engines so that users can search our website through search engines, we need to do some things:


## Page keywords and description

Add keywords and descriptions to each page, such as `.md` file header (source text on this page)
```markdown
---
title: SEO (optimized for search engines)
keywords: teedoc, SEO, search optimization, search engine indexing
desc: How to use teedoc to do SEO (speed up search engines to include websites and pages)
---

```

This will automatically add a title to the article, and add keywords and descriptions to the `HTML` file for search engines to fetch

In addition, since the page will generate a first-level title based on this title, it is best not to use the first-level title for the article, and use the second-level title directly, such as:

```markdown
---
title: SEO (optimized for search engines)
keywords: teedoc, SEO, search optimization, search engine indexing
desc: How to use teedoc to do SEO (speed up search engines to include websites and pages)
---

## Introduction

Here is the introduction

## Directory Two

```

## Sitemap

A site map will be generated to `/sitemap.xml`, and a robot crawling rule to `/robots.txt`. You can submit the `url` of this `sitemap` in the webmaster background of the search engine, so Search engines will come to grab information

You can set the `robots` key value in the `site_config.json` to prevent crawlers from crawling certain files or content. For the format, please refer to the description of the `robots` key value in [Instructions for use](./start.md)



## End of page record information

In China, all websites need to be filed before they can be included by search engines. Add your website's file information in `config.json`. Note that the file information must be consistent with the domain name, otherwise it will be invalid
