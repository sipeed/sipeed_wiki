---
title: LicheeRV Nano PicoClaw 扩展板
update:
  - date: 2026-04-07
    version: v0.0.1
    author: 916BGAI
    content:
      - First version
---

[*模型文件于此下载*](https://dl.sipeed.com/shareURL/LICHEE/LicheeRV_Nano/08_RVClaw)
![rvclaw-kit-jpg](../../../zh/lichee/assets/RV_Nano/rvclaw/rvclaw-kit.jpg)


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

[下载地址](https://github.com/sipeed/rvclaw/releases/latest)

文件：picoclaw-rv-nano-YYYYMMDD.img.xz

- 烧录方式：可使用 balenaEtcher 直接将镜像烧录进 SD 卡；也可先解压 `.xz` 文件后，使用 `dd` 命令进行烧录。

- 镜像内扩展板功能代码基于 Python，位于 `/opt/app_picoclaw`（源码：[https://github.com/sipeed/rvclaw](https://github.com/sipeed/rvclaw)），便于按需二次开发和自定义。

## 快速上手 Picoclaw

### 选择应用

应用默认启动后进入应用选择界面，按下 `KEY1` 键选择 PicoClaw 应用，按下 `KEY2` 键选择 CC Buddy 应用。CC Buddy 自定义的虚拟宠物应用，提供了一个可爱的交互界面和简单的对话功能，适合初次使用者体验。

### 连接 Wi-Fi

首先需要进入设备控制台，推荐以下两种方式：

- **串口连接**：可以使用 USB 接口上的 **SBU1/SBU2** 引出的 **UART0**，使用 USB Type-C 转接板引出 **RX0、TX0** 后连接串口工具。

- **USB 网卡连接**：设备默认会创建 **RNDIS** 和 **NCM** 两个 USB 网卡。先查看电脑侧分配到的 USB 网卡 IP，再将 IP 最后一位改为 `1` 作为设备 IP。示例：若主机识别到 `10.166.194.100`，则设备 IP 为 `10.166.194.1`。

<div align="center">
  <img src="../assets/RV_Nano/picoclaw/usb_net.jpeg" style="width: 90%; height: auto;" alt="usb network" >
</div>

然后可以使用 SSH 工具或者串口工具登录设备，默认用户名和密码均为 `root`。

**登录进设备后可以按照下述方法连接 Wi-Fi。**

<details>
<summary>连接 Wi-Fi</summary>

> ```bash
> # 在 sd 卡第一个分区创建 wifi.sta 文件启用 sta 模式:
> touch /boot/wifi.sta && rm -f /boot/wifi.ap /boot/wifi.mon
> 
> # 然后将 AP 的 SSID 和密码写入文件:
> echo ssid > /boot/wifi.ssid
> echo pass > /boot/wifi.pass
> 
> # 最后重启 Wifi 服务
> /etc/init.d/S30wifi restart
> ```

</details>

### 配置 PicoClaw

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

## CC Buddy 应用

### CC Buddy 介绍

<div align="center">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_hero.jpg" style="width: 90%; height: auto;" alt="📷 cc buddy hero" >
</div>

**CC Buddy** 是 PicoClaw 扩展板镜像内置的另一款应用，定位为 **Claude Code 的桌面伙伴设备（Companion Device）**。它将 Claude Code 的交互过程“拟物化”为一只可爱的虚拟宠物（ASCII Pet），并把 Claude Code 在执行命令、调用工具时所产生的 **权限审批请求**（Permission Request）从电脑端直接转移到 LicheeRV Nano 这块小屏幕上：在屏幕上一键允许或拒绝，决策结果会回传给 Claude Code，从而无需切回电脑窗口即可控制 Agent 的行为。

CC Buddy 移植自 Felix Rieseberg 的 [claude-desktop-buddy](https://github.com/anthropics/claude-desktop-buddy) 项目，针对 LicheeRV Nano + PicoClaw 扩展板做了专门适配：使用 240×240 ST7789 显示、KEY1(A)/KEY2(B) 双按键、板载 LED 等外设。源码位于系统镜像的 `/opt/app_cc_buddy`。

CC Buddy 的核心设计理念：

- **拟物化反馈**：把 Claude Code 的运行状态（空闲、忙碌、等待审批、完成任务等）映射成宠物的情绪与动作，让看不见的 Agent 行为变得直观。
- **就近审批**：Claude Code 的权限请求被推送到设备屏幕，直接按键 A/B 即可批准或拒绝，省去电脑的窗口切换，优化体验。
- **CLI 桥接**：通过 Claude Code 官方 Hook 机制 + 本地守护进程将事件桥接到设备 TCP 端口，无需修改 Claude Code 本体。

### 主要功能

- 240×240 LCD 上以 ASCII 像素风格显示宠物形象（默认提供 `capybara`、`cat`、`robot` 三种形象，可在设置中切换）
- 实时显示 Claude Code 会话状态：会话总数、运行中、等待中、Token 消耗、最近一行命令/输出
- 权限审批弹窗：显示工具名称、提示信息、等待秒数，超过 10 秒会高亮提醒
- 宠物养成系统：根据“审批速度、拒绝次数、Token 消耗”计算情绪值（mood）、饱食度（fed）和精力（energy），累计 Token 触发升级动画
- 多种显示模式：HUD（脚本/转录）、INFO（设备/网络/统计信息）、PET（宠物状态页）、CLOCK（无 Claude 连接时切换为时钟）
- 可选 LED 状态闪烁、屏幕自动息屏（30 秒无操作）、声效反馈（可在设置中开关）
- 一键从应用菜单切换回 PicoClaw 应用（无需重启）

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_hud.jpg" alt="📷 cc buddy hud mode" style="width:23%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P4.jpg" alt="📷 cc buddy info mode" style="width:23%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_pet_P1.jpg" alt="📷 cc buddy pet mode" style="width:23%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_clock_species_capybara.jpg" alt="📷 cc buddy clock mode" style="width:23%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>

<details>
<summary>Full Mode </summary>

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_pet_P1.jpg" alt="📷 cc buddy pet mode P1" style="width:48%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_pet_P2.jpg" alt="📷 cc buddy pet mode P2" style="width:48%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P1.jpg" alt="📷 cc buddy info mode P1" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P2.jpg" alt="📷 cc buddy info mode P2" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P3.jpg" alt="📷 cc buddy info mode P3" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P4.jpg" alt="📷 cc buddy info mode P4" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P5.jpg" alt="📷 cc buddy info mode P5" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_info_P6.jpg" alt="📷 cc buddy info mode P6" style="width:31%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>
</details>

### 连接方式

CC Buddy 通过 **Claude Code CLI（Hooks + Daemon）** 与设备通信。

适用于使用 `claude` 终端命令行的用户。需要在电脑上常驻一个守护进程（daemon），由它把 Claude Code 的 Hook 事件桥接到设备的 TCP 端口。

```
Claude Code CLI (sessions)
    │ HTTP hooks（自动注入到 ~/.claude/settings.json）
    ▼
cc_buddy_daemon.py (默认 :9876)
    │ TCP
    ▼
RVClaw 设备 (:19000)
```

在电脑端启动 daemon（[脚本于此下载](https://raw.githubusercontent.com/sipeed/rvclaw/refs/heads/main/app_cc_buddy/hooks/cc_buddy_daemon.py)）：

```bash
python3 cc_buddy_daemon.py --device <RVCLAW_IP>
# 自定义端口
python3 cc_buddy_daemon.py --device <RVCLAW_IP> --port 9877
```

启动后 daemon 会自动：

- 将以下 Hook 写入 `~/.claude/settings.json`，退出（Ctrl+C / SIGTERM）时自动清理
- 监听 `http://127.0.0.1:9876` 接收 Claude Code 的 Hook 事件
- 通过 TCP 连接到 RVClaw 的 `19000` 端口推送心跳并接收按键决策

| Hook | 用途 |
| --- | --- |
| SessionStart / SessionEnd | 维护活跃会话计数 |
| PreToolUse | 标记“运行中”状态并构建命令转录 |
| PostToolUse | 清除“运行中”状态 |
| Stop | 标记会话生成完成 |
| **PermissionRequest** | **阻塞**等待设备按键决策（默认 30s 超时） |
| PermissionDenied | 清除“等待中”状态 |
| PreCompact | 同步 Token 计数 |

随后正常使用 `claude` 即可：当 Claude 需要权限时，设备会切到审批界面，按 **A 批准 / B 拒绝**，决策通过 daemon 回传给 Claude Code。

<div align="center">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_approval.jpg" style="width: 60%; height: auto; border: 1px solid #e5e7eb; border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" alt="📷 cc buddy approval" >
</div>

### 按键操作

CC Buddy 的两个按键复用为多种功能，行为根据当前界面变化：

| 操作 | A（左侧） | B（右侧） |
| --- | --- | --- |
| 主界面短按 | 切换显示模式（NORMAL / PET / INFO） | 在 INFO/PET 页内翻页；HUD 模式下滚动转录 |
| 长按（≥ 600ms） | 弹出主菜单（settings / help / about / demo / to picoclaw / close） | — |
| 审批界面 | **批准**（once） | **拒绝**（deny） |
| 菜单/设置打开时 | 移动选择项 | 确认/触发当前项 |
| 屏幕息屏时 | 唤醒（首次按键不触发功能） | 唤醒（首次按键不触发功能） |

> 在主菜单中选择 `to picoclaw` 即可在不重启系统的前提下切换回 PicoClaw 应用（CC Buddy 的服务停止，PicoClaw 的服务启动）。

### 设置项与持久化

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_menu.jpg" alt="📷 cc buddy menu" style="width:45%; min-width:200px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_settings.jpg" alt="📷 cc buddy settings" style="width:45%; min-width:200px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>

进入 `主菜单 → settings`，可配置以下项目：

| 设置项 | 含义 | 取值 |
| --- | --- | --- |
| brightness | 显示亮度档位 | 0–4 |
| sound | 提示音开关 | on / off |
| led | 状态 LED 开关（等待审批时闪烁） | on / off |
| transcript | HUD 转录显示开关 | on / off |
| ascii pet | 宠物形象选择 | capybara / cat / robot |
| sleep | 自动息屏开关（30s 无操作） | on / off |
| reset stats | 清空养成数据并恢复出厂 | — |

设备数据持久化到 `/root/.cc_buddy/`：

- `stats.json`：等级、token 累计、approve/deny 计数、宠物形象索引、主人/宠物名等
- `settings.json`：上述设置项

### 宠物养成规则

<div style="display:flex; gap:10px; justify-content:center; margin: 8px 0 16px;">
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_clock_species_capybara.jpg" alt="📷 cc buddy capybara" style="width:30%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_clock_species_cat.jpg" alt="📷 cc buddy cat" style="width:30%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
  <img src="../../../zh/lichee/assets/RV_Nano/rvclaw/cc_buddy_mode_clock_species_robot.jpg" alt="📷 cc buddy robot" style="width:30%; min-width:160px; height:auto; border:1px solid #e5e7eb; border-radius:6px; box-shadow:0 2px 8px rgba(0,0,0,.1);" />
</div>

- **MOOD（情绪）**：审批越快情绪越高（< 5 秒会触发 `HEART` 一次性动画），频繁拒绝会降低情绪
- **FED（饱食度）**：每累计约 50K tokens 升级一次，并播放 `CELEBRATE` 动画
- **ENERGY（精力）**：设计上将屏幕朝下放置触发“小睡”回满精力（当前未支持）
- **状态映射**：连接断开 → IDLE，等待审批 → ATTENTION（伴随 LED 闪烁），同时运行 ≥ 3 个会话 → BUSY，最近完成 → CELEBRATE，深夜（1:00–7:00）且无 Claude 连接 → SLEEP（时钟模式）

### 二次开发

开发仓库地址位于 [Github app_cc_buddy](https://github.com/sipeed/rvclaw/tree/main/app_cc_buddy)。
CC Buddy 完全使用 Python 编写，目录结构清晰：

| 文件 | 作用 |
| --- | --- |
| `main.py` | 主事件循环、按键调度、状态切换、显示刷新 |
| `config.py` | 引脚定义、SPI 参数、字体路径、UI 布局常量 |
| `ui.py` | 启动画面、HUD、审批页、Info/Pet/Clock/Menu/Settings 各界面绘制 |
| `buddy.py` + `buddies/*.py` | 宠物形象渲染器（已注册 capybara、cat、robot） |
| `state.py` | `TamaState`、`PersonaState`、`DisplayMode` 等数据结构 |
| `protocol.py` | JSON 心跳/命令解析与权限响应封装 |
| `transport.py` | TCP（19000）通信实现 |
| `hooks/cc_buddy_daemon.py` | 电脑端 Hook 桥接守护进程 |
| `S99cc_buddy_app` | 开机自启脚本 |

可在 `buddies/` 下新增 species 文件并在 `buddies/__init__.py` 中 `register_species()` 注册即可扩展自定义宠物形象。

## FAQ

- 对话过程中出现报错
  - 可能是模型配置有误，或者当前模型不可用。可以在 Web UI 查看日志确认具体错误信息。
  - 查看 ```/var/log/picoclaw-launcher.log``` 和 ```/var/log/picoclaw-worker.log``` 两个日志文件，确认报错信息。
  - 可以尝试删除 ```/root/.picoclaw``` 目录后重启设备，重新进行配置。

- 使用 ```groq``` 语音模型时报错
  - 目前 ```groq``` 不支持中国大陆访问，可以使用其他模型提供商的模型，或者使用代理工具访问。
