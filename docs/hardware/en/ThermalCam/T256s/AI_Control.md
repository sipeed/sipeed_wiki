---
title: Controlling with AI
keywords: T256s, ThermalCam, thermal camera, AI, HTTP, MCP, LLM, inspection, temperature
---

## Introduction

The T256s has no language model inside. It exposes temperatures, images and raw data over HTTP on its USB network adapter, so any AI tool that can send an HTTP request can read that data and draw conclusions.

No extra server and no SDK are needed. There are two ways to connect:

+ Call the HTTP API directly: when the AI tool can run commands (curl, Python and so on), let it call the API. This is the simplest option and the recommended one;
+ Use MCP: when the AI tool supports MCP, run the bundled MCP server on your computer so the API becomes fixed tools and the model does not have to build commands; this page uses OpenCode as the example.

Both paths read exactly the same data from the same HTTP API. The MCP server is only a thin adapter and is not required.

## How It Works

```text
Option 1: AI tool --HTTP--> T256s  http://192.168.17.1

Option 2: AI tool --MCP--> t256s_mcp_server.py
                --HTTP--> T256s  http://192.168.17.1
```

In both cases:

+ The data comes from `/api/v1/thermal`, `/frame.jpg` and `/frame.temp16`;
+ The MCP server runs on your computer, provides read-only tools only and never changes camera settings;
+ The camera stays connected over USB as usual, and the network adapter address does not change.

## Preparation

Before you start, check the following:

+ The camera runs firmware 26.40.0 or later, is connected, and `http://192.168.17.1` opens in a browser;
+ Option 1: the AI tool can run local commands, for example Claude Code, OpenCode or Cursor;
+ Option 2: Python 3.8 or later is installed, `t256s_mcp_server.py` has been downloaded, and the AI tool supports MCP (OpenCode, for example).

> You can check the firmware version on the device status panel or the device web page; see [System Update](System_Update.html).

## Option 1: Call the HTTP API Directly (Recommended)

When the AI tool can run commands, no middleware is needed; let it call the API.

### Check the API First

```bash
curl http://192.168.17.1/api/v1/thermal
```

Once it returns temperature JSON, the AI can use the camera.

### Tell the AI the Rules

State the rules at the start of the conversation; it is far more reliable than repeating them every turn:

```text
You are connected to a Sipeed T256s thermal camera
at http://192.168.17.1.

Data rules:
1. Read temperatures only from /api/v1/thermal;
   use /frame.temp16 for per-pixel data;
2. Always include the frame number and coordinates;
   coordinates use the 256x192 landscape frame;
3. Sample at least 5 times before claiming a trend;
4. Read-only endpoints are fine; ask me before
   changing the subnet or other settings;
5. If you cannot read data, say so instead of inventing values.
```

After that, just ask questions and the AI runs `curl` itself.

### Examples

```text
Use T256s to read the current maximum temperature
and tell me where it is in the frame.
```

```text
Use T256s to watch for 10 seconds and tell me
whether the temperature is rising or stable.
```

```text
Use T256s to capture a frame, save it, and explain
which area is hottest using the temperatures.
```

```text
Use T256s to read the temperature every 5 seconds
for one minute and warn me if it goes above 60 °C.
```

Start with simple, verifiable requests such as a single reading or a short trend. When asking the AI to sample for a long time, agree on the interval first so it does not send requests continuously.

> Trust the numbers returned by the API. JPEG frames help with position and shape, but they are already colorized and the colors are not temperatures. If the AI estimates a temperature from colors, do not rely on that number.

## Option 2: Use MCP (Optional)

Use this when you want the read endpoints as fixed tools (for example with OpenCode), or when the client can only take tools over MCP.

### Prepare the Script

Save [t256s_mcp_server.py](../../../zh/ThermalCam/T256s/assets/t256s_mcp_server.py) on your computer, for example in a `t256s` folder under your user directory.

The script reads the camera address from the `T256S_BASE` environment variable and defaults to `http://192.168.17.1`. If you changed the subnet, update that variable; the script itself needs no changes.

> The script uses only the Python standard library and needs no extra dependencies. On Windows the Python command is usually `python`; on Linux and macOS it is usually `python3`.

### Add MCP to OpenCode

OpenCode takes MCP servers from its configuration file. Put the global configuration in `~/.config/opencode/opencode.json`, or a project-level `opencode.json` in the project directory.

You can also add it from the command line, and OpenCode writes the structure your version expects:

```bash
opencode mcp add t256s --env T256S_BASE=http://192.168.17.1 -- python3 /path/to/t256s_mcp_server.py
```

