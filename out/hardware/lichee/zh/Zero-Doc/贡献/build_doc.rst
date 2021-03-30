文档构建
====================================

.. contents:: 本文目录

前言
------------------------------------

本文档选择使用Sphinx来进行构建，支持以 :guilabel:`reStructuredText` 和 :guilabel:`Markdown` 格式编写

本地构建
------------------------------------

1. 拉取文档
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开终端，运行以下命令:

   ``git clone https://github.com/Lichee-Pi/lichee-pi-zero.git``

2. 安装依赖
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 首先我们需要通过pip安装Sphinx
   
   ``pip install Sphinx``
   
   若您没有安装pip，请参照 `pip 安装 <http://pip.readthedocs.io/en/stable/installing/>`_

- 接着安装本文档的模块依赖

   ``pip install sphinx_rtd_theme``    用于支持文档主题

   ``pip install recommonmark``        用于支持Markdown文本格式

3. 构建
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd Lichee-Zero-Doc-zh-CN
   
   # windows
   .\make.bat html

   # linux
   make html

构建完成，进入 :menuselection:`build --> html --> index.html` 

打开以浏览器浏览即可。

技术文档贡献
------------------------------------

若您有意向贡献您的实践经验，请参照 `todolist <todolist.html>`_

以reStructuredText编写文档
------------------------------------

.rst 文件是轻量级标记语言的一种，被设计为容易阅读和编写的纯文本，并且可以借助Docutils这样的程序进行文档处理，也可以转换为HTML或PDF等多种格式，或由Sphinx-Doc这样的程序转换为LaTex、man等更多格式。

在本文档中， *.rst* 文件配合sphinx工具以及readthedoc主题，具有较为丰富的文本表现。

此外，与Markdown对比来看：

    1. RST更适合于构建完整较大的文档，Markdown更适用于构建单页应用
    2. RST格式更为丰富，Markdown更为简洁
    3. RST格式要求稍高于Markdown

reStructuredText语法请参考 `quick reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html#doctest-blocks>`_

个人建议您也可以通过查看 `Read the Docs主题示例 <https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/demo.html#id27>`_ ，配合其 `github <https://github.com/rtfd/sphinx_rtd_theme/edit/master/docs/demo/demo.rst>`_ 的编辑源码模式，可更直观地进行对照、借鉴。

- 另： RST的表格对于中文支持不好，个人推荐借助 `pytablewriter <http://pytablewriter.rtfd.io>`_ 来生成中文表格

.. code-block:: python
   :caption: 以下是使用示例：
  
   # coding: utf-8
   import pytablewriter

   writer = pytablewriter.RstGridTableWriter()

   writer.table_name = "example_table"
   writer.header_list = ['水果', '价格', '数量']
   writer.value_matrix = [
      ['香蕉', '1', '5'],
  	  ['苹果', '1', '6'],
  	  ['草莓', '1', '7'],
   ]
  
   writer.write_table()

    

.. sidebar:: 渲染为：

    .. table:: 

        +----+----+----+
        |水果|价格|数量|
        +====+====+====+
        |香蕉|   1|   5|
        +----+----+----+
        |苹果|   1|   6|
        +----+----+----+
        |草莓|   1|   7|
        +----+----+----+

.. code-block:: rst
      :caption: 转换结果：
      :linenos:

      .. table:: 


        +----+----+----+
        |水果|价格|数量|
        +====+====+====+
        |香蕉|   1|   5|
        +----+----+----+
        |苹果|   1|   6|
        +----+----+----+
        |草莓|   1|   7|
        +----+----+----+

以Markdown编写文档
------------------------------------

Markdown语句较为简明，互联网上也有大量的辅助工具与教程；

个人推荐您使用 vscode配合插件Markdown All in One，或使用 `typora <https://www.typora.io/>`_ ，笔者使用体验较为舒适

.. admonition:: 一点小提醒

    若您单纯使用Markdown书写，无需注意以下所有内容；

    若您 **想用Markdown而不涉及rst及其语法** 构建您的 **个人文档** 时，建议您使用 `Mkdocs <http://www.mkdocs.org/>`_ 替代sphinx，参阅 `readthedocs build process <http://docs.readthedocs.io/en/latest/builds.html#mkdocs>`_ ；

    若您将Markdown文件加入sphinx的构建行列，请注意以下两条：

    - 要使用sphinx所提供的特性时，如：

        .. Tip:: 15% if the service is good.

        .. Error:: Does not compute.

        请将其标为代码片段，代码类型为： **eval_rst**，sphinx将会将此片段作为rst文本进行解析：

        .. code-block:: markdown

            ```eval_rst

                .. Tip:: 15% if the service is good.

                .. Error:: Does not compute.

            ```
        
    - sphinx对Markdown的表格支持不够完全，请使用上一条所用方法，以rst语法来绘制表格



