---
title: Flashing the System
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

*The NanoKVM Full version comes pre-flashed with an image and can skip this step if desired.*

1. Prepare the SD Card:

    - The Full version comes with a 32G SD card. You will need to remove it by opening the case.
    - The Lite version requires you to prepare an SD card of at least 8G.

1. Go to [Github](https://github.com/sipeed/NanoKVM/releases) to download the latest version image.

1. Install the flashing software. We recommend using [Etcher](https://etcher.balena.io).

1. Run Etcher:
    ![run Ethcer](../../../../assets/NanoKVM/flashing/run_etcher.png)

1. Click `Flash from file` and select the image file:

    ![select image](../../../../assets/NanoKVM/flashing/select_image.png)

1. Click `Select target` and choose the SD card:

    ![select target](../../../../assets/NanoKVM/flashing/select_target.png)

1. Click `Flash!` to start the flashing process:

    ![select target](../../../../assets/NanoKVM/flashing/flashing.png)

1. Wait for the flashing process to complete.

    ![select target](../../../../assets/NanoKVM/flashing/flashed.png)

Congratulations! The image has been successfully flashed!

You can now insert the SD card into the NanoKVM and proceed to the next steps.