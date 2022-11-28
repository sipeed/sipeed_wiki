---
title: M1s DOCK 常见问题
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-28
    version: v0.1
    author: wonder
    content:
      - 初次编辑
---

## c906_app/build_out/xxxxx/.map:No such file or dictionary

注意编译的时候使用的命令为 `./build.sh demo_name`，比如  `./build.sh hello_world`，而不是 `./build.sh hello_world/` （注意最后面的路径符号`/`）

