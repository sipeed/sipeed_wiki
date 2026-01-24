---
title: IPMI Operation Manual
keywords: IPMI, NanoKVM, Remote desktop, PiKVM, RISCV, tool
---

> 💡 Prerequisite: Update your system image to [v1.4.2](https://github.com/sipeed/NanoKVM/releases/tag/v1.4.2) or a later version before proceeding.

## Project Overview

This project provides a software-based IPMI simulator. It allows users to remotely manage hardware power states and access the Serial Over LAN console using standard IPMI protocols.

Core Components:

- **`ipmi_sim`**: The main open-source IPMI simulator binary (part of OpenIPMI).
- **`ipmi-sim.sh`**: Service management script responsible for starting, stopping, and monitoring the simulator process.
- **`chassis_control.sh`**: Hardware Abstraction Layer (HAL) script that controls physical hardware power/reset pins via GPIO.
- **`lan.conf`**: Configuration file defining users, network interfaces, and SOL serial parameters.

---

## Accessing the Device

Before starting the installation and configuration, you need to log in to the NanoKVM system terminal. There are two ways to do this:

### Method 1: Web Terminal

1. Enter the NanoKVM IP address in your browser address bar to access the Web UI.
2. Locate the **Terminal** icon in the menu bar and open the **Web Terminal**.

### Method 2: SSH Login

If you prefer using command-line tools, you can connect via SSH.

1. Open a terminal on your computer.
2. Run the following command (replace `<IP_Address>` with the actual IP of your NanoKVM):

   ```bash
   ssh root@<IP_Address>
   ```

3. Enter the default password `root` to log in.

---

## Installation & Deployment

The service is designed to be installed in the `/etc/ipmi` directory.

### Directory Structure

Ensure your system follows this file structure:

```text
/etc/ipmi/
├── ipmi-sim.sh        # Service control script
├── chassis_control.sh # Hardware control script
├── lan.conf           # Main configuration file
├── sim.emu            # Simulator persistence data
```

---

## Configuration Guide

### Users & Passwords (`lan.conf`)

The default configuration includes a single admin account.
**For security, it is highly recommended to change the default password before deployment.**

Edit the user section at the bottom of `/etc/ipmi/lan.conf`:

```text
# User 2: Admin user
#         Enabled  Username  Password  Privilege  Max_Sessions  Auth_Type
user 2    true     "admin"   "admin"   admin      10            md5
```

Change `"admin"` (the password field) to your desired password.

### Serial Over LAN (SOL)

To enable viewing device serial output via IPMI, configure the `sol` option in `lan.conf`:

```text
# Map to the physical serial device, e.g., /dev/ttyS1
sol "/dev/ttyS1" 115200 nortscts
```

---

## Service Management

Use the `ipmi-sim.sh` script to manage the service.

### Common Commands

| Operation | Command | Description |
| :--- | :--- | :--- |
| **Start Service** | `/etc/ipmi/ipmi-sim.sh start` | Start the IPMI simulator background process |
| **Stop Service** | `/etc/ipmi/ipmi-sim.sh stop` | Stop the running service |
| **Restart Service** | `/etc/ipmi/ipmi-sim.sh restart` | Stop and then start the service |
| **Check Status** | `/etc/ipmi/ipmi-sim.sh status` | Check if service is running and view PID |
| **Enable Auto-Start** | `/etc/ipmi/ipmi-sim.sh enable` | Configure service to start automatically on boot |
| **Disable Auto-Start** | `/etc/ipmi/ipmi-sim.sh disable` | Disable auto-start on boot |

### Example

```bash
# Enable auto-start and start the service immediately
/etc/ipmi/ipmi-sim.sh enable
/etc/ipmi/ipmi-sim.sh start
```

---

## Client Usage (ipmitool)

You can manage the device remotely from any machine with an IPMI client (like `ipmitool` on Linux/macOS).

**Connection Parameters:**

- `-H`: Target IP address (e.g., NanoKVM IP)
- `-U`: Username (default: admin)
- `-P`: Password (default: admin)
- `-I`: Interface type (use `lanplus` for IPMI 2.0)
- `-C`: Cipher Suite. **It it recommended to use `-C 3`** to skip the long protocol negotiation process.

### Supported Command List

This project currently only supports the following core IPMI commands:

| Category | Command (ipmitool) | Description |
| :--- | :--- | :--- |
| **Power** | `power status` | Check current power state (ON/OFF) |
| | `power on` | Turn on the system |
| | `power off` | Turn off the system (Force/Hard shutdown) |
| | `power reset` | Reset the system (Reboot) |
| **SOL** | `sol activate` | Start Serial Over LAN session |
| | `sol deactivate` | Terminate Serial Over LAN session |
| **Management** | `mc info` | View BMC basic information |

### Power Control

```bash
# Check power status
ipmitool -H <IP> -U admin -P admin -I lanplus power status

# Power On
ipmitool -H <IP> -U admin -P admin -I lanplus power on

# Power Off (Hard shutdown)
ipmitool -H <IP> -U admin -P admin -I lanplus power off

# Reset (Reboot)
ipmitool -H <IP> -U admin -P admin -I lanplus power reset
```

### Serial Over LAN (SOL)

Connect to the device's serial console over the network:

```bash
# Activate SOL session
ipmitool -H <IP> -U admin -P admin -I lanplus sol activate

# Deactivate/Exit SOL session
# Key sequence: ~ + . (Tilde followed by Dot)
```

*Note: If the SOL connection fails, verify the serial device path in `lan.conf` and ensure no other process is locking the serial port.*

### 6.4 Performance Optimization

By default, `ipmitool` attempts to negotiate the encryption protocol with the server, which can cause a delay of several seconds before every command execution.
**Solution**: Explicitly add the `-C 3` parameter to your commands.

**Optimized Command Examples:**

```bash
# 1. Quickly get BMC info (Recommended test command)
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 mc info

# 2. Quickly check power status
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 power status

# 3. Quickly activate SOL
ipmitool -H <IP> -U admin -P admin -I lanplus -C 3 sol activate
```

---

## Troubleshooting

1. **Service Fails to Start**
   - Check if port 623 (UDP) is already in use: `netstat -ln | grep 623`
   - Check system logs. Try running the underlying command manually in the foreground to see error messages.

2. **ipmitool Connection Timeout**
   - Check firewall settings; ensure UDP port 623 is open.
   - Verify the `ipmi_sim` process is running: `ps aux | grep ipmi_sim`.
