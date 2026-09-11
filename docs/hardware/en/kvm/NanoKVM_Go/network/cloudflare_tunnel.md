---
title: Cloudflare Tunnel
keywords: NanoKVM Go, Cloudflare Tunnel, cloudflared, Quick Tunnel, remote access
---

# Configure Cloudflare Tunnel

Cloudflare Tunnel runs `cloudflared` on NanoKVM Go and connects outward to Cloudflare, so the device can be reached from the Internet without a public IP address, port forwarding, or inbound firewall rules.
If you are not familiar with domains and DNS, start with **Part 2**. If you already know how to buy a domain and change DNS records, go straight to **Part 3**.

> Whichever option you choose, change the default NanoKVM Go password first. For long-term use, configure Cloudflare Access as well.

## Part 1: Basic Setup (Installation and Preparation)

### Before You Start

Confirm that:

- NanoKVM Go is connected to the Internet;
- the NanoKVM Go web console opens normally from your local network;
- SSH is enabled, and you know the device's LAN IP address and SSH password;
- you have a computer with SSH and SCP available;
- for a permanent tunnel, you already have a Cloudflare account and a domain of your own.

### Log In to NanoKVM Go

Run the following in Windows PowerShell or another terminal:

```bash
ssh root@192.168.255.255
```

Replace `192.168.255.255` with the actual LAN IP address of your NanoKVM Go. On the first connection, check that the IP address is correct, type `yes` to accept the device fingerprint, then enter the SSH password.

### Install cloudflared

#### Download and Upload the Binary

On your computer, open [cloudflared Releases](https://github.com/cloudflare/cloudflared/releases) and download the latest `cloudflared-linux-armhf` build. Do not download the `arm64` or `amd64` build.

Copy it to NanoKVM Go from PowerShell:

```bash
scp "C:\Users\<your-user-name>\Desktop\cloudflared-linux-armhf" root@192.168.255.255:/root/cloudflared
```

#### Install the Binary

Back in the NanoKVM Go SSH session, run:

```bash
install -m 0755 /root/cloudflared /usr/local/bin/cloudflared
/usr/local/bin/cloudflared --version
```

## Part 2: Quick Tunnel (No Domain Required)

A Quick Tunnel needs neither a Cloudflare account nor a domain. When `cloudflared` starts, it prints a random `trycloudflare.com` address, which stops working as soon as the process exits.

### Start a Quick Tunnel

Run:

```bash
/usr/local/bin/cloudflared tunnel --no-autoupdate --protocol http2 --no-tls-verify --url https://127.0.0.1:443
```

The command keeps running in the current terminal. Wait until a random address appears in the log, for example:

```text
https://random-words.trycloudflare.com
```

Open the full address in a browser and confirm that the NanoKVM Go login page loads. Do not share this address: the random hostname is not an access password by itself.

### Stop the Quick Tunnel

Return to the terminal running `cloudflared` and press `Ctrl+C`. Once the prompt reappears, the Quick Tunnel has stopped, and the old random address should no longer be treated as a valid entry point.

## Part 3: Permanent Tunnel (Custom Domain)

A permanent tunnel uses a fixed hostname and starts `cloudflared` automatically when NanoKVM Go boots. This part uses a tunnel that is managed from the Cloudflare dashboard and connected with a tunnel token.

```text
Remote browser
    │
    │  https://kvm.example.com
    ▼
Cloudflare
    │
    │  outbound connection initiated by cloudflared
    ▼
NanoKVM Go (https://127.0.0.1:443)
```

### Add the Domain to Cloudflare

If the domain is not on Cloudflare yet:

1. Add the root domain in the Cloudflare dashboard;
2. Review the DNS records Cloudflare imports automatically, so that existing A, CNAME, MX, or TXT records are not deleted by mistake;
3. At your domain registrar, replace the nameservers with the two addresses Cloudflare assigns to the domain;
4. Wait until the domain status in Cloudflare becomes `Active`.

The nameservers Cloudflare assigns depend on the account and the domain: always use the values shown in your own dashboard instead of copying an example.

### Create a Tunnel and Get the Token

Cloudflare dashboard labels change over time, so use the names shown on the current page:

1. Go to `Networking` > `Tunnels`;

![The Tunnels page and the Create a Tunnel button](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_tunnels_page.webp)

2. Create a Cloudflare Tunnel;
3. Give it a recognizable name, for example `nanokvm-go`;

![Creating the tunnel and copying the install command](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_create_tunnel.webp)

4. Open the tunnel's `Add a replica` page;

![Opening the new tunnel from the Tunnels list](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_tunnel_created.webp)

5. Copy the install command shown on that page and take the tunnel token from it: the field that starts with `eyJ`.

![The install command on the Add a replica page](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_add_a_replica.webp)

> A tunnel token can run the tunnel on its own, and anyone who obtains it may be able to connect to your tunnel. Never share the token, a command that contains it, or terminal screenshots with others. If the token leaks, rotate it on the tunnel page immediately and update the token stored on NanoKVM Go.

### Save the Token on the Device

In the install command shown in the dashboard, only the last field, the string starting with `eyJ`, is the tunnel token. Copy that field only, not the command in front of it.

Run the following in the NanoKVM Go SSH session, replacing `eyJ...` with your actual token:

```bash
install -d -m 0700 /etc/cloudflared
echo 'eyJ...' > /etc/cloudflared/tunnel-token
chmod 600 /etc/cloudflared/tunnel-token
```

`install -d` creates a directory that only root can enter, `echo` writes the token into the file through the redirection, and `chmod 600` leaves the file readable and writable by root only. The token is written to the file and is never printed to the terminal.

Check the file permissions and size without displaying the contents:

```bash
stat -c '%a %n' /etc/cloudflared/tunnel-token
wc -c < /etc/cloudflared/tunnel-token
```

The expected permission is `600`. The byte count is the token length plus one for the trailing newline, typically a few hundred bytes. If it reports `0`, the file is empty and the token must be written again.

### Test the Tunnel in the Foreground

Run:

```bash
/usr/local/bin/cloudflared tunnel --no-autoupdate --protocol http2 run --token-file /etc/cloudflared/tunnel-token
```

When the log shows `Registered tunnel connection`, `cloudflared` is connected to Cloudflare. Press `Ctrl+C` to stop the test.

This only proves that the tunnel connection is established; the hostname still cannot reach NanoKVM Go until a published application is configured.

### Add a Published Application

Open the tunnel you just created in the Cloudflare dashboard:

1. Go to `Routes`;

![The Routes tab and the Add route button](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_routes.webp)

2. Select `Add route` > `Published application`;
3. Set `Subdomain` to the subdomain you plan to use, for example `kvm`;
4. Set `Domain` to the root domain that is already on Cloudflare;
5. Leave `Path` empty;
6. Set `Service URL` to `https://127.0.0.1:443`;

![Filling in the hostname and the service URL](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_add_application_hostname.webp)

7. Expand the additional application settings and enable `Disable TLS certificate verification` under the TLS settings;

![Enabling Disable TLS certificate verification under TLS](../../../../assets/NanoKVM/go/network/nanokvm_go_cloudflare_tunnel_disable_tls_verify.webp)

8. Save the route.

`Disable TLS certificate verification` is required because the local HTTPS service on NanoKVM Go usually uses a self-signed certificate. The setting only affects the connection from `cloudflared` to the local `127.0.0.1:443`; it does not turn off HTTPS between the browser and Cloudflare.

### Create a systemd Service

Create `/etc/systemd/system/cloudflared.service` on NanoKVM Go:

```ini
[Unit]
Description=Cloudflare Tunnel for NanoKVM Go
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/cloudflared tunnel --no-autoupdate --protocol http2 run --token-file /etc/cloudflared/tunnel-token
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Load the service and enable it at boot:

```bash
systemctl daemon-reload
systemctl enable --now cloudflared
systemctl status cloudflared --no-pager
```

When the service reports `active (running)` and the log contains `Registered tunnel connection`, the connection is up. To view recent log entries:

```bash
journalctl -u cloudflared -n 50 --no-pager
```

### Access from the Internet

Switch your computer or phone to a different network and open the hostname you configured, for example:

```text
https://kvm.example.com
```

If the NanoKVM Go login page opens, sign in with the NanoKVM Go account and test video, keyboard, mouse, and power control.

## Security Recommendations

- Set a strong, dedicated password for NanoKVM Go;
- for long-term use, configure Access authentication and an allow policy for the domain in Cloudflare Zero Trust;
- do not publish Quick Tunnel addresses or permanent tunnel hostnames;
- do not write tunnel tokens, Cloudflare API tokens, or SSH passwords into documents or screenshots;
- keep `cloudflared` and NanoKVM Go up to date;
- review tunnel connections, access logs, and Cloudflare account members regularly;
- rotate a leaked token immediately; changing the NanoKVM Go login password alone is not enough.

If you no longer need the permanent tunnel:

1. Delete or disable the corresponding published application in the Cloudflare dashboard;
2. Run `systemctl disable --now cloudflared` on NanoKVM Go;
3. Once you are sure you will not need it again, delete the local token and service files;
4. If the token was ever exposed, rotate it in the dashboard and disconnect the old connection.

Deleting a route or a token invalidates the original entry point, so confirm first that no other user or tunnel replica still depends on it.
