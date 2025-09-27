---
title:  Hardware Operation
keywords: LogicAnalyzer, SLogic, basic usage, hardware
update:
  - date: 2025-09-25
    version: v0.1
    author: Serika
    content:
      - Release docs
---

This section introduces the usage and operation related to **SLogic16 U3** hardware.

## Hardware Overview

### Accessories List

![unboxing_0](./assets/DCIM/unboxing_0.png)

A complete hardware set includes the **SLoigc16 U3 main unit** and **accessories inside the package**, as shown below:
- <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>CSS Indentation</title>
    <style>
      .indent {
        margin-left: 0ch; /* wideof 0 characters */
      }
    </style>
  </head>
  <body>
    <details class="indent">
      <summary><font color="#4F84FF"><b>SLoigc16 U3 Main Unit</b> x1
  </font></summary>
      <img src="./assets/DCIM/15k_la_photo.png">
    </details>
  </body>
  </html>
- **Accessories inside the package:** (Note: Ribbon cable and coaxial cable module are mutually exclusive) 
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>2x6P Male-to-Female Ribbon Cable</b> x2
      </font></summary>
          <img src="./assets/DCIM/normal_cable.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>2x4P Coaxial Cable Module</b> x2
      </font></summary>
          <img src="./assets/DCIM/coaxial_cable.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>Logic Analyzer Test Clips</b> x16
      </font></summary>
          <img src="./assets/DCIM/testing_hook.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>0.5m A+C to C USB3 Data Cable</b> x1
      </font></summary>
          <img src="./assets/DCIM/usb3_cable.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>Stainless Steel SIM Pin</b> x1
      </font></summary>
          <img src="./assets/DCIM/small_pin.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>Instruction Card</b> x1
      </font></summary>
          <img src="./assets/DCIM/readme_card.jpg">
        </details>
      </body>
      </html>
    - <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>CSS Indentation</title>
        <style>
          .indent {
            margin-left: 0ch; /* wideof 0 characters */
          }
        </style>
      </head>
      <body>
        <details class="indent">
          <summary><font color="#4F84FF"><b>Zipper Storage Bag</b> x1
      </font></summary>
          <img src="./assets/DCIM/storage_bag.jpg">
        </details>
      </body>
      </html>

> The appearance of accessories may vary slightly between batches. Please refer to the actual product.

### Connection Method

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS Indentation</title>
  <style>
    .indent {
      margin-left: 0ch; /* wideof 0 characters */
    }
  </style>
</head>
<body>
  <details class="indent">
    <summary><font color="#4F84FF">Click here to view the hardware connection diagram of SLoigc16 U3
</font></summary>
    <img src="./assets/MISC/la_topview.jpg">
  </details>
  <br>
</body>
</html>

**Coaxial Cable Module**/**Ribbon cable set** are directional. The insertion direction is shown above: the triangle mark **▴** on the cable should align with the triangle mark **▾** on the case.

The far end of the **coaxial cable** has **2** terminals. The white terminal connects to the signal source, and the black terminal connects to GND.

Each group of **Ribbon cables** has only **2** separate GNDs. When the triangle mark **▴** on the cable aligns with the case, the black wire bundle is GND, and the red is VCC.

#### Rear of Logic Analyzer

![slogic16_u3_rear](./assets/MISC/la_rearview.jpg)

The rear of the logic analyzer is a **2x12P** female header with a 2.54mm pitch. The pin definition is shown above (rear view of the logic analyzer).

The digital numbers **0-15** are the sampling channel numbers, corresponding to the channel numbers in the host software, totaling 16 channels.

**G** stands for **GND**. Please connect the GND of the device under test and the logic analyzer, totaling 4 channels.

**VCC** stands for power output, with an output capacity of **3.3V @500mA**, totaling 2 channels (2 channels share the current output capacity).

**CK** stands for reserved sampling clock input/trigger output channels. This function is not yet implemented, totaling 2 channels.

#### Front of Logic Analyzer

![slogic16_u3_rear](./assets/MISC/la_frontview.jpg)

The above is the front view of the logic analyzer, from left to right:

**USB-C** interface standard is 3.2 Gen1 (5Gbps). To use the logic analyzer function, a cable with corresponding capability (USB3.0) must be used.

**MODE** small hole contains a hidden button. It can be pressed by inserting a SIM pin. Its function is described in the [MODE Button](#MODE-Button) section.

**ACT** is the **status indicator light**. Specific states are described in the [ACT Indicator](#ACT-Indicator) section.

---

### Getting Started

First, connect **PC USB3** → **USB-A/C to USB-C** → **SLogic** → **Ribbon cable**/**Coaxial Cable Module**

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS Indentation</title>
  <style>
    .indent {
      margin-left: 0ch; /* wideof 0 characters */
    }
  </style>
</head>
<body>
  <details class="indent">
    <summary><font color="#4F84FF">Click here to view the hardware connection of SLoigc16 U3
</font></summary>
    <img src="./assets/DCIM/SLogic16U3.jpg">
  </details>
  <br>
</body>
</html>

> Currently, SLogic16 only supports **USB3** mode. The included **USB-A/C to USB-C** cable is compatible.

