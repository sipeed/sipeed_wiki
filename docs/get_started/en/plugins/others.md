---
title: teedoc other plugins
keywords: teedoc, theme plugin, themes, plugin
desc: teedoc other plugins
---

## `teedoc-plugin-markdown-parser`: default markdown parsing plugin

Configure the plugin in `site_config.json`
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

* `toc_depth`: The depth of the article table of contents (right column), the default is `3`, which means to `h3` that is `### three-level heading` in `markdown`


## `teedoc-plugin-search`: Website search plugin

Let the website and documents support the search function, support the searched current document and the whole site search

To use, add to the `plugins` keyword in `site_config.json`:
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


The prompt content of different documents can be configured in the corresponding document `config.json` to facilitate multi-language support (internationalization/i18n)

The supported configurations are as follows:

```json
"teedoc-plugin-search":{
    "config": {
        "search_hint": "Search",
        "input_hint": "Enter keywords, separate multiple keywords with spaces",
        "loading_hint": "Loading, please wait...",
        "download_err_hint": "Failed to download the file, please refresh and try again or check the network",
        "other_docs_result_hint": "Results from other documents",
        "curr_doc_result_hint": "Current document search result"
    }
}
```

* `search_hint`: the prompt message of the search box (button), the default is `Search`
* `input_hint`: input hint information in the search box of the search page, default `Keywords separated by space`
* `loading_hint`: Load the file prompt for searching, the default is `Loading, wait please ...`
* `download_err_hint`: The download of the file required for the search fails, the user needs to refresh the browser to try again or the network environment cannot download the file, the default is `Download error, please check network and refresh again`
* `other_docs_result_hint`: search result hint, search result in other documents, default `Result from other docs`
* `curr_doc_result_hint`: search result hint, the search result in the currently browsed document, default `Result from current doc`


## Baidu Statistics

Add the code of [Baidu Statistics](https://tongji.baidu.com/) on each page, send the visit information to Baidu, and you can see the visit statistics in the background

After registering and logging in to Baidu Statistics, add a website on the management page, and then there will be a code acquisition page with the following code
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

Here is a string of keys `90c693aa2************c14a50bb49`, copy this string of keys, and then add to the `plugins` keyword in `site_config.json`:
```json
"plugins": {
    "teedoc-plugin-baidu-tongji":{
        "from": "pypi",
        "config": {
            "code": "Fill in the access key here"
        }
    }
}
```

After the website is deployed, you can see the visit information on the real-time visitor page of the Baidu statistics background
