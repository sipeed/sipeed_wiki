---
title: teedoc plugin
keywords: teedoc, plugin
desc: teedoc, convert markdown or jupyter notbook into html static web pages, introduce teedoc plug-ins
---


## Plug-in introduction

teedoc uses a plug-in system to facilitate expansion


In the `site_config.json` file, set the `plugins` field, such as
```json
{
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

Two plugins are installed by default here, namely `teedoc-plugin-markdown-parser` and `teedoc-plugin-theme-default`, both of which are installed directly from `pypi.org`. The theme plugin has configuration items

The configuration items include whether to use the `dark` theme, as well as the environment variable `env` of the plug-in, and set the `main_color` to `#4caf7d`. This value will be used in the plug-in. Set the theme color to the corresponding color;

As well as setting custom `css` files and `js` files, the value is `url`, not the file path (for the mapping of file path and `url` please see the introduction of `route` (route), by setting this `css` File, you can override the default style of the theme plug-in to achieve simple custom functions


* [Theme Plugin](./themes.md)
* [Other plug-ins](./others.md)
