---
title: Tailscale
keywords: Tailscale, remote access, NAT traversal
update:
    - date: 2026-07-13
      version: v0.1
      author: Liang Ziyue
---

# Tailscale

## 1. Introduction to Tailscale

Tailscale is a WireGuard-based mesh networking tool. It can add NanoKVM Go, computers, phones, and other devices to the same virtual LAN, allowing you to access NanoKVM Go remotely without a public IP address or router port forwarding.

After joining a Tailscale network, each device receives a virtual IP address in the `100.x.x.x` range. As long as the client device and NanoKVM Go are in the same Tailscale network (Tailnet), you can access NanoKVM Go through this address.

```text
NanoKVM Go -- Tailscale virtual network -- remote computer or phone
```

> This guide focuses on configuring Tailscale through the web interface to access NanoKVM Go remotely.

## 2. Prerequisites

Before starting, make sure that:

- NanoKVM Go is connected to the Internet;
- NanoKVM Go is accessible from the local network;
- the NanoKVM Go system and application versions support Tailscale;
- the computer or phone used for remote access can install the Tailscale client.
<!-- TODO: Add the minimum version requirements and instructions for checking the version. -->

## 3. Register and Log In to Tailscale

NanoKVM Go and the computer or phone used for remote access must join the same Tailscale network (Tailnet). If this is your first time using Tailscale:

1. Visit the [Tailscale website](https://tailscale.com/);
2. Click `Get Started` or `Log in`;
3. Sign in using one of the supported account providers;
4. Follow the prompts to complete the initial authorization;
5. Open the Tailscale admin console and locate the `Machines` device list.

The `Machines` page is used to view and manage devices in the current Tailnet. After completing the following configuration, both NanoKVM Go and the client device will appear on this page.

<!-- TODO: Add screenshots of the Tailscale login page, account provider selection, and Machines page. -->

> Tailscale plans, organization management, and advanced network settings are not required for basic remote access and are not covered in this guide.

## 4. Enable Tailscale on NanoKVM Go

### 4.1 Open the Tailscale Settings

<!-- TODO: Add instructions and screenshots for opening the NanoKVM Go settings page. -->

### 4.2 Install or Start Tailscale

<!-- TODO: Add the location of the install/start button and the page status after installation. -->

### 4.3 Log In to Tailscale

<!-- TODO: Add instructions and screenshots for obtaining the login link, signing in, and clicking Connect to authorize the device. -->

### 4.4 Confirm That NanoKVM Go Is Online

<!-- TODO: Add the interface shown after login and explain how to verify the online status. -->

## 5. Install and Log In to Tailscale on the Client Device

Install Tailscale on the computer or phone that will remotely access NanoKVM Go:

1. Download and install the client from an official Tailscale channel;
2. Start Tailscale and click `Log in`;
3. Sign in with the same account used during registration;
4. Confirm that the client shows a connected status;
5. Check that NanoKVM Go appears in the device list.

If you use a different account, make sure that account has been invited to the Tailnet containing NanoKVM Go.

| Platform | Installation method |
| --- | --- |
| Windows | Download the installer from the Tailscale website |
| macOS | Install from the Tailscale website or the App Store |
| Linux | Use the official installation script or package repository |
| Android | Install from Google Play or another official channel |
| iOS / iPadOS | Install from the App Store |

<!-- TODO: Using Windows as an example, add screenshots for downloading, installing, logging in, and confirming a successful connection. Also add official links for each platform. -->

## 6. Find the Tailscale IP Address of NanoKVM Go

After NanoKVM Go joins the Tailnet, it receives a Tailscale IP address in the `100.x.x.x` range. You can find this address on the NanoKVM Go settings page or in the Tailscale admin console.

<!-- TODO: Add both methods and the corresponding screenshots. -->

## 7. Access NanoKVM Go Remotely

To ensure that the test uses an external network, disconnect the client device from the current LAN and use a phone hotspot or mobile network instead:

1. Confirm that Tailscale is connected on the client device;
2. Enter the Tailscale IP address of NanoKVM Go in the browser address bar;
3. Log in to NanoKVM Go;
4. Test remote video, keyboard and mouse control, power control, and other features.

<!-- TODO: Add a complete access URL example and screenshots of the login page and a successful remote connection. -->

## 8. Everyday Use and Security Recommendations

- Enable two-factor authentication for the Tailscale account;
- set a strong password for NanoKVM Go and keep its own login authentication enabled;
- do not expose additional NanoKVM Go ports on the router;
- do not share Tailscale device authentication links with others;
- regularly review the Tailscale admin console and remove unused devices;
- in multi-user environments, use ACLs or Grants to restrict device access.

## 9. Troubleshooting

### Tailscale Cannot Be Installed or Started

<!-- TODO: Add troubleshooting steps for the network, version, storage space, and service status. -->

### The Login Link Is Not Generated

<!-- TODO: Add checks for Internet connectivity, system time, and the Tailscale service. -->

### NanoKVM Go Appears Offline

<!-- TODO: Add instructions for checking the Machines page and the device status. -->

### The Tailscale IP Is Visible but Cannot Be Accessed

<!-- TODO: Add checks for the client connection status, Tailnet, ACLs, and NanoKVM services. -->

### The Connection Works but Video Is Choppy

<!-- TODO: Add recommendations related to network latency, bandwidth, video quality, and frame rate. -->

### Tailscale Does Not Reconnect After a Restart

<!-- TODO: Add instructions for checking automatic startup and logging in again. -->

## 10. Advanced Configuration

After completing the basic configuration, you can also learn how to:

- use MagicDNS to access NanoKVM Go by device name;
- change the NanoKVM Go device name in the Tailnet;
- manage device key expiration policies;
- use ACLs or Grants for precise access control;
- determine whether the current connection is peer-to-peer or relayed through DERP;
- use commands such as `tailscale status` to check the connection;
- log out of the current account or move NanoKVM Go to another Tailnet.

> Exit nodes and subnet routers are not required for remote access to NanoKVM Go. Most users only need to complete the first seven sections.
