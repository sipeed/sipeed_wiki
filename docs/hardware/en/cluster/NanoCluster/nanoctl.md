---
title: NanoCtl
---

## Introduction

**NanoCtl** is a community-developed CLI tool and daemon designed specifically for the Sipeed NanoCluster (CM5). It provides a lightweight, native Go solution for managing hardware interfaces, replacing complex script dependencies.

It allows users to easily manage power states for individual nodes and control the cooling fan with intelligent algorithms.

![nanoctl](../../../zh/cluster/NanoCluster/assets/nanoctl.jpeg)

### Key Features

* **Power Management**: Control individual slot power via GPIO, supporting Power On, Graceful Shutdown, Force Off, and Hardware Reset.
* **Smart Fan Control**: Implements a PID Controller (Proportional-Integral-Derivative) to maintain precise target temperatures with smooth, quiet fan operation.
* **Monitoring & Metrics**: Supports exporting metrics (Fan PWM, Temperature) to Prometheus or OpenTelemetry (OTLP) for visualization.
* **Zero Dependency**: Written in Go as a single binary, interacting directly with Linux GPIO character devices.

## Links

- **GitHub Project**: [https://github.com/AlejandroPerez92/nanoctl](https://github.com/AlejandroPerez92/nanoctl)