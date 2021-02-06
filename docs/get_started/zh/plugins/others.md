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
                "toc_depth": 3
            }
        },
    }
```

* `toc_depth`: 文章目录（右边栏）的深度， 默认 `3`， 代表到`h3` 即 `markdown` 中的`### 三级标题`


## `teedoc-plugin-search`: 网站搜索插件

让网站和文档支持搜索功能，支持所搜当前文档和全站搜索

要使用，在`site_config.json`中的`plugins`关键词中添加：
```json
"plugins": {
    "teedoc-plugin-search":{
        "from": "pypi",
        "config": {
            "search_hint": "Search"
        }
    }
}
```


不同文档的提示内容可以在对应的文档`config.json`中配置，以方便做多语言支持（国际化/i18n）

支持的配置如下：

```json
"teedoc-plugin-search":{
    "config": {
        "search_hint": "搜索",
        "input_hint": "输入关键词，多关键词空格隔开",
        "loading_hint": "正在加载，请稍候。。。",
        "download_err_hint": "下载文件失败，请刷新重试或检查网络",
        "other_docs_result_hint": "来自其它文档的结果",
        "curr_doc_result_hint": "当前文档搜索结果"
    }
}
```

* `search_hint`: 搜索框（按钮）的提示信息， 默认`Search`
* `input_hint`: 搜索页面搜索框输入提示信息， 默认`Keywords separated by space`
* `loading_hint`: 加载搜索所需的文件提示，默认`Loading, wait please ...`
* `download_err_hint`: 下载搜索所需的文件失败提示，需要用户刷新浏览器重试或者网络环境无法下载文件， 默认`Download error, please check network and refresh again`
* `other_docs_result_hint`: 搜索结果提示，其它文档中的搜索结果， 默认`Result from other docs`
* `curr_doc_result_hint`: 搜索结果提示，当前浏览的文档中的搜索结果， 默认`Result from current doc`


## 百度统计

在每个页面添加[百度统计](https://tongji.baidu.com/)的代码，将访问信息发送到百度，就可以在后台看到访问统计信息了

在百度统计注册登录后，在管理页面添加网站，然后会有一个代码获取页面，里面会有如下的代码
```js
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?90c693aa2************c14a50bb49";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
```

这里有一串密钥`90c693aa2************c14a50bb49`，将这一串密钥复制，然后在`site_config.json`中的`plugins`关键词中添加：
```json
"plugins": {
    "teedoc-plugin-baidu-tongji":{
        "from": "pypi",
        "config": {
            "code": "这里填访问密钥"
        }
    }
}
```

部署好网站后，就可以在百度统计后台实时访客页面看到访问信息了




