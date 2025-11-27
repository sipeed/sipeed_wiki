---
title: Access NanoKVM over the Internet with Cloudflare Tunnel (`cloudflared`)
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2025-11-16
    version: v0.1
    author: Johnnybyzhang
    content:
      - Release docs
---

Cloudflare Tunnel lets NanoKVM establish a secure **outbound‑only** connection to Cloudflare, so you don’t need public IPs, port‑forwarding, or inbound firewall holes. PiKVM documents a systemd flow; NanoKVM uses BusyBox `init`, so service setup differs.

Cloudflare does not provide an official RISC‑V build of `cloudflared`, so support on NanoKVM should be considered community‑maintained.

This guide draws from PiKVM’s community documentation on Cloudflare Tunnel. Security considerations covered there are not repeated in full here.

> **Audience**: NanoKVM users on BusyBox/SysV `init`. **Scope**: Token‑only tunnel, RISC‑V binary, minimal `init.d` service.

---

## Prerequisites

- Cloudflare Zero Trust account and a **remotely‑managed Tunnel** (Dashboard → Access → Tunnels → *Create Tunnel*). Copy the **tunnel token**.
- Shell access to NanoKVM.
- RISC‑V build of `cloudflared` (locally compiled with Go). For build notes, see the community discussion: [https://github.com/cloudflare/cloudflared/issues/621](https://github.com/cloudflare/cloudflared/issues/621).
- (Optional) PiKVM reference for general concepts: [https://docs.pikvm.org/cloudflared/](https://docs.pikvm.org/cloudflared/)

> **Security** — The token can start the tunnel. Treat it like a secret.

---

### Get the cloudflared binary

If you are on NanoKVM Pro, you may download the binary directly from the Cloudflare/cloudflared repository or use PiKVM OS, which includes a compatible build and a full guide that this guide references.

If you are on NanoKVM (RISCV CPU), use one of the following methods:

- Download from this automated build that has it's build system fully open-source: [https://github.com/Johnnybyzhang/cloudflared-riscv/releases](https://github.com/Johnnybyzhang/cloudflared-riscv/releases)
- Follow the reference in official cloudflare/cloudflared repo issue #621

## Install the binary

Place your locally built binary and verify it works.

It is recommended to attach external media in the WebUI and place the binary on the USB drive that appears on the system.

```sh
install -m 0755 /data/cloudflared /usr/sbin/cloudflared
/usr/sbin/cloudflared --version
```

---

## Minimal token‑only configuration

Use a config file to avoid exposing the token in the process list.

```sh
mkdir -p /etc/cloudflared
umask 077
cat >/etc/cloudflared/config.yml <<'YAML'
no-autoupdate: true
token: YOUR_TUNNEL_TOKEN_HERE
YAML
chmod 600 /etc/cloudflared/config.yml
```

**One‑shot foreground test** (useful for first‑run troubleshooting):

```sh
cloudflared tunnel --config /etc/cloudflared/config.yml --no-autoupdate run
```

> **Flag order matters** — Global options like `--config`, `--logfile`, `--no-autoupdate` must come **before** `run`.

---

## BusyBox `init` service (no systemd)

Create a small `init.d` script that starts **after networking**. The example uses `S45` to follow `S40network`.

```sh
cat >/etc/init.d/S45cloudflared <<'SH'
#!/bin/sh
PATH=/usr/sbin:/usr/bin:/sbin:/bin
DAEMON="/usr/sbin/cloudflared"
CONF="/etc/cloudflared/config.yml"
LOG="/var/log/cloudflared.log"
PIDFILE="/var/run/cloudflared.pid"

start() {
    [ -x "$DAEMON" ] || { echo "cloudflared not found"; exit 1; }
    [ -f "$CONF" ]   || { echo "missing $CONF"; exit 1; }
    mkdir -p /var/run
    printf "Starting cloudflared: "
    # Keep cloudflared’s own logfile; silence console output
    "$DAEMON" tunnel --config "$CONF" --logfile "$LOG" --no-autoupdate run >/dev/null 2>&1 &
    echo $! >"$PIDFILE"
    echo "OK"
}

stop() {
    printf "Stopping cloudflared: "
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        kill "$(cat "$PIDFILE")" 2>/dev/null || true
        sleep 2
        kill -0 "$(cat "$PIDFILE")" 2>/dev/null && kill -9 "$(cat "$PIDFILE")" 2>/dev/null || true
        rm -f "$PIDFILE"
        echo "OK"
    else
        killall cloudflared 2>/dev/null && echo "OK" || echo "not running"
    fi
}

status() {
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
        echo "cloudflared running (pid $(cat "$PIDFILE"))"
    else
        echo "cloudflared stopped"; exit 1
    fi
}

case "$1" in
  start) start ;;
  stop) stop ;;
  restart|reload) stop; start ;;
  status) status ;;
  *) echo "Usage: $0 {start|stop|restart|status}"; exit 1 ;;
 esac
exit 0
SH
chmod +x /etc/init.d/S45cloudflared
```

**Enable & verify**

```sh
/etc/init.d/S45cloudflared start
/etc/init.d/S45cloudflared status
tail -n 100 /var/log/cloudflared.log
```

> **Why logs might appear in your terminal** — If you start your own init.d script interactively, the child process may inherit your TTY. The script example above redirects output with `>/dev/null 2>&1` and uses `--logfile` for persistent logs.

---

## Networking & time

- Only **outbound** connectivity is required: TCP/443 (and optionally UDP/7844 for QUIC).
- Keep device time accurate (NTP) to avoid TLS issues.

---

## Troubleshooting and suggestions (If you choose to create your own init.d script)

- **“flag provided but not defined: -config”** → Place `--config` **before** `run`.
- **No logs** → Check `/var/log/cloudflared.log` and file perms; verify `--logfile` path exists.
- **Stop doesn’t work** → On first connect `--pidfile` can be used; otherwise the fallback `killall` path helps if the pidfile vanished.
- **Token safety** → Avoid `--token` on the command line; prefer the config file.

---

## Uninstall / disable

```sh
/etc/init.d/S45cloudflared stop
chmod -x /etc/init.d/S45cloudflared
rm -f /usr/sbin/cloudflared /etc/cloudflared/config.yml /var/log/cloudflared.log /var/run/cloudflared.pid
```

---

## References

- PiKVM: Cloudflare Tunnels (general concepts, systemd‑based): [https://docs.pikvm.org/cloudflared/](https://docs.pikvm.org/cloudflared/)
- RISC‑V build discussion for cloudflared: [https://github.com/cloudflare/cloudflared/issues/621](https://github.com/cloudflare/cloudflared/issues/621)

