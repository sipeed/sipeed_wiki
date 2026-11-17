import os

from teedoc import Plugin_Base


__version__ = "1.0.0"


class Plugin(Plugin_Base):
    name = "teedoc-plugin-search-lazy-load"
    desc = "load teedoc search indexes only when the search dialog is opened"

    def on_copy_files(self):
        # This plugin is loaded after teedoc-plugin-search and replaces its script.
        source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "search_main.js")
        return {
            "/static/js/search/search_main.js": source,
        }
