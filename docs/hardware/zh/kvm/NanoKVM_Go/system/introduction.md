---
title: 系统编译
keywords: NanoKVM Go, Remote desktop, KVM, system
update:
    - date: 2026-07-15
      version: v0.2
      author: Liang Ziyue
      content:
          - 补充 NanoKVM Go 系统镜像和 KVM APP 构建说明
---

NanoKVM Go 的软件由两部分组成：

- 系统镜像；
- KVM APP。

系统镜像负责提供 NanoKVM Go 运行所需的基础系统、驱动、网络服务和运行环境。KVM APP 运行在系统镜像之上，负责提供网页控制端、画面采集、键鼠控制和设备管理等 KVM 功能。

这两部分的构建流程相互独立。系统 SDK 编译出来的是可烧录的系统镜像；KVM APP 仓库编译出来的是应用 `.deb` 包和应用更新包。系统镜像不会自动包含 KVM APP 仓库中的最新代码。

## 构建内容

| 内容 | 构建入口 | 主要产物 | 用途 |
| --- | --- | --- | --- |
| 系统镜像 | `maix_ax620e_sdk` | `.axp`、SD 卡 `.img` | 烧录 eMMC 或制作 SD 启动卡 |
| KVM APP | `NanoKVM-Go` | `.deb`、`nanokvm-go_<version>.tar.gz` | 安装或更新设备上的 KVM 应用 |

建议先构建并验证系统镜像可以正常启动，再构建和安装 KVM APP。

## 构建环境

推荐使用 Ubuntu 22.04 或 WSL Ubuntu 22.04。构建系统镜像时，如果需要生成 SD 卡镜像，建议使用支持 loop 设备的完整 Linux 环境，例如 Ubuntu 物理机或虚拟机。

安装基础依赖：

```bash
sudo apt update
sudo apt install -y \
  build-essential git make gcc g++ bc bison flex \
  libssl-dev libncurses-dev libncurses5-dev libncursesw5-dev \
  u-boot-tools device-tree-compiler texinfo texlive gawk \
  binfmt-support fusefat debootstrap \
  libpcre3 patchelf python3 python3-pip python3-lxml python3-pyelftools \
  parted dosfstools mtools e2fsprogs rsync util-linux wget curl xz-utils \
  cmake dpkg-dev debhelper
```

<!-- SDK 构建脚本对 `/bin/sh` 有兼容性要求，建议将 dash 切换为 bash 兼容模式：

```bash
sudo dpkg-reconfigure dash
```

弹窗中选择 `No`。如果当前环境没有弹出交互界面，可以使用非交互方式：

```bash
echo "dash dash/sh boolean false" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash
ls -l /bin/sh
```

期望看到 `/bin/sh -> bash`。 -->

NanoKVM Go 的 Debian rootfs 是 `armhf`。在 x86_64 / amd64 宿主机上构建时，需要安装 QEMU 用户态模拟器，并确认 `qemu-arm` 的 `binfmt_misc` 已启用。

Ubuntu 22.04 通常可以直接安装 `qemu-user-static`：

```bash
sudo apt update
sudo apt install -y qemu-user-static binfmt-support
```

如果提示 `qemu-user-static` 是虚拟包、没有可安装候选，请安装系统提示的实际包。一般选择 `qemu-user-binfmt` 即可：

```bash
sudo apt update
sudo apt install -y qemu-user-binfmt binfmt-support
```

如果系统提示同时存在 `qemu-user-binfmt-hwe`，并且你正在使用 Ubuntu HWE 软件源，也可以安装 HWE 版本：

```bash
sudo apt install -y qemu-user-binfmt-hwe binfmt-support
```

安装后检查 `qemu-arm` 是否已注册：

```bash
update-binfmts --display qemu-arm
cat /proc/sys/fs/binfmt_misc/qemu-arm
```

如果 `update-binfmts` 提示 `qemu-arm not in database of installed binary formats`，先导入再启用：

```bash
sudo update-binfmts --import qemu-arm
sudo update-binfmts --enable qemu-arm
```

如果导入后仍然没有生效，可以重启 binfmt 服务后再检查：

```bash
sudo systemctl restart binfmt-support || sudo service binfmt-support restart
```

