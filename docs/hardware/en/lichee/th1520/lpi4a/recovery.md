---
title: LicheePi 4A recovery notes
keywords: Linux, Lichee, TH1520, SBC, RISCV, recovery, flashing
update:
  - date: 2026-09-17
    version: v1.0
    author: tmsteph
    content:
      - Clarify BOOT and RESET button behavior during USB recovery
---

# LicheePi 4A recovery notes

## Entering USB download mode

The `RESET` and `BOOT` buttons are separate.

To enter USB download mode for flashing or recovery, hold the `BOOT` button while resetting or powering the board. Pressing `RESET` alone does not substitute for holding `BOOT`.

On some LicheePi 4A enclosures, the `RESET` button is externally accessible while the adjacent `BOOT` button is covered by the case. If the board is installed in an enclosure and does not enter USB download mode, you may need to partially open the enclosure to reach the `BOOT` button.

This distinction is especially useful when the board still has power or Ethernet PHY link but no longer reaches Linux or U-Boot normally, because USB download mode may be the next recovery path.

## Related documentation

See the LicheePi 4A image/flashing documentation for the current image and flashing commands.
