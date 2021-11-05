文档规范
=======

文档使用 gitbook 进行构建， 并使用简单高效的 Markdown 编写内容

文档源码托管在 [GitHub](https://github.com/sipeed/Maixduino_DOC)

## Markdown 语法

Markdown 的基础语法如果没接触过， 请花半个小时进行学习， 推荐github的教程： [github Markdown 教程](https://guides.github.com/features/mastering-markdown/)

在本文中， 以下几点我们需要注意：

### 标题类的语法标记必须使用空格隔开，大标题与正文之间需要一个空行，比如：

```markdown
## 这是二级标题

* 这是列表项1
* 这是列表项2

```
而如下所示的则不是正确的，可能会导致解析器出现解析错误格式错乱等

```markdown
##这是二级标题
*这是列表项1
*这是列表项2
```

### 所有页面只有一个一级标题

由于需要自动生成目录，主要是为了保证自动生成的目录正确。
每个页面这样写
```
页面标题/一级标题
=======         (这里等号至少需要三个)
                ( 至少需要一个以上的空行，建议2行 )

## 二级标题1     ( 这里不能使用一级标题，及不能用一个#号。 也不需要写序号，会自动生成序号)
                ( 空一行 )
正文
                ( 至少空一行)
### 三级标题      ( 类似二级标题, 也不需要写需要，会自动生成)

正文

## 二级标题2

正文


```

### 链接

由于页面众多，而且需要链接图片等资源，在写链接时，均使用相对路径，
比如目录结构如下
```
assets/                                 (放公用的资源文件)
      |
      ----pic000.png
en/
   |
   ----- get_started/
                  |
                  ---- assets/          (放get_started目录下md文件公用的资源文件)
                             |
                             ------ pic.png
                  |
                  ---- get_hardware.md
                  |
                  ---- how_to_read.md
zh/
```

如果在`get_hardware.md`中贴图片，将图片放进`assets`文件夹后，使用如下代码引用图片
```
![pic](assets/pic.png)
![pic](../../assets/pic000.png)
```


### 中英文混写

在写中文文档时，在中文中夹杂英文尽量用空格隔开，标点符号尽量使用全角符号，
主要是为了显眼，让文档更优雅。
比如如下对比：

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

## 目录和文件名

* 生成的文档目录在对应语言的文件夹`SUMMARY.md`中编辑

* 源文档的文件夹尽量一个功能模块对应一个文件夹，资源文件（图片）放置到对应 md 文档的当前路径的 `assets`文件夹目录下，这样在增删修改时更方便

```
assets/                                 (放公用的资源文件)
en/
   |
   ----- get_started/
                  |
                  ---- assets/          (放get_started目录下md文件公用的资源文件)
                  |
                  ---- get_hardware.md
zh/
```

* 文件名除了`README.md`特殊，其它文件名使用 小写+下划线 的命名方式，比如 `get_hardware.md`



## 中英文（多语言）的页面文件目录结构和文件名相同

由于最后生成的页面中有多语言切换选项，点击切换后会直接访问对应语言的相同路径，所以中英文的目录结构和文件名必须相同。

比如英文正在访问`en/get_started/how_to_read.md`， 点击语言切换的按钮后，会自动访问`zh/get_started/how_to_read.md`， 如果这个文件不存在就会报`404`错误！


## 目录和链接

尽量引导阅读者使用目录，文内跳转链接慎用，如果链接跳得比较乱，会导致文档看起来比较乱，阅读会比较困难。

## 模块文档内容

* 需要在文件头部包含模块的介绍
* 需要分点说明构造函数、函数、常量等
* **说明不能偷懒只简单将函数名称翻译一遍，需要详细说明函数的功能、参数的取值范围以及注意点**

## 多版本管理

文档除了做了中英文（多语言）支持（不是自动翻译，需要手动修改）， 也做了多版本管理。

每个版本是一个分支， 对分支名字有要求， 分别为： 
* `master` 分支为主分支
* `dev`分支为开发分支
* 其它的发布的历史版本均以小写 `v` 开头，比如创建一个分支叫 `v1.2`

创建好新的分支后，需要在每个语言版本的目录下 `book.json`中修改版本链接，不然读者找不到入口

可以在新建的分支下本地预览（预览方法见根目录 `README.md`）， 注意这时候预览的页面就是当前分支的内容，如果要本地预览其它分支内容，需要先切换到其它分之后再预览即可。

确认无误修改完成后推送分支到远程（github）， 自动构建系统会自动构建并发布到 pages 分支， 等构建完毕访问网址即可看到效果。
