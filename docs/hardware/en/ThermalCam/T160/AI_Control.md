---
title: MS-T160 AI Integration
keywords: MaixSense, Thermal, MS-T160, T160, thermal camera, AI, HTTP, MCP, LLM, temperature
update:
  - date: 2026-11-18
    version: v0.1
    author: Sipeed
    content:
      - Initial release covering direct HTTP use, the MCP server and an FAQ
      - Added letting AI edit the web page
---

# AI Integration

The T160 has no language model inside. It exposes temperatures and images over HTTP on its USB network adapter. Any AI tool that can send HTTP requests can read that data and answer questions such as "which part on this board is hottest" or "is the temperature rising over the last minute".

No extra server or SDK is needed. There are two ways to connect:

- **Call HTTP directly (recommended)**: if your AI tool can run commands such as curl or Python, let it call the API. This is the simplest way.
- **Use MCP**: if your AI tool supports MCP, run the included MCP server on your computer to turn the API into fixed tools, so the model does not build commands itself. This page uses OpenCode as the example.

Both ways read exactly the same data. The MCP server is only a thin adapter and is optional.

Besides reading data, an AI can also edit the T160 web page for you. See [Let AI Edit the Web Page](#Let-AI-Edit-the-Web-Page).

## How It Works

```text
Option 1: AI tool --HTTP--> T160  http://192.168.17.1

Option 2: AI tool --MCP--> t160_mcp_server.py
                  --HTTP--> T160  http://192.168.17.1
```

- Both options read endpoints such as `/api/v1/thermal` and `/frame.temp8`. See [Advanced Use and Development](./Advanced.md).
- The MCP server runs on your computer and offers read-only tools. It never changes device settings.

## Before You Start

Check that:

- The T160 is plugged into the computer and `http://192.168.17.1` shows the image in a browser.
- Option 1: your AI tool can run local commands, for example Claude Code, OpenCode or Cursor.
- Option 2: Python 3.8 or later is installed and your AI tool supports MCP, for example OpenCode.

## Option 1: Call HTTP Directly (Recommended)

### Check the API

```bash
curl http://192.168.17.1/api/v1/thermal
```

If you get temperature JSON with `"valid":true`, you are ready.

### State the Rules in the Conversation

Rules at the start of the conversation work better than reminders later:

```text
You are connected to a Sipeed MS-T160 thermal camera at http://192.168.17.1.
Rules:
1. Read temperatures only from /api/v1/thermal; use /frame.temp8 for per-pixel data (format in the T160 docs).
2. Include the frame number and coordinates in answers; coordinates use the 160x120 native landscape image.
3. Take at least 5 samples before judging a trend.
4. Do not read /stream.temp8, so you do not take the image away from the web page.
5. Read-only endpoints are fine; ask me before any write such as changing the subnet or updating firmware.
6. If you cannot read data, say so. Never make numbers up.
```

Then just ask. The AI runs `curl` or Python to fetch the data.

### Examples

```text
Using the T160, read the current maximum temperature and tell me where it is in the image.
```

```text
Using the T160, watch for 10 seconds and tell me whether the temperature is rising or stable.
```

```text
Using the T160, read the temperature every 5 seconds for 1 minute and alert me above 60 °C.
```

Start with simple, checkable tasks, such as one reading and then one trend.

> Trust the numbers from the API. Colors in an image only show what is warmer or cooler; ignore any temperature the AI estimates from colors.

## Option 2: Use MCP (Optional)

Run the included MCP server if you want fixed tools, or if your AI tool can only use tools through MCP.

### Get the Script

Save [t160_mcp_server.py](../../../zh/ThermalCam/T160/assets/t160_mcp_server.py) on your computer, for example in a `t160` folder under your user directory.

The script reads the device address from the `T160_BASE` environment variable, `http://192.168.17.1` by default. If you changed the subnet, change this variable in the configuration; the script itself stays the same.

> The script uses only the Python standard library, so there is nothing else to install. Windows usually uses the `python` command; Linux and macOS usually use `python3`.

### Add the MCP Server to OpenCode

The quickest way is the command line. OpenCode writes the right structure for its current version:

```bash
opencode mcp add t160 --env T160_BASE=http://192.168.17.1 -- python3 /path/to/t160_mcp_server.py
```

You can also edit the configuration file: `~/.config/opencode/opencode.json` globally, or `opencode.json` in a project folder. If other MCP servers are already there, add a `t160` entry next to them under `mcp`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "t160": {
      "type": "local",
      "command": ["python3", "/path/to/t160_mcp_server.py"],
      "environment": { "T160_BASE": "http://192.168.17.1" }
    }
  }
}
```

> Newer OpenCode versions put servers under `mcp.servers`. If your file already uses `"mcp": { "servers": { ... } }`, add `t160` inside `servers`; the fields stay the same.

- `type` is always `local`, so OpenCode starts the process on your computer.
- `command` is the start command: the Python command first, then the script path.
- `environment` sets `T160_BASE`, the device address.

Save the file and reopen OpenCode; the server connects automatically. Run `/mcps` in OpenCode and check that `t160` is connected.

### Check the Tools

The tool list should show four tools from `t160`:

| Tool | Purpose |
| --- | --- |
| `t160_device_info` | Model, firmware, resolution and supported formats |
| `t160_thermal` | Center, maximum and minimum of the current frame, with coordinates |
| `t160_capture` | Capture one frame as an Ironbow PNG, oriented like the web page, plus that frame's temperatures |
| `t160_watch` | Sample temperatures for a while and return the trend |

Try a simple request:

```text
Using the T160, read the current temperature and tell me the maximum and where it is.
```

The AI should call `t160_thermal` and answer with real numbers.

## Let AI Edit the Web Page

The T160 web page is a single HTML file with no build step, which makes it easy to hand to an AI. You can ask for a new color scheme or layout, larger buttons for the features you use most, your own notes on the page, or a page built for one particular inspection task. Once uploaded, your page replaces the built-in one and stays there through restarts and firmware updates.

### Steps

First, download the source of the built-in page:

```bash
curl http://192.168.17.1/builtin -o t160.html
```

You can also open `http://192.168.17.1/builtin` in a browser, view the page source, and copy all of it into `t160.html`. Do not use the browser's **Save as**: it may save the page after scripts have changed it, or split it into several files.

