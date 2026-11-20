---
title: MS-T256S FAQ
keywords: MaixSense, Thermal, MS-T256S, T256S, thermal camera, FAQ, troubleshooting, OTG, UVC, 192.168.17.1, temperature, firmware update
update:
  - date: 2026-11-19
    version: v1.0
    author: Sipeed
    content:
      - Regroup by connection, screen and image, temperature, photos and files, firmware and development, with question-style headings
      - Update the answers for the 26.47.0 gesture interface, web page and update methods, and merge in the questions from the former System Update page
      - Add questions on the web page, iPhone and iPad, gain ranges, multi-device subnets and the update tool not finding the camera
  - date: 2026-11-17
    version: v0.3
    author: Sipeed
    content:
      - Correct the firmware update version boundary and add HTTP API questions
  - date: 2026-04-24
    version: v0.2
    author: Sipeed
    content:
      - Add firmware update steps and what to do after a power cut
  - date: 2026-03-24
    version: v0.1
    author: Sipeed
    content:
      - Initial English version
---

# FAQ

## Power and Connection

### The Screen Keeps Restarting or Flickering

This is usually a power problem. Super resolution draws more power, so the T256S needs a stable supply:

- Use a good USB-C cable. Long or thin cables lose too much voltage.
- On a computer, plug straight into the computer, not into a hub that cannot supply enough power.
- On a phone, make sure the battery is not low and power saving is off.
- Try another power bank or charger.

### Nothing Happens When I Plug It into My Phone

1. Push the T256S all the way in. A thick phone case can stop the plug from seating; remove the case and try again.
2. Some Android phones need **OTG** turned on in Settings, and some turn it off again after a while. Search Settings for "OTG".
3. If the camera screen is on but the phone shows nothing: with a camera app, make sure the app supports UVC and that you allowed USB access; with the web page, see "The Browser Cannot Open 192.168.17.1" below.

### Does It Work with iPhone and iPad

- **iPhone**: UVC cameras are not supported, so camera apps cannot see the T256S. iPhones with USB-C can open `192.168.17.1` in Safari to use the web page. The page does not open automatically; type the address.
- **iPad**: iPads with USB-C can show the image in a camera app that supports UVC, such as CamX - USB Camera.

