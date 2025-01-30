---
title: "Using Yosys with Tang Primer"
date: 2019-03-10T15:51:32+05:30
---

The Yosys now support Verilog synthesis for Anlogic's FPGA. Although support is partial, it progressing towards having full synthesis support.

### Prerequisites

For Ubuntu Linux 16.04 LTS the following commands will install all prerequisites for building yosys:

```
sudo apt-get install build-essential clang bison flex \
	libreadline-dev gawk tcl-dev libffi-dev git \
	graphviz xdot pkg-config python3
```

### Download Yosys from Github

Clone the Yosys repository from Github.

```
git clone https://github.com/YosysHQ/yosys.git
```

### Build and Install Yosys

To build Yosys simply type 'make' in this directory.

```
make
make test
sudo make install
```

### Compile the Anlogic Demo

We are going to compile an Anlogic example from Yosys examples directory.

### Setup TD environment for demo

For Place and Route, we still need Official TD tools.

set `TD_HOME` env variable to the full path to the TD <TD Install Directory> as follow.

```
export TD_HOME=<TD Install Directory Path>
```

Finally, we are ready to build our demo.

```
cd examples/anlogic/
bash build.sh
```
This build will produce demo.bit that can be download into Tang Primer via TD Download tool.
