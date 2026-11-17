# T256s FAQ

This document summarizes common issues and troubleshooting methods encountered during the use of the T256s, covering power supply, imaging, temperature measurement accuracy, and software updates.

## Power & Startup

### Q: The screen keeps rebooting, stays black, or flickers when connected to a phone or PC.

**A:** This is typically caused by an **insufficient power supply**.

- When the T256s enables AI Super-Resolution (SR), the internal NPU (Neural Processing Unit) operates at high load, requiring a stable current.
- Some smartphones have limited OTG output, or the use of low-quality cables with high internal resistance can cause instantaneous voltage drops, triggering a device reset.
- **Recommendation:** Use a high-quality standard Type-C data cable. Prioritize connecting to a PC's rear USB 3.0 port or a high-capacity power bank. If using a phone, ensure the battery is sufficiently charged and "Power Saving Mode" is disabled.

### Q: The device does not respond at all after connecting to a phone.

**A:** Please follow these troubleshooting steps:

1. **Enable OTG:** Some brands (e.g., OPPO, vivo, OnePlus) require you to manually enable "OTG Connection" in System Settings; it may automatically turn off after 10 minutes of inactivity.
2. **Permission Authorization:** Upon insertion, the phone should prompt for "Allow the app to access the USB device." Please check "Always allow."
3. **UVC Support:** Ensure your phone runs Android 9.0 or higher and use UVC-compatible software (such as the official Sipeed app).
4. **Cross-Verification:** Test the device on a PC or another smartphone to rule out compatibility issues specific to a single mobile terminal.

### Q: The device does not respond after connecting to an iPhone?

**A:** iPhone does not support UVC preview. Use an iPad or an Android device.


## Display & Imaging

### Q: The image is upside down and the controls are reversed after connecting the device to my phone. What should I do?

A: Due to the orientation of the device interface, you need to enable both "Vertical Flip" (Upside Down) and "Horizontal Flip" (Mirroring) after connecting to ensure the display matches the device's physical orientation.


### Q: The image freezes briefly accompanied by a faint mechanical "clicking" sound.

A: This is the **Non-Uniformity Correction (NUC)** process, also known as "shutter calibration." The thermal module periodically closes an internal shutter to calibrate the sensor and compensate for drift caused by temperature changes. The momentary image freeze is a normal part of the operating mechanism.

### Q: The image has noticeable noise, or the SR detail is not sharp enough.

A: AI Super-Resolution (ISR) performance is affected by the environment and target characteristics:

- **Ambient Temperature:** If the ambient temperature is too high (e.g., above 40°C), thermal noise increases significantly, affecting image purity. Recommended usage is between 15°C and 35°C.
- **Warm-up:** Thermal sensitivity reaches its peak only after the device stabilizes. It is recommended to let it run for 2–5 minutes to reach thermal equilibrium.
- **Contrast:** The smaller the temperature difference between the target and the background, the more apparent the noise will be.

## Super-Resolution (SR) Boundary Conditions

### Q: Why is the SR effect very obvious in some scenes but barely noticeable in others?

A: The AI Super-Resolution (ISR) algorithm is based on deep learning to enhance edge details. Its performance depends on scene features:

- **Ideal Scenarios:** Objects with distinct edges, lines, or complex textures (e.g., PCB traces, electronic component outlines, mechanical parts, or text). In these cases, SR significantly sharpens edges and reduces pixelation.
- **Limited Scenarios:** Large areas of uniform temperature lacking texture (e.g., flat white walls, smooth heat sinks, or the sky). Since there are no features to enhance, the visual improvement is minimal.
- **Recommendation:** To evaluate SR performance, point the device at targets with rich temperature gradients or geometric structures.

## Temperature Accuracy

### Q: How do I convert raw Y16 data to Celsius?

A: The conversion formula is: `$Celsius = (Y16\_Value / 64.0) - 273.15$`. Note that accurate readings require the device to reach thermal equilibrium (approx. 2 minutes after power-on).

