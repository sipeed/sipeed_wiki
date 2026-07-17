---
title: System Build
keywords: NanoKVM Go, Remote desktop, KVM, system
update:
    - date: 2026-07-15
      version: v0.2
      author: Liang Ziyue
      content:
          - Add NanoKVM Go system image and KVM APP build instructions
---

NanoKVM Go software consists of two parts:

- system image;
- KVM APP.

The system image provides the base system, drivers, network services, and runtime environment required by NanoKVM Go. The KVM APP runs on top of the system image and provides KVM functions such as the web control page, video capture, keyboard and mouse control, and device management.

These two build flows are independent. The system SDK builds a flashable system image. The KVM APP repository builds application `.deb` packages and application update packages. The system image does not automatically include the latest code from the KVM APP repository.

## Build Outputs

| Item | Build Entry | Main Outputs | Usage |
| --- | --- | --- | --- |
| System image | `maix_ax620e_sdk` | `.axp`, SD card `.img` | Flash eMMC or create an SD boot card |
| KVM APP | `NanoKVM-Go` | `.deb`, `nanokvm-go_<version>.tar.gz` | Install or update the KVM application on the device |

It is recommended to build and verify that the system image can boot normally before building and installing the KVM APP.

## Build Environment

Ubuntu 22.04 or WSL Ubuntu 22.04 is recommended. When building the system image, if you need to generate an SD card image, use a complete Linux environment with loop device support, such as a physical Ubuntu machine or a virtual machine.

Install basic dependencies:

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

<!-- The SDK build scripts have compatibility requirements for `/bin/sh`. It is recommended to switch dash to bash-compatible mode:

```bash
sudo dpkg-reconfigure dash
```

Select `No` in the dialog. If the current environment does not show an interactive dialog, use the non-interactive method:

```bash
echo "dash dash/sh boolean false" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash
ls -l /bin/sh
```

The expected result is `/bin/sh -> bash`. -->

NanoKVM Go uses an `armhf` Debian rootfs. When building on an x86_64 / amd64 host, install the QEMU user-mode emulator and confirm that `qemu-arm` `binfmt_misc` is enabled.

Ubuntu 22.04 can usually install `qemu-user-static` directly:

```bash
sudo apt update
sudo apt install -y qemu-user-static binfmt-support
```

If `qemu-user-static` is reported as a virtual package without an installation candidate, install the actual package suggested by the system. In most cases, choose `qemu-user-binfmt`:

```bash
sudo apt update
sudo apt install -y qemu-user-binfmt binfmt-support
```

If the system also suggests `qemu-user-binfmt-hwe` and you are using Ubuntu HWE repositories, you can install the HWE package instead:

```bash
sudo apt install -y qemu-user-binfmt-hwe binfmt-support
```

After installation, check that `qemu-arm` is registered:

```bash
update-binfmts --display qemu-arm
cat /proc/sys/fs/binfmt_misc/qemu-arm
```

If `update-binfmts` reports `qemu-arm not in database of installed binary formats`, import it before enabling it:

```bash
sudo update-binfmts --import qemu-arm
sudo update-binfmts --enable qemu-arm
```

If it still does not take effect after importing, restart the binfmt service and check again:

```bash
sudo systemctl restart binfmt-support || sudo service binfmt-support restart
```

You can also check whether the interpreter file exists. The path can differ between distributions, and either one is acceptable:

```bash
ls -l /usr/bin/qemu-arm-static
ls -l /usr/libexec/qemu-binfmt/arm-binfmt-P
```

If `cat` reports that the file does not exist, confirm that `binfmt_misc` is mounted, and enable `qemu-arm` again:

```bash
sudo mount -t binfmt_misc binfmt_misc /proc/sys/fs/binfmt_misc || true
sudo update-binfmts --enable qemu-arm
cat /proc/sys/fs/binfmt_misc/qemu-arm
```

The output should include `enabled`.

## Build the System Image

### Get the SDK

The NanoKVM Go system SDK is available at:

