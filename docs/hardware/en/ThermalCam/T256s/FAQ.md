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
## Display & Imaging

### Q: The image freezes briefly accompanied by a faint mechanical "clicking" sound.

A: This is the **Non-Uniformity Correction (NUC)** process, also known as "shutter calibration." The thermal module periodically closes an internal shutter to calibrate the sensor and compensate for drift caused by temperature changes. The momentary image freeze is a normal part of the operating mechanism.

### Q: The app displays "No Signal" or a black screen with no thermal image.

A: Check the physical connection. If the connection is secure but there is still no image, the module may have failed to initialize or the driver is occupied. Try re-plugging the device. If the following prompt persists, please contact technical support:

![占位图](../../../en/ThermalCam/T256s/assets/no-image-signal.jpg)

### Q: The image has noticeable noise, or the SR detail is not sharp enough.

A: AI Super-Resolution (ISR) performance is affected by the environment and target characteristics:

- **Ambient Temperature:** If the ambient temperature is too high (e.g., above 40°C), thermal noise increases significantly, affecting image purity. Recommended usage is between 15°C and 35°C.
- **Warm-up:** Thermal sensitivity reaches its peak only after the device stabilizes. It is recommended to let it run for 2–5 minutes to reach thermal equilibrium.
- **Contrast:** The smaller the temperature difference between the target and the background, the more apparent the noise will be.

---

## Super-Resolution (SR) Boundary Conditions

### Q: Why is the SR effect very obvious in some scenes but barely noticeable in others?

A: The AI Super-Resolution (ISR) algorithm is based on deep learning to enhance edge details. Its performance depends on scene features:

- **Ideal Scenarios:** Objects with distinct edges, lines, or complex textures (e.g., PCB traces, electronic component outlines, mechanical parts, or text). In these cases, SR significantly sharpens edges and reduces pixelation.
- **Limited Scenarios:** Large areas of uniform temperature lacking texture (e.g., flat white walls, smooth heat sinks, or the sky). Since there are no features to enhance, the visual improvement is minimal.
- **Recommendation:** To evaluate SR performance, point the device at targets with rich temperature gradients or geometric structures.

---

## Temperature Accuracy

### Q: How do I convert raw Y16 data to Celsius?

A: The conversion formula is: `$Celsius = (Y16\_Value / 64.0) - 273.15$`. Note that accurate readings require the device to reach thermal equilibrium (approx. 2 minutes after power-on).

### Q: Why is there a deviation between the measured value and the actual temperature?

A: Infrared accuracy is affected by several physical factors:
1. **Emissivity:** The most critical factor. Different materials radiate infrared energy differently. Shiny metal surfaces (e.g., aluminum foil, stainless steel) have extremely low emissivity; measuring them directly will result in incorrect reflected temperatures. Apply electrical tape or matte black paint to the metal surface before measuring.
2. **Measurement Distance:** As distance increases, a single pixel covers a larger physical area, leading to the "Size-of-Source Effect." For precision, keep the distance between 0.2m and 1.0m. Use a dedicated macro lens for close-up analysis.
3. **Environmental Reflection:** High-temperature objects nearby (e.g., sunlight, soldering irons) can reflect off the target surface into the sensor, causing inflated readings.
4. **Atmospheric Correction:** For long-distance measurements, water vapor and $CO_2$ absorb infrared energy. While T256s is designed for near-field analysis where this is negligible, professional software may offer compensation settings.
## Software & Firmware Updates

### Q: The software recognizes the device, but the video stream won't open.

A: 1. Ensure no other programs are occupying the UVC camera; 2. Try manually switching the resolution to 640x480; 3. Check if the system driver identifies it as "T256s" or "USB Camera."

### Q: How do I update the firmware for better AI capabilities?

A: T256s supports OTA updates via a PC firmware upgrade tool. Please visit the Sipeed Download Station for the latest firmware packages. Do not disconnect power during the upgrade. If an upgrade failure causes a boot loop (stuck on Logo), refer to the official "Blind Flash" recovery tutorial.

## Miscellaneous

### Q: Is it normal for the device to get quite hot?

A: Yes. The T256s integrates a high-performance AI processing chip which generates heat during operation. The housing is designed to act as a heat sink. Ensure use in a well-ventilated area and avoid prolonged use in enclosed, high-temperature environments.

### Q: Can I use it with Linux or Raspberry Pi?

A: Yes. T256s follows the standard UVC protocol and supports Linux (V4L2). On Ubuntu or Raspberry Pi, it can be accessed directly using `cheese`, `guvcview`, or OpenCV. Please run this as the root user. The VID/PID is typically `359f:ffff`.