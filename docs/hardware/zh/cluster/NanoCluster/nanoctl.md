---
title: NanoCtl
---

## 简介

**NanoCtl** 是一个由社区开发的 CLI 工具和守护进程，专为 Sipeed NanoCluster (CM5) 设计。它提供了一种轻量级、原生 Go 语言编写的解决方案来管理硬件接口，旨在替代复杂的脚本依赖。

通过它，用户可以轻松管理单个节点的电源状态，并利用智能算法控制散热风扇。

![nanoctl](../../../zh/cluster/NanoCluster/assets/nanoctl.jpeg)

### 主要特性

* **电源管理**：通过 GPIO 控制单个插槽的电源，支持开机、优雅关机 (Graceful Shutdown)、强制关机和硬件复位。
* **智能风扇控制**：实现了 PID 控制器（比例-积分-微分算法），在保持精确目标温度的同时，确保风扇运行平稳且静音。
* **监控与指标**：支持将指标数据（如风扇 PWM 占空比、温度）导出到 Prometheus 或 OpenTelemetry (OTLP) 以进行可视化监控。
* **零依赖**：基于 Go 语言编写，编译为单个二进制文件，直接与 Linux GPIO 字符设备交互，无需额外运行环境。

## 链接

- **GitHub 项目**: [https://github.com/AlejandroPerez92/nanoctl](https://github.com/AlejandroPerez92/nanoctl)