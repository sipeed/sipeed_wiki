---
title: Tailscale
keywords: Tailscale, remote access, NAT traversal
---

# Configure Tailscale

## Introduction to Tailscale

Tailscale is a WireGuard-based mesh networking tool. It can add NanoKVM Go, computers, phones, and other devices to the same virtual LAN, allowing you to access NanoKVM Go remotely without a public IP address or router port forwarding.

After joining a Tailscale network, each device receives a virtual IP address in the `100.x.x.x` range. As long as the client device and NanoKVM Go are in the same Tailscale network (Tailnet), you can access NanoKVM Go through this address.

```text
NanoKVM Go -- Tailscale virtual network -- remote computer or phone
```

> This guide focuses on configuring Tailscale through the web interface to access NanoKVM Go remotely.

## Prerequisites

Before starting, make sure that:

- NanoKVM Go is connected to the Internet;
- NanoKVM Go is accessible from the local network;
- the NanoKVM Go system and application are updated to the latest versions;
- the computer or phone used for remote access can install the Tailscale client.

> If the Tailscale option is not available on the settings page, check for and install the latest NanoKVM Go system and application updates.

## Register and Log In to Tailscale

NanoKVM Go and the computer or phone used for remote access must join the same Tailscale network (Tailnet). If this is your first time using Tailscale:

1. Visit the [Tailscale website](https://tailscale.com/);
2. Click `Get started` or `Log in`;

![Registration and login entry on the Tailscale website](../../../../assets/NanoKVM/go/network/tailscale_homepage_get_started.webp)

3. Sign in using one of the supported account providers;
4. Follow the prompts to complete the initial authorization;
5. Open the Tailscale admin console and select the `Machines` device list.

![Machines device list in the Tailscale admin console](../../../../assets/NanoKVM/go/network/tailscale_admin_machines.webp)

The `Machines` page is used to view and manage devices in the current Tailnet. After completing the following configuration, both NanoKVM Go and the client device will appear on this page.

> Tailscale plans, organization management, and advanced network settings are not required for basic remote access and are not covered in this guide.

## Enable Tailscale on NanoKVM Go

### Open the Tailscale Settings

Log in to the NanoKVM Go web interface and click the settings icon in the top toolbar.

![Open the NanoKVM Go settings page](../../../../assets/NanoKVM/go/network/nanokvm_go_settings_button.webp)

### Install or Start Tailscale

Select `Tailscale` in the sidebar. If the page indicates that Tailscale is not running, click `Start` and wait for the service to start.

![Start Tailscale on NanoKVM Go](../../../../assets/NanoKVM/go/network/nanokvm_go_tailscale_start.webp)

### Log In to Tailscale

1. After Tailscale starts, click `Log in`. The page generates a temporary authentication link and opens the Tailscale login page in the browser.

![Click the Tailscale login button on NanoKVM Go](../../../../assets/NanoKVM/go/network/nanokvm_go_tailscale_login.webp)

2. Select the same account or sign-in method used earlier and complete authentication.

![Select a Tailscale login method](../../../../assets/NanoKVM/go/network/tailscale_login_methods.webp)

3. Confirm that the device information is correct, then click `Connect` to add NanoKVM Go to the current Tailnet.

![Confirm connecting NanoKVM Go to the Tailnet](../../../../assets/NanoKVM/go/network/tailscale_connect_device.webp)

4. When the page displays `Login successful`, the Tailscale account authorization is complete.

![Tailscale login successful](../../../../assets/NanoKVM/go/network/tailscale_login_success.webp)

5. Return to the NanoKVM Go web interface and click `Login complete`.

![Confirm the completed login on NanoKVM Go](../../../../assets/NanoKVM/go/network/nanokvm_go_tailscale_confirm_login.webp)

6. When the device name, device address, and account are displayed, NanoKVM Go has successfully joined the Tailnet.

![Tailscale device address and account information on NanoKVM Go](../../../../assets/NanoKVM/go/network/nanokvm_go_tailscale_device_info.webp)

### Confirm That NanoKVM Go Is Online

Open the `Machines` page in the Tailscale admin console and locate NanoKVM Go. A `Connected` status indicates that the device is online.

![Confirm that NanoKVM Go is online in the Tailscale admin console](../../../../assets/NanoKVM/go/network/tailscale_admin_nanokvm_connected.webp)

## Install and Log In to Tailscale on the Client Device

Install Tailscale on the computer or phone that will remotely access NanoKVM Go. Official installation guides for each platform are listed below:

| Platform | Installation method |
| --- | --- |
| Windows | Follow the [Tailscale for Windows installation guide](https://tailscale.com/docs/install/windows) to download and install the client |
| macOS | Follow the [Tailscale for macOS installation guide](https://tailscale.com/docs/install/mac) to install it from the website or App Store |
| Linux | Follow the [Tailscale for Linux installation guide](https://tailscale.com/docs/install/linux) to use the official installation script or package repository |
| Android | Follow the [Tailscale for Android installation guide](https://tailscale.com/docs/install/android) to install it from an official channel |
| iOS / iPadOS | Follow the [Tailscale for iOS installation guide](https://tailscale.com/docs/install/ios) to install it from the App Store |

After installation, connect the client device to the Tailnet:

1. Start the Tailscale client and click `Log in`;
2. Sign in with the same Tailscale account used by NanoKVM Go;
3. Confirm that the client shows a connected status;
4. Open the `Machines` page and confirm that both the client device and NanoKVM Go are online.

> If the client device uses a different account, first invite that account to the Tailnet containing NanoKVM Go and grant it the required access permissions.

## Find the Tailscale IP Address of NanoKVM Go

After NanoKVM Go joins the Tailnet, it receives a Tailscale IP address in the `100.x.x.x` range. You can find this address in either of the following locations.

### Find the Address in NanoKVM Go Settings

Open `Settings` > `Tailscale` on NanoKVM Go and find the Tailscale IP in the `Device Address` field.

![Find the Tailscale IP in NanoKVM Go settings](../../../../assets/NanoKVM/go/network/nanokvm_go_tailscale_ip.webp)

### Find the Address in the Tailscale Admin Console

Open the `Machines` page in the Tailscale admin console and find the Tailscale IP in the `ADDRESSES` column for NanoKVM Go.

![Find the NanoKVM Go Tailscale IP in the Tailscale admin console](../../../../assets/NanoKVM/go/network/tailscale_admin_nanokvm_ip.webp)

## Access NanoKVM Go Remotely

Before connecting, confirm that both NanoKVM Go and the client device show `Connected` on the `Machines` page.

![Confirm that the client device and NanoKVM Go are connected to Tailscale](../../../../assets/NanoKVM/go/network/tailscale_admin_devices_connected.webp)

To ensure that the test uses an external network, disconnect the client device from the current LAN and use a phone hotspot or mobile network instead. Then follow these steps:

1. Confirm that the Tailscale client is connected on the client device;
2. Enter the Tailscale IP address of NanoKVM Go in the browser address bar, for example, `http://100.x.x.x`;
3. Open the NanoKVM Go login page and sign in;
4. Test remote video, keyboard and mouse control, power control, and other features.

> If the page cannot be opened, confirm that both devices use the same Tailnet and that NanoKVM Go and the client device are still online.

## Everyday Use and Security Recommendations

- Enable two-factor authentication for the Tailscale account;
- set a strong password for NanoKVM Go and keep its own login authentication enabled;
- do not expose additional NanoKVM Go ports on the router;
- do not share Tailscale device authentication links with others;
- regularly review the Tailscale admin console and remove unused devices;
- in multi-user environments, use ACLs or Grants to restrict device access;
- regularly update NanoKVM Go and the Tailscale client to receive the latest features and security fixes.