### Q: Why is there a deviation between the measured value and the actual temperature?

A: Infrared temperature accuracy is subject to interference from several physical factors:
1. **Macro Lens:** Direct impact. The addition of a macro lens introduces variable interference during infrared signal transmission and reception, leading to inherent measurement errors.
2. **Emissivity:** A critical factor. Different materials have varying capacities to radiate infrared energy. Shiny metal surfaces (e.g., aluminum foil, stainless steel) have extremely low emissivity; measuring them directly will result in incorrect "reflected temperatures." It is recommended to apply electrical tape or matte black paint to the target metal surface before measurement.
3. **Measurement Distance:** As distance increases, the physical area covered by a single pixel expands, leading to the **"Size-of-Source Effect" (SSE)**. For precision thermography, a range of 0.2m to 1.0m is recommended. For ultra-close-up shots, a dedicated macro lens must be used.
4. **Environmental Reflection:** If high-temperature objects (e.g., sunlight, soldering irons) are nearby, their radiation may reflect off the target surface into the sensor, causing inflated temperature readings.
5. **Atmospheric Compensation:** For long-distance measurements, water vapor and $CO_2$ in the air absorb infrared energy. While the T256s is primarily designed for near-field analysis (where atmospheric impact is minimal), compensation settings in professional software may be required for specialized use.

## Software and Firmware Update

### Q: The software recognizes the device, but the video stream won't open.

A: 1. Ensure no other programs are occupying the UVC camera; 2. Try manually switching the resolution to 640x480; 3. Check if the system driver identifies it as "T256s" or "USB Camera."

### Q: How do I update the firmware?

A: Systems on 26.17.1 or earlier run the upgrade script, which updates the device to 26.47.0; systems after 26.17.1 update on the device web page. See [System Update](System_Update.md) for steps.

### Q: How do I check the current version number?

A: On 26.17.1 or earlier, hold the capture button to display the version. After 26.17.1, swipe down from the top edge of the screen to open the status panel, which shows `FW` and the version; you can also expand "Device settings & firmware" at the bottom of the web page and read the "Firmware" entry.

## Miscellaneous

### Q: Is it normal for the device to get quite hot?

A: Yes. The T256s integrates a high-performance AI processing chip which generates heat during operation. The housing is designed to act as a heat sink. Ensure use in a well-ventilated area and avoid prolonged use in enclosed, high-temperature environments.

### Q: Can I use it with Linux or Raspberry Pi?

A: Yes. T256s follows the standard UVC protocol and supports Linux (V4L2). On Ubuntu or Raspberry Pi, it can be accessed directly using `cheese`, `guvcview`, or OpenCV. Please run this as the root user. The VID/PID is typically `359f:4201`.

## Development and API

### Q: Can I read temperatures from a program instead of watching the video?

A: Yes. Besides the UVC camera, the T256s also enumerates a USB network adapter. The camera serves an HTTP API at `http://192.168.17.1`: `/api/v1/thermal` returns center, maximum and minimum temperatures, `/frame.temp16` returns per-pixel raw temperatures, and `/frame.jpg` returns a colorized frame. Python, Go, Node and shell all work, and it is a good fit for AI agents. See the [HTTP API Reference](API.md), and [Controlling the Camera with AI](AI_Control.md) for the AI side.

### Q: What firmware version do web access and the HTTP API require?

A: The live web image and the HTTP API need firmware 26.40.0 or later; web update is supported after 26.17.1. See [System Update](System_Update.md) for checking the version and upgrading. Keep the camera powered during the upgrade and do not unplug it.

### Q: The built-in web page shows temperatures, but my recording has no temperature data. Why?

A: UVC video and the HTTP API are separate channels. The UVC MJPEG stream is already colorized, so pixel colors no longer map to temperatures; only the Y16 stream carries raw values. For accurate temperatures use HTTP TEMP16 or `/api/v1/thermal` instead of inferring them from the colored picture.
