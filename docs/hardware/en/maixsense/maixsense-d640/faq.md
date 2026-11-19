---
title: FAQ
keywords: MaixSense, D640, troubleshooting
update_open: false
update:
  - date: 2026-10-27
    version: v0.1
    author: lxowalle
    content: Initial release
---

## The computer cannot find the camera

1. Try another USB-C data cable and connect directly to the computer.
2. Wait for startup, then refresh the device list.
3. Select **UVC** as the connection type and choose the D640 by serial.
4. On Linux, check [USB and video access permissions](./quick-start.html#linux-access).
5. Close other camera applications, then reconnect the device.

## The camera is listed but there is no image

Keep only one capture program running. Close other desktop apps, browser previews, and SDK examples. Connect the camera and enable the required views. Raw depth and device-generated pseudocolor are alternative device modes. See [Choose the views](./gui.md).

## Why can I not measure distance in a color depth image?

Two views may look similar. The desktop app can colorize raw Depth16 while retaining distance values, so you can measure a point. Device-generated MJPEG pseudocolor has no raw millimetre values and cannot support measurement. Select raw Depth16, click a valid target, and read the distance at the bottom-right. See [Measure distance](./gui.md).

## The point cloud does not open

Select raw Depth16, wait for a complete synchronized frame set, and check that camera calibration can be read. Video may work while point clouds do not if control permissions or SDK/firmware compatibility prevent calibration access. For a WebGL error, check hardware acceleration and the graphics driver. See [Desktop App Guide](./gui.md).

## Why does depth contain black areas or holes?

Transparent, mirror-like, strongly reflective, very dark, overexposed, or textureless surfaces can produce invalid depth. Occlusion edges can do so too. Keep the target within the camera version's measurement range, inspect both infrared images, and adjust lighting or camera angle. Hole filling can improve the display but does not guarantee a true distance. See [Adjust the depth display](./gui.md).

## Does a millimetre depth value mean millimetre accuracy?

No. Millimetres are the data unit, not a fixed error specification. In the recorded tests, the mean absolute relative error was approximately 0.65% for the short baseline and 1.27% for the long baseline. Error depends on distance and the scene, and may vary within approximately ±5%. See [Measurement Accuracy](./accuracy.md) for conditions, individual points, and calculations.

## The browser cannot find the camera or show distance

The browser accesses cameras on the computer where the page is open. Connect the D640 to that computer, allow camera access, and use a trusted HTTPS page. Browser preview displays decodable video rather than raw metric depth. Use the desktop app for measurement and point clouds. See [Quick Start](./quick-start.md).

## A firmware or calibration update failed

1. Save the complete error message. Do not disconnect power or USB while installation or restart is still in progress.
2. Check the `.tar.gz` package type, supported camera version, and device serial. Firmware and calibration packages are not interchangeable.
3. For permission errors, check USB control access. If an update interface is missing, follow the release instructions.
4. After the operation has ended, reconnect and check device information. If the device does not return, provide the error and version information to technical support.

Calibration is specific to each camera. Do not copy another camera's calibration to troubleshoot. See [Desktop App Guide](./gui.md).

## Why does SDK capture save only three files with `--frames 10`?

The example waits for ten complete frame sets and saves only the last set: depth or pseudocolor, left IR, and right IR. For continuous recording, use MCAP in the desktop app or write your own SDK save loop. See [SDK Guide](./sdk.md).

## Why is there a `.mcap.part` file?

The recording has not finished normally. Click **Stop recording** and wait for the completed `.mcap` file. A disconnect or write error may leave `.part`. Renaming its extension does not make it a complete recording. See [Desktop App Guide](./gui.md).

## Which baseline should I choose?

The baseline is the spacing between the cameras. Choose 50 mm for approximately 0.25–2.0 m work, or 100 mm for approximately 0.5–4.0 m. Evaluate the camera at the intended distance and in the actual scene.

## Next steps

- Reconnect and view images: [Quick Start](./quick-start.md).
- Follow the operating steps: [Desktop App Guide](./gui.md).
