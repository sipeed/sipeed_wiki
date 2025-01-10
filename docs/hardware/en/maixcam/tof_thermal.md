---
title: ToF/Thermal PMOD
---

## PMOD_Thermal32

The PMOD_Thermal32 module is a low-cost thermal imaging module compliant with the PMOD interface standard. It can be directly inserted into the PMOD slot of the MaixCAM Pro and combined with a visible light camera to achieve dual-light fusion functionality.

| **Module Name** | PMOD_Thermal32      |
|------------------|---------------------|
| **Resolution**   | 32x24              |
| **Temperature Range** | -40°C to 450°C  |
| **Field of View (FOV)** | 55° x 35°     |
| **Frame Rate**   | 1~30fps            |
| **Interface**    | I2C                |

PMOD_Thermal32 Installation Guide  
![PMOD_Thermal32 Installation](../../assets/maixcam/pmod_thermal32.jpg)

Thermal Imaging with Pseudo-color Display  
![Pseudo-color Thermal Imaging](../../assets/maixcam/th32_1.jpg)

Thermal Imaging + Visible Light Fusion Display  
![Thermal + Visible Light Fusion](../../assets/maixcam/th32_2.jpg)

Reference Code:  
[GitHub Repository](https://github.com/sipeed/MaixPy/tree/main/examples/ext_dev/sensors/thermography_mlx90640)

---

## PMOD_TOF100

The PMOD_TOF100 module is a low-cost array ToF module compliant with the PMOD interface standard. It can be directly inserted into the PMOD slot of the MaixCAM Pro and combined with a visible light camera to achieve dual-light fusion functionality.

| **Module Name** | PMOD_TOF100         |
|------------------|---------------------|
| **Resolution**   | 100x100, 50x50, 25x25 |
| **Measuring Range** | 0.2~2.5m         |
| **Field of View (FOV)** | 70°H x 60°V   |
| **Laser Emitter** | 940nm VCSEL       |
| **Frame Rate**    | 100x100: 6fps, 50x50: 22fps, 25x25: 30fps |
| **Interface**     | SPI                |

PMOD_TOF100 Installation Guide  
![PMOD_TOF100 Installation](../../assets/maixcam/pmod_tof100.jpg)

Depth Imaging with Pseudo-color Display  
![Pseudo-color Depth Imaging](../../assets/maixcam/tof100_1.jpg)

Depth + Visible Light Fusion Display  
![Depth + Visible Light Fusion](../../assets/maixcam/tof100_2.jpg)

Reference Code:  
[GitHub Repository](https://github.com/sipeed/MaixPy/tree/main/examples/ext_dev/sensors/tof_opns303x)
