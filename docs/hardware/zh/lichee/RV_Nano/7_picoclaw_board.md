---
title: LicheeRV Nano PicoClaw 扩展板
update:
  - date: 2026-04-07
    version: v0.0.1
    author: 916BGAI
    content:
      - First version
---

## PicoClaw 扩展板

PicoClaw 扩展板是一款为 **PicoClaw** 交互应用打造、基于 **LicheeRV Nano** 开发板的功能扩展板，面向语音交互与本地显示场景，集成显示、按键、指示灯、电池管理与音频外设接口，便于快速搭建完整的人机交互终端。

扩展板搭载一块 **240×240 LCD 屏幕**，可用于展示系统状态、识别文本、对话结果与交互菜单；板载 **2 个按键**，用于模式切换、功能确认等操作；板载 **2 个 LED 灯**，用于电源、运行与状态提示。扩展板提供 **Battery 电池接口**，支持充电，**最大充电功率为 3W**。同时支持连接喇叭实现语音播放。

配合定制镜像后，扩展板可与 PicoClaw 协同实现实时语音对话：设备可进行语音采集、识别、生成，并将关键结果同步显示在屏幕上，提供完整的本地交互体验。

PicoClaw 扩展板的主要功能包括：

- 240×240 LCD 显示
- 2 个功能按键
- 2 个状态 LED
- Battery 接口（支持充电，最大 3W）
- 支持喇叭连接与语音输出
- 支持实时对话与结果显示（需配合定制镜像）

### PicoClaw 介绍

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/picoclaw.jpeg" style="width: 90%; height: auto;" alt="picoclaw" >
</div>

PicoClaw 是一个面向低资源设备的开源个人 AI 助手项目，使用 **Go** 从零实现，目标是在低成本、低功耗设备上提供完整的 Agent 能力。项目强调“轻量、快速、可部署”：在资源受限平台上也可运行，并支持多种芯片架构与 Linux 设备。

PicoClaw 主要特性包括：

- **超轻量部署**：面向低内存设备优化，可在入门级硬件上运行。
- **快速启动**：适合本地常驻与即时交互场景。
- **跨平台支持**：支持 RISC-V、ARM、MIPS、x86 等多架构。
- **多通道接入**：可对接 Telegram、Discord、微信、QQ、Slack 等多种聊天平台。
- **丰富模型与工具生态**：支持多家 LLM Provider、MCP、Web 搜索与技能扩展。
- **多形态使用**：支持 WebUI、TUI、CLI 等管理与交互方式。

对于 LicheeRV Nano + PicoClaw 扩展板，PicoClaw 提供语音对话与本地显示能力的上层软件基础：通过配置模型、通道与工具，可快速搭建可用的本地 AI 交互终端。

项目地址：<https://github.com/sipeed/picoclaw>

## 镜像地址

PicoClaw 扩展板定制镜像下载：

