---
title: 开始写文档
keywords: teedoc, markdown, jupyter notebook, html, 文档生成, 替代gitbook, 网站生成, 静态网站, 写文档
desc: teedoc， 将 markdown 或者 jupyter notbook 转换成 html 静态网页， 介绍了 teedoc 的基本使用
---


## 文档架构

```
├─.github
├─docs
│  ├─develop
│  │  ├─en
│  │  └─zh
│  └─get_started
│      ├─assets
│      ├─en
│      └─zh
├─pages
│  └─index
│      ├─en
│      └─zh
├─static
│
└─site_config.json
```

* `.github`: 自动构建脚本，在后面的章节将如何使用
* `docs`: 文档，包含了多份文档， 每份文档都是单独一个文件夹
* `pages`: 页面，包括主页、404页面等等页面
* `static`: 静态文件文件夹，比如存放图片
* `site_config.json`: 网站配置文件
* `config.json`: 除了`site_config.json`外，每个文档目录下都可以有`config.json`用来配置文档相关页面
* `sidebar.json`: 文档目录

## site_config.json 网站配置

网站的配置项，比如网站名称，页面路由，插件配置等等

比如：

```json
{
    "site_name": "teedoc",
    "site_slogon": "happy to write",
    "route": {
        "docs": {
            "/get_started/zh": "docs/get_started/zh",
            "/get_started/en": "docs/get_started/en",
            "/develop/zh": "docs/develop/zh",
            "/develop/en": "docs/develop/en"
        },
        "pages": {
            "/": "pages/index/zh",
            "/en": "pages/index/en"
        },
        "assets": {
            "/static": "static",
            "/get_started/assets": "docs/get_started/assets"
        },
        "/blog": "blog"
    },
    "executable": {
        "python": "python3",
        "pip": "pip3"
    },
    "plugins": {
        "teedoc-plugin-markdown-parser":{
            "from": "pypi",
            "config": {
            }
        },
        "teedoc-plugin-theme-default":{
            "from": "pypi",
            "config": {
                "dark": true,
                "env":{
                    "main_color": "#4caf7d"
                },
                "css": "/static/css/custom.css",
                "js": "/static/js/custom.js"
            }
        }
    }
}

```

* `site_name`: 网站名
* `site_slogon`: 网站标语
* `route`: 网页路由，包含了文档和页面以及资源文件的路由，比如文档的路由
```json
"docs": {
    "/get_started/zh": "docs/get_started/zh",
    "/get_started/en": "docs/get_started/en",
    "/develop/zh": "docs/develop/zh",
    "/develop/en": "docs/develop/en"
},
```
`key`代表了最终生成的网站中文档的`url`, 后面的值则是对应的源文档路径，
比如源文档`docs/get_started/zh/README.md`，构建后会生成文件`out/get_started/zh/index.html`, 如果不是`md`文件（即不支持的文件），则会原封不动地拷贝文件，最后`out`目录就是生成的网站

`pages`、`assets`同理

* `executable`: 可执行程序设置， 这里可以设置`python`和`pip`的可执行程序名，在安装插件时会用到
* `plugins`: 插件配置， 主要有名字， 来源， 配置项组成。
名字可以在[github](https://github.com) 搜索`teedoc-plugin`来找到开源的插件，也欢迎你参与编写插件（只需要动 `Python` 语法即可）； 
`from`字段填`pypi`即可，如果插件下载到了本地也可以填写文件夹路径，也可以直接填`git`路径比如`git+https://github.com/*****/******.git`
配置项则由具体的插件决定，比如`teedoc-plugin-theme-default`就有`dark`选项来选择是否启用暗黑主题
* `rebuild_changes_delay`: 检测到文件更改后，延迟多少秒自动重新生成该文档



