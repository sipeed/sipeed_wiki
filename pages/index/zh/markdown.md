---
title: Markdown 语法
---

**【[English Version](../en/markdown.md)】**

## Markdown 简介

`Markdown` 是一种轻量级的标记语言，即用非常简单的字符来控制格式和排版，不用像类似 Word 的富文本编辑器一样费力使用鼠标来排版，并且文档是纯文本格式，方便修改和版本管理。

本文主要介绍如何了解和学习 `Markdown` 语法。

## Markdown 组成

Markdown 一般由一份**纯文本内容**和一个**渲染器**组成，纯文本就是按照 `Markdown`语法编写的文档，渲染器就是将纯文本内容转换为 HTML 等方便阅读的格式的工具。

一般在两种地方使用 `Markdown`:
1. 网站: 在网站填写内容时，如果支持 `Markdown`语法，可以直接使用 `Markdown` 语法来编辑内容，一般会有预览功能自动渲染。
2. 离线工具，如 `Typora`，`VS Code` 等，这些工具一般都有预览功能，可以实时渲染。

`Markdown`语法就是用特殊的符号来控制格式，比如 `#` 表示标题，`[连接显示的文字](https://***)` 表示链接等。

## 简单例子

文本文件`test.md`：

```markdown
# 关于如何学习 Markdown 语法

## 什么是 Markdown

Markdown 一般由一份**纯文本内容**和一个**渲染器**组成，纯文本就是按照 `Markdown`语法编写的文档，渲染器就是将纯文本内容转换为 HTML 等方便阅读的格式的工具。

## Markdown 参考资料

1. [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. [Markdown 基本语法](https://markdown.com.cn/basic-syntax/)

```

## 学习 Markdown 语法参考

详细的参考以下网站，下面会简要列出基础和重要的语法：

1. [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
2. [Markdown 基本语法](https://markdown.com.cn/basic-syntax/)

### 标题

注意 `#` 后面有一个空格，而且为了兼容更多渲染器，尽量在一行标题后面加一个空行。

```markdown
# 一级标题

## 二级标题

### 三级标题
```

### 段落

段落之间用空行分隔

```markdown
这是第一段。

这是第二段。
```

### 字体

```markdown
*斜体*
**粗体**
~~删除线~~
```

效果：

*斜体*
**粗体**
~~删除线~~

### 列表

```markdown
1. 有序列表，注意 1. 后面有一个空格
2. 有序列表

- 无序列表，注意 - 后面有一个空格
- 无序列表

* 无序列表，注意 * 后面有一个空格
* 无序列表
```

效果：

1. 有序列表，注意 1. 后面有一个空格
2. 有序列表

- 无序列表，注意 - 后面有一个空格
- 无序列表

* 无序列表，注意 * 后面有一个空格
* 无序列表


### 引用段落

```markdown
> 引用段落，也可以拿来做注释用，注意 > 后面有一个空格
```

> 效果就是这样

### 代码

```markdown
`单行代码`
```
效果：`单行代码`

多行代码
```
​```python
print("hello")
​```
```

效果：
```python
def hello():
    print("hello")

hello()
```

### 链接

```markdown
[连接显示的文字，点击我调转到 MaixHub](https://maixhub.com)
```

[连接显示的文字，点击我调转到 MaixHub](https://maixhub.com)


### 图片

```markdown
![图片显示的文字](/static/image/sipeed_logo.png)
![图片显示的文字](/static/image/sipeed_logo_4.svg)
```

效果：
![图片显示的文字](/static/image/sipeed_logo.png)
![图片显示的文字](/static/image/sipeed_logo_4.svg)

### 表格

```markdown
| 表头1 | 表头2 |
| ----- | ----- |
| 内容1 | 内容2 |
```

效果：

| 表头1 | 表头2 |
| ----- | ----- |
| 内容1 | 内容2 |

### 其他

更多语法参考上面的参考资料。

