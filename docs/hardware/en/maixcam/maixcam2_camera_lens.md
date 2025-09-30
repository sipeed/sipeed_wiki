---
title: MaixCAM2 – Camera and Lens Selection & Usage
---

## Camera Sensors Officially Supported by MaixCAM2

| Parameter \ Model | OS04D10                                                                                         | SC850SL                                | OS04A10                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------------------- |
| Resolution & FPS  | 2568x1448\@30fps (2K / 4MP)                                                                     | 3856x2176\@60fps (10bit) (4K / 8MP)    | 2688x1520\@30fps (2K / 4MP)                                |
| Pixel Size        | 1.998µm x 1.998µm                                                                               | 2.0µm x 2.0µm                          | 2.9µm x 2.9µm                                              |
| Sensor Size       | 5130.864µm x 2893.104µm                                                                         | -                                      | 7841.6µm x 4454.4µm                                        |
| Lens Size         | 1/3"                                                                                            | 1/1.8"                                 | 1/1.79"                                                    |
| Output Format     | 10bit RAW RGB                                                                                   | 12/10/8bit RAW RGB                     | 16/12/10bit RAW RGB                                        |
| Shutter Type      | Rolling Shutter                                                                                 | Rolling Shutter                        | Rolling Shutter                                            |
| CRA               | 12°                                                                                             | 9°                                     | 9°                                                         |
| Max Exposure      | 0.5s                                                                                            | -                                      | 45s                                                        |
| Dynamic Range     | -                                                                                               | Linear mode 75dB<br>WDR mode > 100dB   | >120dB (2x/3x staggered HDR)                               |
| SNR               | -                                                                                               | 39dB                                   | -                                                          |
| Sensitivity       | -                                                                                               | 5034 mV/lux·s                          | 32,000 e-/Lux-sec (green pixel @ 530nm illumination)       |
| Operating Temp    | -30°C \~ 85°C<br>Optimal -20°C \~ 60°C                                                          | -30°C \~ 85°C<br>Optimal -20°C \~ 60°C | -30°C \~ 85°C                                              |
| Application       | Lower resolution, lower heat, good image quality, suitable for general AI detection/recognition | High resolution & clarity, higher heat | High-quality imaging, color night vision, HDR, higher heat |

> `-` = not listed in datasheet or not tested.

More sensor datasheets can be found on the [download site](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2/Hardware/sensors).

## Lens and Mount Parameters & Replacement

Each official camera module comes with a standard M12 lens.
Note: Lens parameters vary by sensor. If you want to purchase different lenses, use the sensor specs above and the reference lens table below.

Datasheets for more lenses and mounts are available at the [download site](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2/Hardware/sensors).
⚠️ Actual lenses may differ slightly from the datasheet (e.g. OS04D10 and SC850SL default lenses don’t use `650 IR-Cut` even though listed). Always go by actual parts.

### Lenses

#### Official MaixCAM2 Kit Lenses

![SC850SL Lens](../../assets/maixcam/cam_len.png)

| Parameter \ Model | OS04D10                 | SC850SL                       | OS04A10                      |
| ----------------- | ----------------------- | ----------------------------- | ---------------------------- |
| Interface         | **M12**                 | **M12**                       | **M12**                      |
| Diameter          | 12mm                    | 12mm                          | 12mm                         |
| Thread Pitch      | 0.5mm                   | 0.5mm                         | 0.5mm                        |
| FOV               | H 90°<br>V 81°<br>D 90° | H 86.7°<br>V 48.8°<br>D 99.5° | H 88°<br>V 49.9°<br>D 100.2° |
| Distortion        | None                    | -25.6%                        | -25.6%                       |
| IR-Cut            | None                    | None                          | None                         |
| Lens Size         | **1/3"**                | **1/1.8"**                    | **1/1.8"**                   |
| CRA               | 12°                     | 16.2°                         | 16.2°                        |
| TTL               | -                       | 22.28±0.2mm                   | 22.28±0.2mm                  |
| Focal Length      | **3.05mm**              | **4.9±5%mm**                  | **4.9±5%mm**                 |
| Back Focal Length | 3.1mm                   | 6.41±0.2mm                    | 6.41±0.2mm                   |
| Flange Distance   | 3.1mm                   | **6.17±0.2mm**                | **6.17±0.2mm**               |
| F-Number          | 2.5                     | 1.65±10%                      | 1.6±10%                      |
| Lens Elements     | 2G2P                    | 4G4P                          | 4G4P                         |
| Resolution Std.   | 4MP                     | 8MP                           | 4MP                          |

### Focusing

Default M12 lenses are **manual focus**.
If the image looks blurry, rotate the lens until focus is achieved.
Some lenses include a **lock ring**—loosen it before adjusting focus, then tighten it to secure.

### Zoom

Default M12 lenses are **fixed focal length**—they support focusing (sharpness) but not zooming (optical magnification). If needed, purchase an **M12 zoom lens**, referencing the specs above.

### Replacing the Lens

Choose another **M12-compatible** lens.
Important factors: **lens length**, **mount height**, and **focal length**.

To ensure proper focus:

1. **Focus before bottoming out:** Sensor-to-lens distance (at screw-in) must ≤ flange distance. Otherwise, it can’t focus.
2. **Focus before falling out:** When focusing on close objects, lens may need to move outward (`v_d`). Ensure flange + `v_d` < mount height, or the lens will slip out before focusing.

> If unsure, provide your sensor + mount specs to the lens vendor for confirmation.

### Mounts

![](../../assets/maixcam/cam_len_base.png)

Mounts are generally **not replaceable** (glued to PCB). Choose lenses that fit the existing mount.

| Parameter \ Model | OS04D10          | SC850SL                         | OS04A10                         |
| ----------------- | ---------------- | ------------------------------- | ------------------------------- |
| IR-Cut            | **650nm IR-Cut** | **650nm IR-Cut**                | **650nm IR-Cut**                |
| Height            | **12mm**         | **13mm<br>(12mm + 1mm spacer)** | **13mm<br>(12mm + 1mm spacer)** |

* **IR-Cut:** Filters infrared. If you need IR capture, you must remove or replace the filter (not easy).

## Can I Replace the Sensor?

In theory, yes.
Official sensors are already tuned and plug-and-play.
If you want a new sensor, you’ll need **sensor driver integration** experience and **ISP tuning**. The process is complex and **not covered in this doc**.

## Real-World Camera Comparisons

TODO:

