---
title: Tailscale
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

> **It is recommended to use NanoKVM with Tailscale for accessing remote hosts over the internet.**

*Note: Tailscale is not supported in v1.0.0 of the image. If your NanoKVM image version is v1.0.0, please [update the image](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/start/flashing.html) first.*

NanoKVM now comes with Tailscale built-in, and you can start using it with just a few simple steps. There are two methods for configuring Tailscale: via the browser and via the terminal. Browser configuration is recommended. However, if you need more customization, you can also configure it via the terminal.

## Configuring via Browser

1. Enter the IP address of NanoKVM in your browser and access it.
2. Click on Settings - Tailscale:

    ![ipconfig](../../../../assets/NanoKVM/tailscale/setting.png)

3. If prompted that Tailscale is not installed, click Install and wait for the installation to complete. If it shows as installed, proceed to the next step:

    ![ipconfig](../../../../assets/NanoKVM/tailscale/install.png)

4. Click Login and wait for Tailscale to start and generate a login link (this step only needs to be done once; Tailscale will start automatically on boot):

    ![ipconfig](../../../../assets/NanoKVM/tailscale/login.png)

5. Once the login link is generated, the browser will automatically open it. If it does not redirect automatically, manually visit the generated link. Log in to your Tailscale account and click `Connect` to add NanoKVM to your account.

    ![ipconfig](../../../../assets/NanoKVM/tailscale/connect.png)

6. You should now see NanoKVM under your Tailscale account. In a public network environment, run Tailscale and access NanoKVM using `100.79.236.88 (replace with your Tailscale IP)` in your browser:

    ![ipconfig](../../../../assets/NanoKVM/tailscale/machines.png)

## Configuring via Terminal

1. SSH into NanoKVM.
2. Execute `tailscale version` to check if Tailscale is already installed. If not, manually install it:
    - Download [Tailscale](https://pkgs.tailscale.com/stable/tailscale_latest_riscv64.tgz) and extract it;
    - Move the `tailscale` file to the `/usr/bin/` directory;
    - Move the `tailscaled` file to the `/usr/sbin/` directory.
3. Execute `/etc/init.d/S98tailscaled restart` to start the Tailscale service.
4. Execute `tailscale login` and wait for the login link to be generated, then visit the generated link in your browser.
5. Click `Connect` in the browser to add NanoKVM to your Tailscale account.
6. You're all set! You can now access NanoKVM via Tailscale.