也可以检查解释器文件是否存在。不同发行版的路径可能不同，存在其中一个即可：

```bash
ls -l /usr/bin/qemu-arm-static
ls -l /usr/libexec/qemu-binfmt/arm-binfmt-P
```

如果 `cat` 提示文件不存在，先确认 `binfmt_misc` 已挂载，并再次启用 `qemu-arm`：

```bash
sudo mount -t binfmt_misc binfmt_misc /proc/sys/fs/binfmt_misc || true
sudo update-binfmts --enable qemu-arm
cat /proc/sys/fs/binfmt_misc/qemu-arm
```

输出中包含 `enabled` 即可继续。

## 编译系统镜像

### 获取 SDK

NanoKVM Go 的系统 SDK 位于：

[maix_ax620e_sdk](https://github.com/sipeed/maix_ax620e_sdk)

获取代码并初始化子模块：

```bash
mkdir -p ~/NanoKVM_Go
cd ~/NanoKVM_Go
git clone https://github.com/sipeed/maix_ax620e_sdk
cd maix_ax620e_sdk
git submodule sync --recursive
git submodule update --init --recursive
```

如果没有 GitHub SSH 权限，可以将子模块地址改为 HTTPS 后再同步：

```bash
git config -f .gitmodules submodule.msp.url https://github.com/sipeed/maix_ax620e_sdk_msp.git
git config -f .gitmodules submodule.kernel.url https://github.com/sipeed/maix_ax620e_sdk_kernel.git
git submodule sync --recursive
git submodule update --init --recursive
```

如果之前已经用 SSH 地址克隆失败过，可以清理失败的子模块缓存后再执行上面的 HTTPS 配置和更新命令：

```bash
git submodule deinit -f kernel msp
rm -rf .git/modules/kernel .git/modules/msp kernel msp
```

### 安装系统 SDK 工具链

NanoKVM Go 使用 AX620Q、ARM 32 位、glibc、Debian rootfs，对应系统 SDK 工具链为 `arm-none-linux-gnueabihf-` GCC 10。

```bash
cd /tmp
wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/10.3-2021.07/binrel/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.tar.xz
sudo tar -xf gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.tar.xz -C /opt

export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH
arm-none-linux-gnueabihf-gcc --version
```

如果需要长期使用，可以写入 shell 配置：

```bash
echo 'export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH' >> ~/.bashrc
```

### 生成 Debian Base Rootfs

NanoKVM Go 的工程配置名为：

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent
```

先生成基础 rootfs：

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian
sudo -E TARGET_ARCH=armhf DEBIAN_RELEASE=trixie bash ./mk_debian_base.sh .
```

如果默认 Debian 源下载较慢，可以指定镜像源，例如清华源：

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian
sudo -E \
  TARGET_ARCH=armhf \
  DEBIAN_RELEASE=trixie \
  DEBIAN_MIRROR=https://mirrors.tuna.tsinghua.edu.cn/debian \
  bash ./mk_debian_base.sh .
```

生成后检查产物：

```bash
ls -lh ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian/debian_rootfs_base.tar.gz
```

如果 Tailscale 下载时报 404，例如：

```text
https://pkgs.tailscale.com/stable/debian/pool/tailscale_1.98.5_armhf.deb
ERROR 404: Not Found.
```

说明 `mk_debian_base.sh` 中硬编码的 Tailscale `.deb` 版本在官方仓库里不存在或已经调整。先查询当前 `trixie armhf` 可用版本：

```bash
curl -L https://pkgs.tailscale.com/stable/debian/dists/trixie/main/binary-armhf/Packages \
  | grep -A12 '^Package: tailscale' \
  | grep -E 'Version:|Filename:' \
  | tail -n 20
```

然后修改：

```bash
~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian/mk_debian_base.sh
```

将 `wget -O /tmp/tailscale.deb ...` 里的文件名替换为仓库里实际存在的版本。例如当前可用版本之一是：

```text
pool/tailscale_1.98.9_armhf.deb
```

对应下载地址：

```text
https://pkgs.tailscale.com/stable/debian/pool/tailscale_1.98.9_armhf.deb
```

### 构建 AXP 镜像

进入 SDK 的 `build` 目录构建系统镜像：

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build
export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH

make p=AX620Q_emmc_arm32_k419_sipeed_nanoagent clean all install axp -j$(nproc)
```

如果并行构建出现偶发依赖错误，可以降低并发重试：

```bash
make p=AX620Q_emmc_arm32_k419_sipeed_nanoagent clean all install axp -j1
```

构建完成后，在 `build/out` 下检查 `.axp`：

```bash
ls -lh ~/NanoKVM_Go/maix_ax620e_sdk/build/out/*.axp
```

`.axp` 可用于通过 AXDL 烧录 eMMC。

### 生成恢复或 SD 卡镜像

系统镜像构建成功后，根据烧录方式选择生成的镜像类型。

如果使用 USB 恢复模式烧录 NanoKVM Go，优先生成 rootfs 分区更新镜像：

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build/projects/AX620Q_emmc_arm32_k419_sipeed_nanoagent
sudo -E bash ./gen_sd_image.sh --update
```

该命令生成的是 rootfs 分区镜像，文件名类似：

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent_sd_update_<时间>.img
```

`sd_update_*.img` 用于写入 NanoKVM Go 通过 USB 恢复模式暴露出来的 rootfs 分区，不要写入整张空 SD 卡。

如果要把 NanoKVM Go 拆开，取出内部 TF 卡并通过读卡器烧录，才需要生成完整 SD 卡镜像：

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build/projects/AX620Q_emmc_arm32_k419_sipeed_nanoagent
sudo -E bash ./gen_sd_image.sh
```

默认输出位于 `build/out`，文件名类似：

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent_sdcard_<时间>.img
```

写入 TF 卡时应写入整张 TF 卡设备，而不是某个分区：

```bash
sudo dd if=<sdcard.img> of=/dev/<TF卡整盘设备> bs=4M status=progress conv=fsync
```

NanoKVM Go 外壳通常使用胶水粘合，不建议普通用户为了烧录系统拆机取卡。一般情况下，应使用 USB 恢复模式和 `sd_update_*.img`。

## 编译 KVM APP

### 准备 APP 仓库

KVM APP 的构建入口是 `NanoKVM-Go` 仓库根目录的 `build.py`。获取源码后，进入仓库：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
```

主要组件包括：

| 组件 | 作用 |
| --- | --- |
| `server` | Go 后端服务 |
| `web` | Web 前端页面 |
| `libkvm` | KVM 相关动态库 |
| `kvm_vin` | 视频输入组件 |
| `kvm_ui` | UI / 显示组件 |
| `nano_ocr` | OCR 组件 |
| `memfab` | Go 运行组件 |
| `debhelper` | Debian 打包目录 |

### 准备 APP 构建环境

APP 构建需要 Go、Node.js、pnpm、Python 3、CMake、Conan、Debian 打包工具，以及项目自带的 ARMv7 工具链。

基础依赖示例：

```bash
sudo apt update
sudo apt install -y build-essential python3 python3-pip cmake git patchelf dpkg-dev debhelper
python3 -m pip install --user conan
```

根据仓库中的 `go.mod` 要求安装对应版本的 Go。当前 `memfab` 要求 Go 1.26，`server` 要求 Go 1.25.0 或更新版本。可以直接安装 Go 1.26：

```bash
cd /tmp
GO_VERSION=1.26.0
wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz

echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc
export PATH=/usr/local/go/bin:$PATH

go version
```

如果 `wget` 提示文件不存在，请到 [Go 下载页面](https://go.dev/dl/)确认当前可用的 1.26.x 版本号，并替换 `GO_VERSION`。

前端使用 pnpm。推荐安装 Node.js 22，并通过 Corepack 启用 pnpm：

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs

node -v
npm -v
corepack enable
pnpm -v
```

如果当前 shell 找不到 `go`，重新打开终端，或者执行：

```bash
source ~/.bashrc
```

安装项目自带的 ARMv7 工具链：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go/support/scripts
./toolchain_setup.sh
```

构建前确认当前终端使用的是 APP 工具链：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
export PATH=~/NanoKVM_Go/NanoKVM-Go/support/toolchains/armv7-toolchain/bin:$PATH
hash -r

which arm-none-linux-gnueabihf-gcc
arm-none-linux-gnueabihf-gcc --version
```

`which` 应指向：

```text
~/NanoKVM_Go/NanoKVM-Go/support/toolchains/armv7-toolchain/bin/arm-none-linux-gnueabihf-gcc
```

### 构建全部组件

在 APP 仓库根目录执行：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
python3 build.py build
```

该命令会依次构建：

```text
libkvm
kvm_vin
kvm_ui
nano_ocr
memfab
server
web
```

构建完成后检查产物：

```bash
find build -maxdepth 2 -type f | sort
```

常见产物包括：

```text
build/NanoKVM-Server
build/kvm_ui
build/kvm_vin
build/libkvm.so.0.1.0
build/memfab
build/nano_ocr_app
build/web/index.html
```

### 打包 APP

推荐使用 release 命令完成完整构建和打包：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
python3 build.py release --version <version>
```

例如：

```bash
python3 build.py release --version 0.0.21
```

release 流程会执行：

```text
build
package_kvmcomm
package_nanokvm_go
package_update
```

生成的 Debian 包位于：

```text
build/kvmcomm_<version>_armhf.deb
build/nanokvm-go_<version>_armhf.deb
```

生成的应用更新包位于：

```text
build/update/nanokvm-go_<version>.tar.gz
build/update/latest.json
```

如果组件已经构建完成，也可以单独打包：

```bash
python3 build.py package_kvmcomm
python3 build.py package_nanokvm_go
python3 build.py package_update --version <version>
```

`package_update --version` 使用的版本号必须和 `.deb` 包版本一致。

### 安装到设备

设备已经启动并且可以通过 SSH 连接时，可以使用 `.deb` 安装或更新 APP。假设设备 IP 为 `192.168.1.50`：

```bash
cd ~/NanoKVM_Go/NanoKVM-Go

scp build/kvmcomm_<version>_armhf.deb root@192.168.1.50:/root/
scp build/nanokvm-go_<version>_armhf.deb root@192.168.1.50:/root/
```

登录设备后安装：

```bash
ssh root@192.168.1.50
dpkg -i /root/kvmcomm_<version>_armhf.deb /root/nanokvm-go_<version>_armhf.deb
sync
reboot
```

## 注意事项

- 系统镜像和 KVM APP 是两条构建流程。构建 SDK 镜像不会自动编译或集成 `NanoKVM-Go` 仓库中的最新 APP。
- NanoKVM Go 系统镜像使用 `AX620Q_emmc_arm32_k419_sipeed_nanoagent` 工程，rootfs 是 `armhf` Debian rootfs，不是 AX630C 使用的 arm64 Ubuntu rootfs。
- 系统 SDK 使用 GCC 10 工具链，KVM APP 使用项目自带的 GCC 12 ARMv7 工具链。切换构建对象前，先用 `which arm-none-linux-gnueabihf-gcc` 和 `arm-none-linux-gnueabihf-gcc --version` 确认当前工具链。
- `rootfs/arm/glibc/debian/mk_debian_rootfs_sipeed.sh` 通常由 SDK `make` 流程调用，不建议手动无参数执行。
- `debian_rootfs_base.tar.gz` 是 Debian 基础 rootfs。只要基础 rootfs 没有变化，通常不需要每次都重新生成。
- 如果 rootfs 构建时报 `Exec format error`，通常是 `qemu-arm` 的 `binfmt_misc` 没有启用。先确认 `/proc/sys/fs/binfmt_misc/qemu-arm` 输出中包含 `enabled`。
- 如果 SD 卡镜像生成时报找不到可用 loop 设备，说明当前环境不支持或未启用 loop block device。建议换到完整 Linux 环境中运行 `gen_sd_image.sh`。
- `sdcard_*.img` 是完整 SD 卡镜像，应写入整张 SD 卡设备；`sd_update_*.img` 是 rootfs 分区更新镜像，不要写入整张空 SD 卡。
- `.axp` 用于通过 AXDL 烧录系统镜像；`.deb` 用于系统已启动后的 APP 安装或更新；`nanokvm-go_<version>.tar.gz` 和 `latest.json` 用于应用更新包。
