---
title: teedoc 其它插件
keywords: teedoc, 主题插件, 主题, 插件
desc: teedoc 其它插件
---

## `teedoc-plugin-markdown-parser`: 默认 markdown 解析插件

在`site_config.json`中配置插件
```json
    "plugins": {
        "teedoc-plugin-markdown-parser":{
            "from": "pypi",
            "config": {
                "link_abs_path": true
            }
        },
    }
```

* `link_abs_path`: 将链接转换为绝对路径