To edit the file by hand, add a `t256s` entry next to the others under `mcp`; leave the existing entries untouched:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "t256s": {
      "type": "local",
      "command": ["python3", "/path/to/t256s_mcp_server.py"],
      "environment": { "T256S_BASE": "http://192.168.17.1" }
    }
  }
}
```

> Newer OpenCode (V2) puts servers under `mcp.servers`. If your file already uses `"mcp": { "servers": { ... } }`, add `t256s` inside `servers`; the fields stay the same.

In this entry:

+ `type` must be `local`, which tells OpenCode to start the process on this machine;
+ `command` is the launch command: the first item is the Python command, the second is the script path; use `python3` on Linux and macOS and `python` on Windows;
+ `T256S_BASE` in `environment` is the camera address.

Save the file and reopen OpenCode; the server connects automatically. Run `/mcps` inside OpenCode and check that `t256s` is connected.

### Verify the Connection

After restarting, the tool list should show the four tools provided by `t256s`:

| Tool | Purpose |
| --- | --- |
| `t256s_device_info` | Model, firmware, resolution and supported formats |
| `t256s_thermal` | Center, maximum and minimum of the current frame, with coordinates |
| `t256s_capture` | Capture a JPEG and return that frame's temperatures |
| `t256s_watch` | Sample temperatures for a while and return the trend |

Try a simple request first:

```text
Use T256s to read the current temperature and tell me
the maximum and where it is.
```

The AI should call `t256s_thermal` and answer with real numbers. If the tool list is empty, see the [FAQ](#FAQ).

## Other: Integrate Into Your Own Application

To connect the camera to your own platform or tool-calling pipeline, use the bundled OpenAPI description:

[openapi.json](../../../zh/ThermalCam/T256s/assets/openapi.json)

After import, each `operationId` becomes a tool. For AI-facing toolsets, keep only the read endpoints and leave out subnet changes.

## FAQ

### Do I have to use MCP

No. A tool that can run commands, such as OpenCode, can call the HTTP API directly; MCP only turns the API into fixed tools and keeps the model from building commands on its own.

### The AI cannot read data

Check the following:

+ The camera is connected and `http://192.168.17.1` opens in a browser;
+ `curl http://192.168.17.1/api/v1/thermal` works;
+ The AI tool is allowed to run commands and access the local network;
+ For hand-built HTTP requests, the `Host` header is the camera address; otherwise it is treated as a captive-portal probe.

### The t256s tools do not appear in the AI tool

Check the following:

+ The AI tool was fully quit and reopened after saving the configuration;
+ The hierarchy and field names under `mcp` are correct (`mcp.servers` on newer versions), and `type` is `local`;
+ The command in the `command` array runs in a terminal, for example `python3 --version`;
+ The script path in the `command` array is correct; use the full path when it contains spaces;
+ The script has no syntax error; run `python3 t256s_mcp_server.py` in a terminal once to confirm.

### The AI can read temperatures but capture fails

Check the following:

+ `/frame.jpg?source=sr` opens in a browser;
+ Another program is not consuming most of the USB bandwidth, for example several video streams;
+ You are not holding 4 or more continuous streams; beyond the limit the camera returns `409`.

### The AI reads 0 or NaN

The camera may not have a usable frame right after boot. Wait a second or two and read again. If it persists, open `/api/v1/thermal` in a browser to check whether the API itself works.

### Windows reports that python3 is not found

On Windows the Python command is usually `python`. Change the first item of the `command` array to `python`, or run `where python` in a terminal to confirm the command name.

### The AI cannot read data after the subnet changed

When calling HTTP directly, use the new `192.168.<segment>.1` address in the conversation. With MCP, update `T256S_BASE` in the configuration, save and restart the AI tool.

### Can the AI change the palette or subnet

No. The current API has no palette control, and changing the subnet is a write operation that the AI rules should forbid; do it manually when needed (see [HTTP API](API.html)).

### API temperatures differ from the camera screen

Common causes:

+ The two readings come from different frames;
+ The camera has just powered on and has not reached thermal equilibrium;
+ The target surface has low emissivity, such as shiny metal;
+ The AI used image colors instead of API data.

Confirm that the AI used values from `/api/v1/thermal` or TEMP16, not a description of the image.

## Safety Notes

+ Connect trusted AI tools only;
+ Do not expose `192.168.17.1` to the public internet or open it on untrusted networks;
+ Forbid write operations in the conversation rules; change the subnet manually when needed;
+ Do not leave the AI sampling unattended for long periods;
+ Before entering passwords or keys, confirm that the AI tool and network are trusted.

## Next Steps

+ For endpoint fields, data formats and error codes, see [HTTP API](API.html);
+ To view the picture over UVC first, see the [User Guide](UG.html).
