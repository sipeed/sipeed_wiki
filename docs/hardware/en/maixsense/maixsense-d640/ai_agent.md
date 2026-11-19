---
title: Agent Guide
keywords: MaixSense, D640, AI Agent, skill, capture, depth, infrared
update_open: false
update:
  - date: 2026-11-04
    version: v0.1
    author: lxowalle
    content: Initial release
---

Use an AI agent to capture depth or infrared images from MaixSense D640, save files, and check results through a conversation. For example, ask it to capture one depth image and report the valid depth pixel count, or save a left infrared image and provide its location.

## Prepare your agent

1. Choose an agent such as [Codex](https://openai.com/codex/), [Claude Code](https://code.claude.com/docs/en/overview), or [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). Follow its official installation, account, or model setup instructions. Give it access to the downloaded files and local command execution.
2. Connect the camera with a USB data cable.
3. Download the [MaixSense D640 skill](https://cdn.sipeed.com/maixsense/d640/latest/maixsense_d640_skill.zip). Give the ZIP file or its full path to the agent and ask it to extract and read `SKILL.md`:

```text
Extract this skill package and read SKILL.md. Check the environment,
install Python if it is missing, and identify the connected camera's serial.
When ready, tell me which camera you found and which capture operations are available.
```

The skill guides the agent through Python and image-encoding dependency setup and camera identification. If system authorization or additional identity information is needed, the agent will explain the next step.

## Where to put the skill

For temporary use, capable agents can usually read and follow a skill from a path you provide. You do not normally need a special installation directory. Keep `SKILL.md` and its accompanying `scripts` folder together, then ask:

```text
Read SKILL.md in [FULL PATH TO THE SKILL FOLDER]
and follow it to operate the connected MaixSense D640.
```

The agent must be able to read that location and run commands. Providing a path for one conversation is different from installing a skill for automatic discovery across projects.

For regular use, place the complete `maixsense-d640-capture` folder inside one of these default local directories:

| Agent | Current project | All projects for your user |
| :--- | :--- | :--- |
| Codex | `<project>/.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `<project>/.claude/skills/` | `~/.claude/skills/` |
| DSH | `<project>/.dsh/skills/` | `~/.dsh/skills/` |

For example, a Codex project installation contains `.agents/skills/maixsense-d640-capture/SKILL.md` and `scripts/capture.py` inside the same skill folder. Avoid an extra nested copy of the package folder, and do not copy only `SKILL.md`.

On Linux and macOS, `~` means your home directory. On Windows, use `%USERPROFILE%`, for example `%USERPROFILE%\.agents\skills\` for Codex. When the agent runs in WSL, use paths within that WSL environment.

Custom settings may change these defaults. See the official instructions for [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), and [DSH](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md).

## Capture depth

Send this request after the skill has been read:

```text
Use the skill to receive 10 depth frames from the connected MaixSense D640.
Save the last frame in a new folder. Check the result and report the file path,
image dimensions, and valid depth pixel count.
```

This receives ten frames and saves only the last one. It does not record a video. The agent checks the new files and reports whether capture succeeded.

## Capture infrared

```text
Use the same MaixSense D640 to receive 10 left infrared frames.
Save the last frame in a new folder and report its path and image dimensions.
```

Replace “left infrared” with “right infrared” for the other camera. The default capture mode selects one stream per request. Separate depth and infrared requests do not produce a synchronized three-stream set.

## Check the result

The default network capture returns the output location and these files:

| File | Contents |
| :--- | :--- |
| `result.json` | Capture status, device identity, dimensions, and filenames |
| `depth_ID.pgm` | Depth in millimetres, with zero for invalid values |
| `left_ir_ID.jpg`, `right_ir_ID.jpg` | The requested left or right grayscale infrared image |

Infrared defaults to JPG for convenient viewing. Depth remains 16-bit PGM to retain millimetre values. The skill asks the agent to check and, if needed, install Pillow for infrared JPEG encoding.

Check that the agent reports success and provides paths to this capture's new files. A depth capture should also have a valid depth pixel count greater than zero. Creating a file alone does not prove that the measurement is usable.

Some image viewers cannot open 16-bit depth PGM directly. Keep the original for analysis and ask the agent to read the data if needed. For live viewing and distance measurement, use the [desktop app](./gui.md).

## Next steps

- View, measure, and save interactively: [Desktop App Guide](./gui.md).
- Build your own capture program: [SDK Guide](./sdk.md).
- Integrate with a robot: [ROS2 Guide](./ros2.md).
