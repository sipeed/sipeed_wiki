---
title: MS-T160 FAQ
keywords: MaixSense, Thermal, MS-T160, T160, thermal camera, FAQ, OTG, 192.168.17.1, temperature
update:
  - date: 2026-11-18
    version: v0.1
    author: Sipeed
    content:
      - Initial release covering connection, the web page, temperature, firmware and settings
      - Use airplane mode when an Android phone cannot open the page, and cover iPad
---

# FAQ

## Connection

### Nothing happens when I plug it into my phone

Check in order:

1. The T160 is fully inserted. A thick phone case can block the plug, so try without the case.
2. Some Android phones need the **OTG** switch turned on in Settings, and some turn it off again after a while. Search Settings for "OTG".
3. iPhones must have a USB-C port. Lightning iPhones are not supported.

### No "Sign in to network" notification appears

That is normal. The phone's system decides whether to show it, and many phones and all computers never do.

- **Android phones**: turn on airplane mode first, then open a browser and enter `192.168.17.1`. The reason is under "The browser cannot open 192.168.17.1" below.
- **iPhone, iPad and computers**: open a browser and enter `192.168.17.1`.

See Open the Web Page in the [Quick Start](./Quick_Start.md) for the full steps.

### My phone says "No internet access"

That is normal. The T160 is a local network that only connects to your phone, so it never has internet. Stay connected; nothing needs fixing.

### The browser cannot open 192.168.17.1

Check in order:

1. The address is `192.168.17.1` without `https://` in front.
2. Right after plugging in, wait a few seconds for the system to set up the network.
3. **On Android, turn on airplane mode first.** Android ranks a USB network adapter below Wi-Fi and mobile data, so the browser sends its requests over those and cannot reach the T160. Enter the address after turning on airplane mode; if Wi-Fi stays on in airplane mode, turn it off too. Turn airplane mode off again when you are done.
4. On a computer, check that a new wired network adapter appeared with a `192.168.17.x` address.
5. If you changed the subnet, the address is `192.168.<subnet>.1`; see [Use several devices on one computer](./Advanced.md).

### No new network adapter appears on my computer

Check that:

- Another USB-C port works. Plug in directly rather than through an unreliable dock.
- On Windows, Device Manager shows a new device under Network adapters.
- On Linux, `ip addr` shows a new interface with a `192.168.17.x` address.

### Which iPhones and iPads are supported?

iPhones with a USB-C port (iPhone 15 and later) and iPads with a USB-C port. Lightning models are not supported.

## Using the Web Page

### Super resolution did not turn on, or turned itself off

The page measures how fast super resolution runs in your browser and turns it off when it is too slow, to keep the image smooth. Tap **SR** to turn it on manually.

For the fastest super resolution, use Chrome 114, Firefox 146 or later. See Super Resolution and Comparison in the [Quick Start](./Quick_Start.md).

### The Compare button does not respond

Compare needs super resolution. Tap **SR** to turn it on, and Compare becomes available.

### The image is upside down

Tap the rotate button at the right of the status bar. Each tap turns the image 90° clockwise until it is upright, and the browser remembers the angle. When you turn a phone or tablet, the image already follows on its own.

### Does super resolution need the internet?

No. The super resolution model and the web page are both stored on the T160 and run locally. It works with no internet at all.

### Where are my photos and videos?

The browser saves them on the phone or computer you are using, with file names starting with `T160_`. On Android they usually go to Downloads; on a computer, to the browser's download folder. The T160 stores nothing.

### With two pages open, one shows no image

The T160 streams to only one connection at a time, and a newly opened page takes over from the old one. Keep only one page open.

## Temperature

### The temperature reading looks wrong

Check these points:

- **Surface**: the T160 calculates temperature with an emissivity of 0.95, which fits most non-metal surfaces such as skin, plastic, PCBs and walls. Shiny metal reflects a lot and reads clearly low. Stick a small piece of black electrical tape on the spot, wait for it to match the object's temperature, and measure the tape.
- **Target size**: at 1 m, each T160 pixel covers about 3.7 mm. A target smaller than that blends with its surroundings, so move closer.
- **Range**: the T160 measures 0 to 120 °C. Readings outside this range are not accurate.
- **Environment**: use it at room temperatures of 10 to 30 °C. After moving it from a cold or hot place, wait a few minutes before measuring.

### Do the colors show the temperature?

No. Colors only show what is warmer or cooler in the current image, and the range adjusts every frame. For values, read the H, L and C markers.

### Where is the center temperature measured?

The center temperature (C) covers a 5 × 5 pixel area in the middle of the image. Put the object you want to measure in the center.

## Firmware and Settings

### How do I check the firmware version?

Expand the **Device settings & firmware** panel at the bottom of the page. The Firmware update section shows the version; see [Advanced Use and Development](./Advanced.md).

### The firmware update failed

Keep the T160 connected, choose the firmware file again and tap **Install update** once more. During the update, do not unplug the device, close the page or let the phone lock. If the device stops responding after an interrupted update, contact support@sipeed.com.

### The page will not open after I changed the subnet

The new address is `192.168.<your number>.1`. If you forgot the number, look up the IP of this USB network adapter on the computer: if it is `192.168.N.x`, the device is at `192.168.N.1`. See [Use several devices on one computer](./Advanced.md).

### My custom web page broke and the page will not load

Open `http://192.168.17.1/builtin`; the built-in page always works there. Then tap **Restore built-in page** in the **Device settings & firmware** panel.

## Still Stuck?

Email support@sipeed.com with your phone or computer model, system version, browser version and the firmware version shown on the page.