Then:

1. Give `t160.html` to the AI. Send the [rules](#Rules-for-the-AI) below first, then describe what you want.
2. Upload the edited file: in the **Device settings & firmware** panel, find **Custom web appearance**, choose the file and tap **Upload & apply**. You can also [upload from the command line](#Upload-and-Restore-from-the-Command-Line).
3. Reload the page to check the result. If something is off, tell the AI, then upload the new version.

Change one thing at a time and check it before moving on, so a problem is easy to trace. Keep a copy of your requests; you will need them again after a firmware update.

### Rules for the AI

Send this to the AI as rules it must follow:

```text
The attached t160.html is the built-in web page of a Sipeed MS-T160 thermal camera. The device serves HTTP over a USB network adapter at http://192.168.17.1, and serves this page itself once uploaded.
Edit this file and follow these rules:
1. The result must still be one complete HTML file, UTF-8, no larger than 126976 bytes (124 KiB). The original is about 98 KB, which leaves about 28 KB, so keep additions lean.
2. Do not load anything from the internet: no CDN scripts, web fonts or remote images. The phone or computer may be offline. Use inline SVG for icons and data URIs for images.
3. Use relative paths for every API call (for example /frame.temp8), never a hard-coded 192.168.17.1, so the page keeps working after a subnet change.
4. Unless I ask, do not change: the code that reads /frame.temp8 and /stream.temp8, the 120-byte metadata parsing and temperature conversion, super resolution (the WebGL code in createGpuSr, plus /assets/sr-fast.wasm, /assets/sr-fast-simd.wasm, /assets/sr-fast.bin), image rotation, or <canvas id="view"> and #overlay.
5. Keep the Device settings & firmware panel, especially Restore built-in page and the firmware update.
6. Every write (page upload, firmware update, subnet change) must send the header X-Sipeed-Request: 1.
7. When done, list the changes and the file size. Ask me before uploading anything to the device.
```

### Upload and Restore from the Command Line

An AI tool that can run commands can upload the page itself. Uploading writes to the device's flash, so review the changes before you let the AI run it, and do not unplug the device while it writes.

```bash
# Check whether a custom page is in use, its size and the limit
curl http://192.168.17.1/api/v1/web

# Upload a custom page
curl -X POST http://192.168.17.1/api/v1/web \
  -H 'Content-Type: text/html' \
  -H 'X-Sipeed-Request: 1' \
  --data-binary @t160.html

# Delete the custom page and go back to the built-in one
curl -X DELETE http://192.168.17.1/api/v1/web \
  -H 'X-Sipeed-Request: 1'
```

A successful upload returns `{"ok":true,"custom":true,"bytes":...}`. A `400` usually means a missing header or a file larger than 124 KiB. A `409` means an earlier upload has not finished; try again shortly.

### If the Page Breaks

Open `http://192.168.17.1/builtin` in a browser; the built-in page is always available there. Tap **Restore built-in page** in its **Device settings & firmware** panel, or run the delete command above, to remove the custom page.

## FAQ

### Do I have to use MCP?

No. AI tools that can run commands can call HTTP directly. MCP only turns the API into fixed tools so the model builds fewer commands itself.

### The AI cannot read any data

Check that:

- The T160 is plugged in and `http://192.168.17.1` opens in a browser.
- `curl http://192.168.17.1/api/v1/thermal` returns data.
- The AI tool may run commands and access the local network.

### The t160 tools do not appear in the AI tool

Check that:

- You fully quit and reopened the AI tool after saving the configuration.
- The nesting and field names under `mcp` are correct and `type` is `local`.
- The Python command in `command` runs in a terminal, for example `python3 --version`.
- The script path is correct. You can also run `python3 t160_mcp_server.py` once in a terminal to check for errors; it then waits for input, so press Ctrl+C to quit.

### The AI gets invalid temperatures

Right after plugging in, the device may have no image yet and the API returns `"valid": false`. Read again after 1 to 2 seconds. If it stays that way, open `/api/v1/thermal` in a browser to check the API itself.

### The web page freezes whenever the AI reads data

The AI is probably reading `/stream.temp8`. The T160 serves only one stream at a time, so the AI and the page keep taking it from each other. Ask the AI to use `/api/v1/thermal` or `/frame.temp8` instead.

### Windows says python3 is not found

On Windows the command is usually `python`. Change the first element of `command` to `python`.

### The AI stopped reading data after a subnet change

For direct HTTP, change the address in the conversation to `192.168.<subnet>.1`. For MCP, change `T160_BASE` in the configuration, save, and restart the AI tool.

### The AI's temperature differs from the web page

Common causes:

- The two readings come from different frames while the temperature is changing.
- The surface has low emissivity, such as shiny metal; see the [FAQ](./FAQ.md).
- The AI estimated temperature from image colors instead of API data.

### The custom page misbehaves after a firmware update

The custom page survives firmware updates, but the new built-in page may have changed its API use or features. Download the new `/builtin` again, send your earlier requests to the AI, and let it redo the changes on the new file.

### The upload says the file is too large

A custom page can be up to 124 KiB. Ask the AI to trim it: drop features you do not use, and replace images with SVG or compress them before embedding.

## Safety

- Connect only AI tools you trust.
- The API has no authentication. Use it over the direct USB link only, and never forward it to a LAN or the internet.
- Forbid writes in the conversation rules; let a person change the subnet or update firmware.
- When an AI edits the web page, read the changes it lists before you upload.
- Do not let an AI collect data continuously without supervision.

## Next Steps

- For API fields and data formats, see [Advanced Use and Development](./Advanced.md).
- If something goes wrong, see the [FAQ](./FAQ.md).
