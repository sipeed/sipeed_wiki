---
title: How to Reset Password for NanoKVM
keywords: NanoKVM, Remote desktop, RISCV, tool
---

> Document Scope
> Applicable to NanoKVM Cube/Lite/PCIe series
> Password reset feature is available in APP version 2.1.5 and above

## When to Reset Password

Use the password reset function when you forget the login password for the web management interface and cannot retrieve it through other means.

## How to Reset Password

With the device powered on, press and hold the `BOOT` button (next to the USB-HID interface for Cube version, on the panel for PCIe version) for **more than 10 seconds**. The device will automatically reset the password.

## Default Password After Reset

After password reset, the default credentials for the web management interface are:
- **Username**: `admin`
- **Password**: `admin`

> **Note**: Resetting the password only affects the web management interface login password, not the SSH login password. If you need to modify the SSH password, use the `passwd` command after logging in.
