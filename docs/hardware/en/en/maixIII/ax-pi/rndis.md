---
title: RNDIS
tags: rndis
update:
  - date: 2022-12-23
    version: v0.1
    author: wonder
    content:
      - Create file
---

This essay just tells how to fix the RNDIS error in windows device manager.

![rndis_error_device](./assets/flash_system/rndis_error_device.jpg)

## RNDIS interduction

Visit [Introduction to Remote NDIS (RNDIS)](https://learn.microsoft.com/en-us/windows-hardware/drivers/network/remote-ndis--rndis-2?source=recommendations) to know more.

## Steps

Right click the error RNDIS device and choose Update driver

![rndis_update_driver](./assets/rndis/rndis_update_driver.png)

Choose the `Browse my computer for drivers`

![rndis_broswer_driver](./assets/rndis/rndis_broswer_driver.jpg)

Choose where the arrow points at

![rndis_pick_driver](./assets/rndis/rndis_pick_driver.jpg)

Network adapter

![rndis_net_adapter](./assets/rndis/rndis_net_adapter.jpg)

Compatible Device

![rndis_compatible_device](./assets/rndis/rndis_compatible_device.jpg)

Then there is no error on the RNDIS device

![rndis_no_error](./assets/rndis/rndis_no_error.jpg)