---
title: Update Application
keywords: NanoKVM Go, Remote desktop, KVM, update
update:
    - date: 2026-07-15
      version: v0.1
      author: Liang Ziyue
      content:
          - Add NanoKVM Go application update guide
---

NanoKVM Go supports updating the application from the web control page. Before updating, make sure the device is connected to the network and has obtained an IP address.

## Preparation

Before updating, confirm the following:

- NanoKVM Go has booted normally;
- NanoKVM Go is connected to a network with Internet access;
- NanoKVM Go has obtained an IP address through DHCP or static IP configuration;
- the computer and NanoKVM Go are on mutually reachable networks;
- the browser can open the NanoKVM Go web control page.

## Open the Control Page

1. Open a browser.
2. Enter the NanoKVM Go IP address in the address bar.
3. Open the NanoKVM Go web control page.
4. If the page asks you to log in, log in first.

## Open the Settings Page

On the top menu bar of the control page, click `Settings` to open the settings page.

![NanoKVM Go Settings button](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_settings_button.webp)

## Check for Updates

On the settings page, click `Check for updates`.

![NanoKVM Go check for updates page](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_check_update.webp)

If an update is available, a confirmation dialog is displayed. Click `OK` to start the update.

![Confirm the NanoKVM Go application update](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_confirm_update.webp)

## Wait for the Update to Complete

After clicking OK, keep NanoKVM Go powered on and connected to the network, then wait for the application update to complete.

![NanoKVM Go application update progress](../../../../assets/NanoKVM/go/system/nanokvm_go_updating_progress.webp)

Do not power off the device during the update, and do not refresh or close the page. After the update is complete, follow the instructions on the page. If the page refreshes automatically or returns to the login page, log in again.

## Update Complete

After the update is complete, you can continue accessing NanoKVM Go from the browser and use the remote control functions normally.
