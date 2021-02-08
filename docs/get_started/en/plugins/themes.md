---
title: teedoc theme plugin
keywords: teedoc, theme plugin, themes, plugin
desc: teedoc theme plugin
---


## `teedoc-plugin-theme-default`: default theme plugin

Configure the plugin in `site_config.json`
```json
    "plugins": {
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
```

* `main_color`: theme main color
* `css`: `css` file, which can override the default style, will be inserted into the `head` tag of the page
* `js`: `js` file, you can write `js` program, it will be loaded at the end of the page

Supports `day` and `night` modes. The night mode will add a `dark` class to the `body`. If you want the `css` style of the night mode, you can modify it based on this class name
