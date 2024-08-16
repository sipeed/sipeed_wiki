---
title: Static IP
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

By default, NanoKVM obtains its IP address via DHCP, which means the IP address may change.

If you want to always access NanoKVM using the same IP address, you can set a static IP.

## Setting a Static IP

Create a file `/boot/eth.nodhcp` in NanoKVM and edit it as follows:

- Each line represents a custom IP in the format `addr/netid gw[optional]`;
- You can preset multiple static IPs on multiple lines.

```bash
# Example
192.168.0.101/24 192.168.0.1  # addr/netid gw
192.168.3.116/22              # addr/netid
```

After editing and saving the file, run the command `/etc/init.d/S30eth restart` to apply the configuration.

**Note:** If all preset static IP addresses are detected by ARP as already in use, setting the static IP will fail. In this case, DHCP will be triggered to obtain an IP address. If this also fails, the IP will be forcibly set to `192.168.90.1/24`.

This ensures that NanoKVM always has a usable IP address, allowing network access to operate NanoKVM. If NanoKVM does not receive a valid IP address, you will need to manually modify the file on the TF card or reflash the image to use it normally.

## Canceling the Static IP

Delete the `/boot/eth.nodhcp` file to cancel the static IP setting. NanoKVM will then obtain its IP address via DHCP again.