Connect the signal points of the target device under test to any free CH digital port of **SLogic** via **Ribbon cable**/**Coaxial cable**, and ensure the GND of the device under test is connected to the GND of SLogic.

> Note: When the Nyquist frequency of the signal source is greater than or equal to 50 MHz, it is recommended to use coaxial cables for sampling to achieve better stability.

You may optionally use **logic analyzer test clips** to connect to the signal points.

> To improve sampling stability, the GND wire of SLogic should be as close as possible to the test point. Even shortening by **1 mm** may help. When using coaxial cables, it is recommended to connect the corresponding **GND** along with each sampled signal **CH**.

Finally, launch [**plusview**](./Software_User_Guide) to start acquisition.

For software installation and related operations, refer to [here](./Introduction#Software-installation).

---

## ACT Indicator

The **ACT indicator** is located on the front of the logic analyzer, near the outer side.

![slogic16_u3_rear](./assets/MISC/la_frontview_act.jpg)

### Colors & Functions

The indicator is a 3-color RGB LED. Each color represents a function, and combinations indicate device status.

| **Color**   | <span style="color:blue">Blue</span> | <span style="color:green">Green</span> | <span style="color:red">Red</span> |
| ----------- | ------------------------------------ | -------------------------------------- | ---------------------------------- |
| **Function**| Power                                | USB LINK indicator                     | Running status indicator           |

---

Normal operating states:

| **Status**       | **Color**                                                                 | **Notes**                                                                 |
| ---------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Normal Link**  | <span style="color:cyan">Cyan</span>                                      | <span style="color:blue">Blue</span> + <span style="color:green">Green</span> |
| **Data Transfer**| <span style="color:cyan">Cyan</span> + <span style="color:red">Red fast blink</span> | Blue + Green + Red fast blink |
| **DFU Mode**     | <span style="color:cyan">Cyan</span> + <span style="color:red">Red slow blink</span> | Blue + Green + Red slow blink |

---

Abnormal states:

| **Status**          | **Color**                         | **Notes**                              |
| ------------------- | --------------------------------- | -------------------------------------- |
| **USB Link Fail**   | <span style="color:blue">Blue</span> | Only blue light on                     |
| **Flash Load Error**| <span style="color:red">Red</span> | Only red light on                      |

- Other states (e.g., only green on / all three on) are undefined.
- If undefined states occur, try re-plugging USB. If unresolved, suspect hardware damage.

> ⚠ Note: If the <span style="color:green">green light</span> goes off at any time, it means USB connection failed. Reconnect to resolve. The <span style="color:red">red light</span> status is irrelevant in this case.

---

### Troubleshooting

- **Checklist: <span style="color:blue"><b>Only blue light</b></span>**
  - USB cable does not support **USB3** (common with phone charging cables)
  - PC USB port does not support **USB3**
  - Connected to front panel USB of desktop PC
  - Connected to incompatible **USB hub** (always connect SLogic directly to PC USB)
  - Connected to insufficient power USB port
  - Cable too long (use ≤1 m cable)

- **Checklist: <span style="color:red"><b>Only red light</b></span>**
  - Poor quality USB cable, excessive voltage drop
  - PC USB port fault: fuse aging, insufficient power
  - SLogic hardware damage → keep device powered off and contact support

---

## MODE Button

The **MODE button** is on the front of the logic analyzer, between the **USB-C connector** and **ACT indicator**. It is hidden and requires a SIM pin to press.

![slogic16_u3_rear](./assets/MISC/la_frontview_mode.jpg)

When powered on, the default function is **Logic Analyzer**. Normally, the [ACT indicator](#ACT-Indicator) shows cyan.  
A new **USB3** device appears: **SLogic16 U3** (logic analyzer).

**Pressing the MODE button** switches function. After switching, the indicator changes: red slow blink.  
A new **USB2** device appears: **SLogic DFU** (upgrade mode).

> **SLogic** mode uses **USB3**, while **DFU** mode uses **USB2**.

Pressing **MODE** again switches back to **SLogic16 U3**. Repeatedly pressing **MODE** cycles between **SLogic DFU** and **SLogic16 U3**.

> In Windows, open Device Manager or use *USB treeview*.  
> In Linux/macOS, use the *lsusb* command.  
> You will find the device listed as "*SLogic16 U3*" or "*SLogic DFU*".

---

## Firmware Update

First, [enter DFU MODE](#MODE-Button): after powering on, press the **MODE button** and wait until the <span style="color:red">red light blinks slowly</span>.

Confirm that the "*SLogic DFU*" device appears, then use the **DFU Tool** to perform the update.

> In Windows, open Device Manager or use *USB treeview*.  
> In Linux/macOS, use *lsusb*.  
> You should see "*SLogic DFU*" listed.

Detailed instructions for the DFU tool are provided below.

> In principle, OTA operations only update the SLogic firmware and do not affect the **DFU** function.  
> Even if OTA fails, the device will remain locked in **DFU** mode until the SLogic firmware is successfully updated.

Firmware updates are provided via a Python/PyQt GUI tool.

- [Firmware update tool repository](https://github.com/sipeed/slogic16u3-tools)

### **Update steps:**
1. Run the GUI tool:
2. Press the **mode** button on the device. The GUI should display "SLogic16U3 OTA".
3. Select the firmware file in the GUI.
4. Click **OTA** to start the update.
5. Wait for completion and follow on-screen instructions.

> **Note:** A binary version of the update tool will be released soon.

![](../../../en/logic_analyzer/slogic16u3/assets/Screenshots/Screenshot_2025-09-25_15-34-06.png)


---

## Safety & Precautions

- **SLogic** ***VCC*** is a **power output**. The two ***VCC*** ports share the same power rail.  
  Output capability: ***3.3V @ 500 mA MAX***
- **Never** short ***VCC*** directly to ***GND***, to avoid overcurrent or short circuit.
- **SLogic** has built-in overcurrent protection. However, for safety, avoid short circuits, as the host PC’s USB port overcurrent protection may vary.
- When **SLogic** is used with a computer powered by mains electricity, its ground is connected to the computer’s ground.  
  To protect both the device and the host, connect probe grounds only to equipotential ground points.  
  **Never** connect to hot ground or mismatched potential points.
