# Lichee 86 Panel

## Introduction

Lichee RV-86 Panel is a development kit designed for smart home central control scene. It's equipped with LicheeRV Core board (Allwinner D1 chip with 512MB ddr3), 4-inch touch IPS screen, Wifi+BT module, Ethernet, two digital silicon mic and GPIO expansion interface. For software it can use Linux OS (OpenWrt or Debian) and Ali WAFT (WAFT is a high-performance application research framework for AIoT based on WebAssembly and their own rendering engine)

![Basic board](./../assets/RV/86_2.png)

## Parameters
| Item                                                  | Value                                                                                                                                                                                                                                      |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Core board                                            | Sipeed LicheeRV Nezha compute bar                                                                                                                                                                                                          |
| Display                                               | Default Bundle for 4-inch 480\*480 standard definition IPS capacitive touch screen <br> Optional upgrade to 4-inch 720\*720 high definition IPS capacitive touch screen<br>Reserver 8-inch 1280\*800 IPS capacitive touch screen interface |
| Audio                                                 | Onboard 1W mini speaker, Dual digital silicon microphone                                                                                                                                                                                   |
| Network                                               | XR829 WIFI+BT wireless module <br>RTL8201F 100M Ethernet <br> Reserved RJ45 ethernet pad                                                                                                                                                   |
| USB                                                   | USB-C OTG interface on core board <br> Reserved USB-C HOST and USB-uart interface                                                                                                                                                          |
| Power                                                 | Support 5V,12V power supply (Onboard DC-DC )                                                                                                                                                                                               |
| Extension pins                                        | Double 2x8Pin 2.54mm Pin headers，Reserved FPCIO                                                                                                                                                                                           |
| Shell                                                 | Optional 86 panel 3D print shell，download 3D file [here](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV_86_panel/6_Shell_3D) source                                                                                                                                                                               |
| Dimension                                             | 86x86mm                                                                                                                                                                                                                                    |
| Usage situations                                      | Smart home center control unit，WAFT UI evaluation                                                                                                                                                                                         |
| Development framework                                 | Support WAFT (WebAssembly Framework For Things）runtime                                                                                                                                                                                    |
| Operating system                                      | Support OpenWRT and Debian                                                                                                                                                                                                                 |
| [Development resource](./user.html#bsp-sdk-develpoment) | Provide docker development image of the original SDK                                                                                                                                                                                       |

![Functions map](./../assets/RV/86_pin.png)

## Related links

[Download center](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV_86_panel)

[Burn image](./flash.md)

[Basic usage](./user.md)

## Support

Email to support@sipeed.com for business cooperation or leave message on this page for help.