[下载地址](https://github.com/sipeed/LicheeRV-Nano-Build/releases)

文件：picoclaw-rv-nano-YYYYMMDD.img.xz

- 烧录方式：可使用 balenaEtcher 直接将镜像烧录进 SD 卡；也可先解压 `.xz` 文件后，使用 `dd` 命令进行烧录。

- 镜像内扩展板功能代码基于 Python，位于 `/opt/app_picoclaw` 目录下，便于按需二次开发和自定义。

## 快速上手

### 1. 连接网络

首先需要进入设备控制台，推荐以下两种方式：

- **串口连接**：可以使用 USB 接口上的 **SBU1/SBU2** 引出的 **UART0**，使用 USB Type-C 转接板引出 **RX0、TX0** 后连接串口工具。

- **USB 网卡连接**：设备默认会创建 **RNDIS** 和 **NCM** 两个 USB 网卡。先查看电脑侧分配到的 USB 网卡 IP，再将 IP 最后一位改为 `1` 作为设备 IP。示例：若主机识别到 `10.166.194.100`，则设备 IP 为 `10.166.194.1`。

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/usb_net.jpeg" style="width: 90%; height: auto;" alt="usb network" >
</div>

然后可以使用 SSH 工具或者串口工具登录设备，默认用户名和密码均为 `root`。登录进设备后可以按照[外设使用](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/5_peripheral.html#WIFI)中的方法连接 Wi-Fi。

### 2. 配置 PicoClaw

第一次进入系统后，PicoClaw 还未完成初始化，需要先进行配置。可以使用 Web UI 或者 TUI 进行配置，以下以 Web UI 为例：

#### Web UI 配置
在浏览器中访问 `http://<设备 IP>:18800`，进入 PicoClaw Web UI。第一次进入需要输入令牌，目前令牌默认为 `root`。

#### 对话模型配置
进入设置界面，选择 **模型**，根据需要选择合适的模型提供商和模型。例如可选择 `openai/gpt-5.4` 作为默认模型。

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/models.jpeg" style="width: 60%; height: auto; border: 1px solid #e5e7eb; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="picoclaw models" >
</div>

- 配置完成后，点击保存并返回对话界面，此时上方会提示 `服务未运行，请先启动以进行对话。`，点击右上角的 `启动服务` 按钮，等待服务启动完成后即可开始对话。

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/chat.jpeg" style="width: 95%; height: auto; border: 1px solid #e5e7eb; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="picoclaw chat" >
</div>

#### 语音模型配置

> 目前 PicoClaw 的 WebSocket channel 还不支持直接输入音频流，因此无法直接调用 PicoClaw 的 ASR 功能进行语音对话。目前 ASR 功能暂时独立于 PicoClaw，不过依旧通过读取 PicoClaw 的配置文件来进行模型配置。

现在还没法直接和 PicoClaw 进行语音对话，需要先配置语音模型。进入模型界面，点击添加模型，然后配置一个 ASR 模型，下面以 `qwen3/qwen3-asr-flash` 为例：

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/asr.jpeg" style="width: 60%; height: auto; border: 1px solid #e5e7eb; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="picoclaw asr" >
</div>

下面是目前支持的 ASR 模型列表：

| 模型 | 提供商 |
| --- | --- |
| `qwen3/qwen3-asr-flash-realtime` | Qwen |
| `qwen3/qwen3-asr-flash` | Qwen |
| `openai/whisper-1` | OpenAI |
| `groq/whisper-large-v3` | Groq |
| `groq/whisper-large-v3-turbo` | Groq |
| `elevenlabs/scribe_v1` | ElevenLabs |

<br>

> 配置的时候需要注意 `模型别名` 要和模型对应，例如 `qwen3/qwen3-asr-flash-realtime` 的别名应为 `qwen3-asr-flash-realtime`。

#### 尝试对话

配置完成后，点击保存。然后按住扩展板左侧的 `KEY1` 按键进行语音输入，松开后会触发 ASR 识别并将结果发送给 PicoClaw。等待 PicoClaw 处理完成后，识别结果和对话回复会显示在屏幕上。

<div style="display:flex; flex-direction:column; gap:10px; margin: 8px 0 16px;">
  <div style="display:flex; gap:10px; justify-content:center;">
    <img src="../assets/RV_Nano/picoclaw/picoclaw_board_1.jpeg" alt="picoclaw board 1" style="width:100%; min-width:180px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
    <img src="../assets/RV_Nano/picoclaw/picoclaw_board_2.jpeg" alt="picoclaw board 2" style="width:100%; min-width:180px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
    <img src="../assets/RV_Nano/picoclaw/picoclaw_board_3.jpeg" alt="picoclaw board 3" style="width:100%; min-width:180px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  </div>
  <div style="display:flex; gap:10px; justify-content:center;">
    <img src="../assets/RV_Nano/picoclaw/picoclaw_board_4.jpeg" alt="picoclaw board 4" style="width:31%; min-width:180px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
    <img src="../assets/RV_Nano/picoclaw/picoclaw_board_5.jpeg" alt="picoclaw board 5" style="width:31%; min-width:180px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  </div>
</div>

## FAQ

- 对话过程中出现报错
  - 可能是模型配置有误，或者当前模型不可用。可以在 Web UI 查看日志确认具体错误信息。
  - 查看 ```/var/log/picoclaw-launcher.log``` 和 ```/var/log/picoclaw-worker.log``` 两个日志文件，确认报错信息。
  - 可以尝试删除 ```/root/.picoclaw``` 目录后重启设备，重新进行配置。

- 使用 ```groq``` 语音模型时报错
  - 目前 ```groq``` 不支持中国大陆访问，可以使用其他模型提供商的模型，或者使用代理工具访问。
