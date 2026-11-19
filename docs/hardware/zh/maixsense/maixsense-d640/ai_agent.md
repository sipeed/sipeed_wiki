---
title: Agent 使用指南
keywords: MaixSense, D640, AI Agent, skill, 采集, 深度, 红外
update_open: false
update:
  - date: 2026-11-04
    version: v0.1
    author: lxowalle
    content: 初版
---

使用 AI Agent 操作 MaixSense D640，可以通过对话完成深度图和左右红外图采集、保存数据、检查采集结果。例如，要求 Agent“采集一张深度图并告诉我有效深度像素数”，或“保存一张左红外图并告诉我文件位置”。

## 准备 Agent 环境

1. 选择一个 Agent，常见的有 [Codex](https://openai.com/codex/)、[Claude Code](https://code.claude.com/docs/en/overview)、[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)等, 按官方说明完成安装、登录或模型配置, 确保让它能够读取下载的文件并执行本地命令。
2. 用 USB 数据线连接设备
3. 下载 [MaixSense D640 SKILL](https://cdn.sipeed.com/maixsense/d640/latest/maixsense_d640_skill.zip)。将压缩包或文件路径发给 Agent，让它解压并读取包内的 `SKILL.md`：

```text
请解压这个 SKILL 包并读取 SKILL.md，检查运行环境，
缺少 Python 时按当前系统完成安装，并查询已连接设备的序列号。
准备完成后，告诉我识别到的设备和可以执行的采集操作。
```

Python 和图像编码依赖的检查、安装，以及设备身份查询由 SKILL 引导 Agent 完成。系统需要授权或无法自动读取序列号时，Agent 会说明需要你补充的操作或信息。

## SKILL 放在哪里

当前主流模型通常可以按指定路径读取并理解 SKILL。临时使用时，大多数情况无需安装到指定位置，只需让 Agent 读取解压目录里的 `SKILL.md`，并保留同目录下的 `scripts` 文件夹。例如：

```text
请读取【SKILL 文件夹的完整路径】中的 SKILL.md，
按其中的说明操作已连接的 MaixSense D640。
```

Agent 需要能够访问该路径并执行命令。指定路径供当前对话使用，不等于已安装为所有项目自动加载的 SKILL。

希望长期使用、让 Agent 自动发现时，可把完整的 `maixsense-d640-capture` 文件夹放入下表目录：

| Agent | 只在当前项目使用 | 在当前用户的所有项目使用 |
| :--- | :--- | :--- |
| Codex | `<项目目录>/.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `<项目目录>/.claude/skills/` | `~/.claude/skills/` |
| DSH | `<项目目录>/.dsh/skills/` | `~/.dsh/skills/` |

例如 Codex 的项目目录下应形成 `.agents/skills/maixsense-d640-capture/SKILL.md`，旁边保留 `scripts/capture.py`。不要多套一层同名文件夹，也不要只复制 `SKILL.md`。

Linux 和 macOS 中 `~` 表示用户主目录。Windows 中对应 `%USERPROFILE%`，例如 Codex 用户目录为 `%USERPROFILE%\.agents\skills\`。使用 WSL 时，路径应位于 Agent 实际运行的 WSL 环境中。

以上是默认的本地目录，自定义配置以各工具说明为准：[Codex](https://learn.chatgpt.com/docs/build-skills)、[Claude Code](https://code.claude.com/docs/en/skills)、[DSH](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md)。

## 采集深度图

提示词:
```text
请使用刚才的 SKILL，从已连接的 MaixSense D640 接收 10 帧深度数据，
将最后一帧保存到一个新文件夹。
检查采集结果，告诉我文件路径、图像尺寸和有效深度像素数。
```

这次操作接收 10 帧，只保存最后一帧，不会录制视频。Agent 会检查新生成的文件，并报告采集是否成功。

## 采集红外图

提示词:
```text
请使用同一台 MaixSense D640 采集左红外图，接收 10 帧，
保存最后一帧到新的文件夹，并告诉我文件路径和图像尺寸。
```

需要右红外时，将请求中的“左红外”改为“右红外”。默认每次只采一路，分开执行的结果不属于同步三路数据。

## 查看采集结果

| 文件 | 用途 |
| :--- | :--- |
| `result.json` | 采集结果，包括设备身份、图像尺寸和文件名 |
| `depth_数字.pgm` | 深度数据，像素值表示毫米距离，0 表示无效值 |
| `left_ir_数字.jpg`、`right_ir_数字.jpg` | 分别采集的左右红外灰度图 |

左右红外默认保存为 JPG，可直接用常见看图软件打开。深度保留为 16 位 PGM，用于保存毫米深度值。


## 下一步

- 实时看图、测距和保存数据：[上位机软件指南](./gui.md)。
- 编写自己的采集程序：[SDK 开发指南](./sdk.md)。
- 接入机器人程序：[ROS2 使用指南](./ros2.md)。