See [Quick Start](./Quick_Start.html#iPad-and-iPhone).

### The Computer Does Not Show the Camera

1. Try another cable. Charge-only cables carry no data, so the computer sees nothing.
2. Try another USB port, preferably one on the computer itself.
3. On Windows, open Device Manager and look under "Cameras" or "Imaging devices". On Linux, run `lsusb` and look for a device with ID `359f:4201`.
4. Make sure no other program is using the camera. Only one program at a time can open a UVC camera.

### The Browser Cannot Open 192.168.17.1

Check the following in order:

1. The firmware must be 26.40.0 or later; older versions have no web page. See [Check the Firmware Version](./Advanced.html#Check-the-Firmware-Version).
2. The address is `192.168.17.1`, without `https://` in front.
3. Right after plugging in, wait a few seconds for the system to bring up the network.
4. **On Android, turn on airplane mode first.** Android ranks the USB network below Wi-Fi and mobile data, so the browser sends the request over Wi-Fi or mobile data and cannot reach the T256S. Turn on airplane mode, then enter the address. If Wi-Fi stays on in airplane mode, turn it off too. Turn airplane mode off when you are done.
5. **On a computer**, check that a new network adapter appeared with a `192.168.17.x` address. A `169.254.x.x` address means automatic setup failed; set the adapter to `192.168.17.100` with subnet mask `255.255.255.0` by hand.
6. If you changed the subnet, the address is `192.168.<subnet>.1`; see the next question.

### The Web Page Is Unreachable After a Subnet Change

The new address is `192.168.<your number>.1`. If you forgot the number, pull down from the top edge of the screen to open the status panel; the current address follows the `FW` version. See [Use Several Cameras on One Computer](./Advanced.html#Use-Several-Cameras-on-One-Computer).

### My Phone Says the Network Has No Internet Access

That is expected. The T256S provides a local network that only connects to your phone, so there is no internet. Stay connected.

## Screen and Image

### The Screen Looks Different from This Guide

This guide describes firmware 26.47.0. Older firmware (26.17.1 and earlier) shows a column of buttons on the right: tap the color button to change palettes, the round button to take a photo and the gallery button to view photos; long-press the round button to see the version. Older firmware has no web page or HTTP API, so we recommend [updating the firmware](./Advanced.html#Update-the-Firmware) to 26.47.0.

### Pulling Down or Swiping Up Does Nothing

Both gestures must start right at the screen edge. A swipe that starts in the middle of the image changes the palette instead. Also, close the status panel before you swipe up from the bottom for the gallery.

### The Text on the Screen Is Upside Down

Open the status panel and tap the rotate button. When `TAP AGAIN` appears, tap it once more. The buttons and text turn 180°; the thermal image itself does not rotate.

### The Image Is Upside Down on My Phone

With the T256S plugged into the bottom of a phone, the image is upside down relative to the phone:

- In a UVC camera app, rotate the image 180°, or turn on both horizontal and vertical mirroring.
- On the web page, tap the rotate button at the top.
- On an iPad, rotate the image in the camera app.

### The Camera Stream Is Still Upscaled After Turning Off SR

That is expected. The SR switch on the status panel only affects the screen. The UVC MJPEG stream is always the super-resolution image. On the web page, the SR button at the top switches between super resolution and the native image.

### The Image Pauses Briefly with a Faint Click

The thermal module is calibrating with its shutter (NUC). It closes an internal shutter from time to time to correct sensor drift as the temperature changes. The image pauses for a moment during calibration. This is normal.

### Super Resolution Helps More in Some Scenes

Super resolution enhances edges, lines and texture, such as board traces, component outlines and machine edges, so those scenes improve the most. Large flat areas at an even temperature, such as a white wall or a heat spreader, have little detail to enhance, so the change is small. To compare directly, use [Compare Super Resolution](./Quick_Start.html#Compare-Super-Resolution) on the web page.

### The Image Looks Noisy

- Right after power-on, wait 2 to 5 minutes for the camera to reach thermal equilibrium.
- The smaller the temperature difference between the target and its surroundings, the more visible the noise.
- High ambient temperatures, above about 40 °C, add thermal noise. Use the camera between 15 and 35 °C.

## Temperature

### Temperatures Look Wrong

Check the following:

- **Surface**: the T256S uses an emissivity of 0.95, which suits skin, plastic, circuit boards, walls and most other non-metal surfaces. Shiny metal, such as aluminum foil or stainless steel, reflects strongly and reads much too low. Put a small piece of black electrical tape or a spot of matte black paint on it, let it reach the object's temperature and measure that.
- **Distance and target size**: at 1 m, each pixel covers about 4 mm. A target that is too small blends with its surroundings. For accurate readings, measure from 0.2 to 1 m.
- **Reflections**: hot objects nearby, such as sunlight or a soldering iron, can reflect off the surface into the lens and raise the reading.
- **Warm-up**: readings drift right after power-on; wait about 2 minutes.
- **Macro lens**: readings are less accurate with the macro lens. Remove it when you need accurate numbers.

### What HI and LO on the Screen Mean

They show the current measurement range. **HI** is high gain, -15 to 150 °C, more accurate and the default. **LO** is low gain, 50 to 500 °C, for hotter scenes. The T256S switches to LO when more than a tenth of the image is above 130 °C, and back to HI once almost the whole image is below 110 °C. There is nothing to set. See [Read the Temperature](./Quick_Start.html#Read-the-Temperature).

### Can I Read Temperatures from the Colors

No. Palette colors only show relative heat, and every frame spreads the colors between its own coldest and hottest points. For numbers, use the temperatures on the screen or multi-point measurement on the web page.

### Videos Recorded from the Camera Have No Temperature Data

The UVC MJPEG image is already colored, so the colors no longer map to temperatures. For temperatures, use the UVC Y16 format at 192 × 256, or the HTTP API's `/frame.temp16` and `/api/v1/thermal`. Do not try to recover temperatures from a color image. See [UVC Output Formats](./Advanced.html#UVC-Output-Formats).

### How to Convert Y16 Values to Temperatures

`temperature (°C) = pixel value / 64 - 273.15`. The formula applies only to Y16 at 192 × 256. Y16 at 480 × 640 is an upscaled grayscale image, not temperatures. See [Read Temperatures from Y16](./Advanced.html#Read-Temperatures-from-Y16) for an example.

## Photos and Files

### Where Photos Taken on the Screen Are Stored

On the camera. Plug the T256S into a computer and open the new USB drive; the photos are in the `Gallery` folder, and their file names record the center, minimum and maximum temperatures. See [Photos and the USB Drive](./Advanced.html#Photos-and-the-USB-Drive).

### The Gallery Says GALLERY EMPTY

There are no photos on the camera yet. Tap the capture button to take one, then swipe up from the bottom edge to open the gallery. The update tool also erases all photos.

### Where Photos and Videos from the Web Page Are Saved

The browser saves them on the phone or computer you are using, usually in the Downloads folder. Photo names start with `thermal-`; videos are `thermal-record.mp4` or `.webm`. Nothing is stored on the T256S.

### Photos on the USB Drive Do Not Match the Screen

If you take or delete photos on the screen while the computer is using the USB drive, the two sides may show different contents. Eject the drive on the computer, then unplug and reconnect the T256S. From then on, eject the drive before you take or delete photos on the screen.

## Firmware and Development

### How to Check the Firmware Version

After 26.17.1: pull down from the top edge of the screen to open the status panel; the version follows `FW`. You can also find it under "Device settings & firmware" on the web page. On 26.17.1 and earlier: long-press the capture button on the screen. See [Check the Firmware Version](./Advanced.html#Check-the-Firmware-Version).

### How to Update the Firmware

On 26.17.1 and earlier, run the update tool on a computer, which goes straight to 26.47.0. After 26.17.1, update in the browser. Cameras on 26.17.1 or earlier cannot update in the browser. See [Update the Firmware](./Advanced.html#Update-the-Firmware).

### The Update Tool Cannot Find the Camera

- Check that the T256S is connected with a data cable and that its USB drive appears on the computer.
- Close programs that are using the drive, such as a window showing the `Gallery` folder, and try again.
- On Linux, run `./Linux/t256s-migrate info` to list candidate drives, and if needed run the tool again with `--mount <path>` pointing at the T256S drive.
- If the tool says the camera may still be converting, do not restart it. Wait a few minutes and check the version again.

### The Web Page Rejects the Firmware File

- Make sure you downloaded the T256S `.sysupgrade.bin` file and did not extract or rename it.
- The download may be incomplete; download it again.
- If the section says "USB migration required", the camera still uses the old single-slot system. [Run the update tool](./Advanced.html#Run-the-Update-Tool) first.

### The Screen Stays Black After an Update

The camera restarts several times during an update, so a black screen for a while is normal. Keep it powered and wait for the live image. If it stays black and will not start, contact support@sipeed.com.

### The Power Was Cut During an Update

Reconnect the power right away and wait for the camera to recover. Browser updates can roll back: if the new system fails to start, the camera returns to the previous version. The update tool has no power-loss protection, and the camera may not start afterwards. In that case, contact support@sipeed.com for repair and do not open the camera.

### Can I Read Temperatures from My Own Code

Yes. With the T256S plugged into a computer, it serves an HTTP API at `http://192.168.17.1`: `/api/v1/thermal` returns the center, hottest and coldest temperatures, `/frame.temp16` returns the raw temperature of every pixel, and `/frame.jpg` returns the color image. Python, Go, Node.js and shell scripts can all call it, and so can AI tools. See the [HTTP API](./API.md) and [AI Integration](./AI_Control.md).

### Which Firmware the Web Page and HTTP API Need

26.40.0 or later. Cameras on 26.17.1 or earlier should [run the update tool](./Advanced.html#Run-the-Update-Tool) to reach 26.47.0.

### Does It Work with Linux and Raspberry Pi

Yes. The T256S is a standard UVC camera and works with Linux (V4L2) without a driver. `guvcview`, `cheese`, `ffplay` and OpenCV can all open it. Its USB ID is `359f:4201`. The web page and HTTP API work on Linux too.

### The Camera Gets Warm

That is normal. The processor that runs super resolution produces heat, and the aluminum housing spreads it. Use the camera with some airflow and do not leave it in a closed, hot space for long periods.

## Still Stuck

Email support@sipeed.com with your phone or computer model, its system version, and the T256S firmware version.