[maix_ax620e_sdk](https://github.com/sipeed/maix_ax620e_sdk)

Clone the code and initialize submodules:

```bash
mkdir -p ~/NanoKVM_Go
cd ~/NanoKVM_Go
git clone https://github.com/sipeed/maix_ax620e_sdk
cd maix_ax620e_sdk
git submodule sync --recursive
git submodule update --init --recursive
```

If you do not have GitHub SSH access, change the submodule URLs to HTTPS and synchronize again:

```bash
git config -f .gitmodules submodule.msp.url https://github.com/sipeed/maix_ax620e_sdk_msp.git
git config -f .gitmodules submodule.kernel.url https://github.com/sipeed/maix_ax620e_sdk_kernel.git
git submodule sync --recursive
git submodule update --init --recursive
```

If a previous clone already failed with SSH URLs, clean the failed submodule cache before running the HTTPS configuration and update commands above:

```bash
git submodule deinit -f kernel msp
rm -rf .git/modules/kernel .git/modules/msp kernel msp
```

### Install the System SDK Toolchain

NanoKVM Go uses AX620Q, 32-bit ARM, glibc, and Debian rootfs. The corresponding system SDK toolchain is `arm-none-linux-gnueabihf-` GCC 10.

```bash
cd /tmp
wget https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/10.3-2021.07/binrel/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.tar.xz
sudo tar -xf gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf.tar.xz -C /opt

export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH
arm-none-linux-gnueabihf-gcc --version
```

To use it permanently, add it to your shell configuration:

```bash
echo 'export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH' >> ~/.bashrc
```

### Generate the Debian Base Rootfs

The NanoKVM Go project configuration is:

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent
```

Generate the base rootfs first:

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian
sudo -E TARGET_ARCH=armhf DEBIAN_RELEASE=trixie bash ./mk_debian_base.sh .
```

If the default Debian mirror is slow, specify a mirror, such as the Tsinghua mirror:

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian
sudo -E \
  TARGET_ARCH=armhf \
  DEBIAN_RELEASE=trixie \
  DEBIAN_MIRROR=https://mirrors.tuna.tsinghua.edu.cn/debian \
  bash ./mk_debian_base.sh .
```

Check the output after generation:

```bash
ls -lh ~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian/debian_rootfs_base.tar.gz
```

If Tailscale returns a 404 error during download, for example:

```text
https://pkgs.tailscale.com/stable/debian/pool/tailscale_1.98.5_armhf.deb
ERROR 404: Not Found.
```

This means the Tailscale `.deb` version hardcoded in `mk_debian_base.sh` does not exist in the official repository or has been changed. First check the currently available `trixie armhf` versions:

```bash
curl -L https://pkgs.tailscale.com/stable/debian/dists/trixie/main/binary-armhf/Packages \
  | grep -A12 '^Package: tailscale' \
  | grep -E 'Version:|Filename:' \
  | tail -n 20
```

Then edit:

```bash
~/NanoKVM_Go/maix_ax620e_sdk/rootfs/arm/glibc/debian/mk_debian_base.sh
```

Replace the filename in `wget -O /tmp/tailscale.deb ...` with a version that actually exists in the repository. For example, one currently available version is:

```text
pool/tailscale_1.98.9_armhf.deb
```

The corresponding download URL is:

```text
https://pkgs.tailscale.com/stable/debian/pool/tailscale_1.98.9_armhf.deb
```

### Build the AXP Image

Enter the SDK `build` directory and build the system image:

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build
export PATH=/opt/gcc-arm-10.3-2021.07-x86_64-arm-none-linux-gnueabihf/bin:$PATH

make p=AX620Q_emmc_arm32_k419_sipeed_nanoagent clean all install axp -j$(nproc)
```

If a parallel build hits an occasional dependency error, reduce the job count and retry:

```bash
make p=AX620Q_emmc_arm32_k419_sipeed_nanoagent clean all install axp -j1
```

After the build completes, check the `.axp` file under `build/out`:

```bash
ls -lh ~/NanoKVM_Go/maix_ax620e_sdk/build/out/*.axp
```

The `.axp` file can be used to flash eMMC through AXDL.

### Generate a Recovery or SD Card Image

After the system image is built successfully, choose the image type according to the flashing method.

If you use USB recovery mode to flash NanoKVM Go, generate the rootfs partition update image first:

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build/projects/AX620Q_emmc_arm32_k419_sipeed_nanoagent
sudo -E bash ./gen_sd_image.sh --update
```

This command generates a rootfs partition image with a filename similar to:

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent_sd_update_<time>.img
```

`sd_update_*.img` is used for writing to the rootfs partition exposed by NanoKVM Go USB recovery mode. Do not write it to a blank whole SD card.

Only generate a complete SD card image if you disassemble NanoKVM Go, remove the internal TF card, and flash it through a card reader:

```bash
cd ~/NanoKVM_Go/maix_ax620e_sdk/build/projects/AX620Q_emmc_arm32_k419_sipeed_nanoagent
sudo -E bash ./gen_sd_image.sh
```

The default output is under `build/out`, with a filename similar to:

```text
AX620Q_emmc_arm32_k419_sipeed_nanoagent_sdcard_<time>.img
```

When writing to a TF card, write to the whole TF card device, not to a partition:

```bash
sudo dd if=<sdcard.img> of=/dev/<whole-tf-card-device> bs=4M status=progress conv=fsync
```

The NanoKVM Go enclosure is usually glued together, so normal users are not recommended to disassemble it just to flash the system. In most cases, use USB recovery mode and `sd_update_*.img`.

## Build the KVM APP

### Prepare the APP Repository

The KVM APP build entry is `build.py` in the root directory of the `NanoKVM-Go` repository. After obtaining the source code, enter the repository:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
```

The main components include:

| Component | Function |
| --- | --- |
| `server` | Go backend service |
| `web` | Web frontend page |
| `libkvm` | KVM-related dynamic library |
| `kvm_vin` | Video input component |
| `kvm_ui` | UI / display component |
| `nano_ocr` | OCR component |
| `memfab` | Go runtime component |
| `debhelper` | Debian packaging directory |

### Prepare the APP Build Environment

The APP build requires Go, Node.js, pnpm, Python 3, CMake, Conan, Debian packaging tools, and the ARMv7 toolchain provided by the project.

Basic dependency example:

```bash
sudo apt update
sudo apt install -y build-essential python3 python3-pip cmake git patchelf dpkg-dev debhelper
python3 -m pip install --user conan
```

Install the Go version required by `go.mod` in the repository. Currently, `memfab` requires Go 1.26, and `server` requires Go 1.25.0 or later. You can install Go 1.26 directly:

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

If `wget` reports that the file does not exist, check the current available 1.26.x version on the [Go downloads page](https://go.dev/dl/) and replace `GO_VERSION`.

The frontend uses pnpm. It is recommended to install Node.js 22 and enable pnpm through Corepack:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs

node -v
npm -v
corepack enable
pnpm -v
```

If the current shell cannot find `go`, reopen the terminal or run:

```bash
source ~/.bashrc
```

Install the ARMv7 toolchain provided by the project:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go/support/scripts
./toolchain_setup.sh
```

Before building, confirm that the current terminal is using the APP toolchain:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
export PATH=~/NanoKVM_Go/NanoKVM-Go/support/toolchains/armv7-toolchain/bin:$PATH
hash -r

which arm-none-linux-gnueabihf-gcc
arm-none-linux-gnueabihf-gcc --version
```

`which` should point to:

```text
~/NanoKVM_Go/NanoKVM-Go/support/toolchains/armv7-toolchain/bin/arm-none-linux-gnueabihf-gcc
```

### Build All Components

Run the following command in the APP repository root:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
python3 build.py build
```

This command builds the following components in order:

```text
libkvm
kvm_vin
kvm_ui
nano_ocr
memfab
server
web
```

After the build completes, check the outputs:

```bash
find build -maxdepth 2 -type f | sort
```

Common outputs include:

```text
build/NanoKVM-Server
build/kvm_ui
build/kvm_vin
build/libkvm.so.0.1.0
build/memfab
build/nano_ocr_app
build/web/index.html
```

### Package the APP

It is recommended to use the release command to complete the full build and packaging process:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go
python3 build.py release --version <version>
```

For example:

```bash
python3 build.py release --version 0.0.21
```

The release flow runs:

```text
build
package_kvmcomm
package_nanokvm_go
package_update
```

The generated Debian packages are located at:

```text
build/kvmcomm_<version>_armhf.deb
build/nanokvm-go_<version>_armhf.deb
```

The generated application update packages are located at:

```text
build/update/nanokvm-go_<version>.tar.gz
build/update/latest.json
```

If all components have already been built, you can also package them separately:

```bash
python3 build.py package_kvmcomm
python3 build.py package_nanokvm_go
python3 build.py package_update --version <version>
```

The version used by `package_update --version` must match the version of the `.deb` packages.

### Install to the Device

When the device has booted and can be accessed through SSH, use the `.deb` packages to install or update the APP. Assuming the device IP address is `192.168.1.50`:

```bash
cd ~/NanoKVM_Go/NanoKVM-Go

scp build/kvmcomm_<version>_armhf.deb root@192.168.1.50:/root/
scp build/nanokvm-go_<version>_armhf.deb root@192.168.1.50:/root/
```

Log in to the device and install:

```bash
ssh root@192.168.1.50
dpkg -i /root/kvmcomm_<version>_armhf.deb /root/nanokvm-go_<version>_armhf.deb
sync
reboot
```

## Notes

- The system image and KVM APP are two separate build flows. Building the SDK image does not automatically compile or integrate the latest APP from the `NanoKVM-Go` repository.
- The NanoKVM Go system image uses the `AX620Q_emmc_arm32_k419_sipeed_nanoagent` project. Its rootfs is an `armhf` Debian rootfs, not the arm64 Ubuntu rootfs used by AX630C.
- The system SDK uses the GCC 10 toolchain. The KVM APP uses the GCC 12 ARMv7 toolchain provided by the project. Before switching build targets, use `which arm-none-linux-gnueabihf-gcc` and `arm-none-linux-gnueabihf-gcc --version` to confirm the current toolchain.
- `rootfs/arm/glibc/debian/mk_debian_rootfs_sipeed.sh` is usually called by the SDK `make` flow. It is not recommended to run it manually without parameters.
- `debian_rootfs_base.tar.gz` is the Debian base rootfs. If the base rootfs has not changed, it usually does not need to be regenerated every time.
- If the rootfs build reports `Exec format error`, `qemu-arm` `binfmt_misc` is usually not enabled. First confirm that `/proc/sys/fs/binfmt_misc/qemu-arm` output includes `enabled`.
- If SD card image generation reports that no available loop device can be found, the current environment does not support or has not enabled loop block devices. It is recommended to run `gen_sd_image.sh` in a complete Linux environment.
- `sdcard_*.img` is a complete SD card image and should be written to the whole SD card device. `sd_update_*.img` is a rootfs partition update image and should not be written to a blank whole SD card.
- `.axp` is used to flash the system image through AXDL. `.deb` is used for APP installation or update after the system has booted. `nanokvm-go_<version>.tar.gz` and `latest.json` are used as application update packages.
