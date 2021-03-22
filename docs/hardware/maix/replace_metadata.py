import os, sys
from glob import glob
import re

path = sys.argv[1]

file_dirs = glob(os.path.join(path, "**"), recursive=True)
for path in file_dirs:
    if os.path.isdir(path):
        continue
    if not path.endswith(".md"):
        continue
    print("deal:", path)
    with open(path, encoding="utf-8") as f:
        content = f.read()
        title = ""
        def re_replace_sharp_h1(c):
            global title
            title = c[0][2:-1]
            return ""
        def re_replace_h1(c):
            global title
            title = c[0].split("\n")[0]
            return ""
        # find title from:
        #                title
        #                ===
        content = re.sub(r'.*\n===.*\n', re_replace_h1, content, flags=re.MULTILINE)
        if not title:
            # find tile from:
            #                 # title
            content = re.sub(r'^# .*\n', re_replace_sharp_h1, content)
        header = '''---
title: {}
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: {}
---

'''.format(title, title)
        content = header + content
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)



