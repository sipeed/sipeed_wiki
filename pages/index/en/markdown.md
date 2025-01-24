---
title: Markdown syntax
---

## Introduction to Markdown

`Markdown` is a lightweight markup language that uses very simple characters to control formatting and typesetting. It does not require the effort of using the mouse to typeset like a rich text editor like Word, and the document is in plain text format, making it easy to modify. and version management.

This article mainly introduces how to understand and learn `Markdown` syntax.

## Markdown composition

Markdown generally consists of a **plain text content** and a **renderer**. Plain text is a document written according to `Markdown` syntax. The renderer converts the plain text content into an easy-to-read format such as HTML. tool.

`Markdown` is generally used in two places:
1. Website: When filling in content on a website, if it supports `Markdown` syntax, you can directly use `Markdown` syntax to edit the content. Generally, the preview function will be automatically rendered.
2. Offline tools, such as `Typora`, `VS Code`, etc. These tools generally have preview functions and can render in real time.

The `Markdown` syntax uses special symbols to control the format, such as `#` for the title, `[Text displayed in the link](https://***)` for the link, etc.

## Simple example

Text file `test.md`:

```markdown
# About how to learn Markdown syntax

## What is Markdown

Markdown generally consists of a **plain text content** and a **renderer**. Plain text is a document written according to `Markdown` syntax. The renderer converts the plain text content into an easy-to-read format such as HTML. tool.

## Markdown Reference

1. [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. [Markdown basic syntax](https://markdown.com.cn/basic-syntax/)

```

## Learn Markdown syntax reference

Please refer to the following website for details. The basic and important syntax is briefly listed below:

1. [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. [Markdown basic syntax](https://markdown.com.cn/basic-syntax/)

### Title

Note that there is a space after `#`, and in order to be compatible with more renderers, try to add a blank line after a line of title.

```markdown
#Level 1 title

## Second level title

### Third level title
```

### Paragraph

Separate paragraphs with blank lines

```markdown
This is the first paragraph.

This is the second paragraph.
```

### Font

```markdown
*italics*
**bold**
~~strikethrough~~
```

Effect:

*italics*
**bold**
~~strikethrough~~

### List

```markdown
1. Ordered list, note 1. There is a space after it
2. Ordered list

- Unordered list, note - there is a space after it
- unordered list

*Unordered list, note that there is a space after *
* Unordered list
```

Effect:

1. Ordered list, note 1. There is a space after it
2. Ordered list

- Unordered list, note - there is a space after it
- unordered list

*Unordered list, note that there is a space after *
* Unordered list


### Quote paragraph

```markdown
> Quoted paragraphs can also be used as comments. Note that there is a space after >
```

>The effect is like this

### Code

```markdown
`One line of code`
```
Effect: `Single line of code`

multiple lines of code
```
​```python
print("hello")
​```
```

Effect:
```python
def hello():
     print("hello")

hello()
```

### Link

```markdown
[The text displayed in the link, click on me to transfer to MaixHub](https://maixhub.com)
```

[The text displayed in the link, click on me to transfer to MaixHub](https://maixhub.com)


### picture

```markdown
![Text displayed in the image](/static/image/sipeed_logo.png)
![Text displayed in the image](/static/image/sipeed_logo_4.svg)
```

Effect:
![Text displayed in the image](/static/image/sipeed_logo.png)
![Text displayed in the image](/static/image/sipeed_logo_4.svg)

### sheet

```markdown
| Header 1 | Header 2 |
| ----- | ----- |
| Content 1 | Content 2 |
```

Effect:

| Header 1 | Header 2 |
| ----- | ----- |
| Content 1 | Content 2 |

### other

See the references above for more syntax.

