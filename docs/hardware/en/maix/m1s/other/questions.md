---
title: M1s DOCK Questions
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-12-03
    version: v0.1
    author: wonder
    content:
      - Create file
---

## c906_app/build_out/xxxxx/.map:No such file or dictionary

When compiling your firmware, make sure your command is `./build.sh demo_name`, like  `./build.sh hello_world`, not `./build.sh hello_world/` (pay atention to the end symbol `/`)

