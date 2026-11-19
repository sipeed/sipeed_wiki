---
title: ROS2 使用指南
keywords: MaixSense, D640, ROS 2, 深度相机, 机器人
update_open: false
update:
  - date: 2026-11-04
    version: v0.1
    author: lxowalle
    content: 初版
---

ROS2 是用于构建机器人应用程序的工具包，可以把相机、机器人底盘、机械臂和算法程序连接起来，常见应用场景有：

- **移动机器人避障**：根据深度图或点云判断前方障碍物，为减速、停止和绕行提供依据。
- **室内导航与巡检**：结合地图和定位结果规划路线，让机器人到达目标位置或依次巡检多个地点。
- **环境建图**：把相机观测与机器人运动信息结合，建立周围环境的地图。
- **机械臂作业**：利用物体的空间位置和周围障碍物信息，辅助抓取定位与避碰规划。

本页介绍如何连接设备、查看图像与点云，以及保存和录制数据。导航、建图和机械臂作业需要另行配置对应的机器人程序。

第一次使用，请依次完成[准备环境](#准备环境)、[连接设备](#连接设备)和[首次使用](#首次使用)。完成后，日常只需加载环境并启动查看器。

## 准备环境

本页在连接设备的 Ubuntu 22.04 电脑上操作，使用 ROS2 Humble。其他系统版本请参考对应的 ROS 官方安装说明。

本节完成 ROS2、编译工具和 SDK 依赖的安装。已安装 Humble 的用户可跳过软件源配置，但仍需安装下方列出的依赖软件。

### 确认系统版本

```bash
cat /etc/os-release
dpkg --print-architecture
```

确认系统为 Ubuntu，`VERSION_ID` 为 `22.04`。处理器架构应为 `amd64` 或 `arm64`。ROS 2 Humble 的官方 Ubuntu 安装包对应这一系统版本。

### 检查 UTF-8 环境

```bash
locale
```

输出中的 LANG/LC_* 使用 UTF-8 即可，中文 `zh_CN.UTF-8` 也可以，不需要改成英文。仅当系统没有 UTF-8 环境时，执行下面的配置，然后重新检查 locale：

```bash
sudo apt update
sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale
```

### 添加 ROS2 官方软件源

软件源用于让 Ubuntu 的 apt 找到 ROS 安装包。下面安装 ROS 官方提供的软件源配置包，包含相应软件源和签名配置：

```bash
sudo apt update
sudo apt install software-properties-common curl python3
sudo add-apt-repository universe
```

配置官方软件源：

```bash
# 查询官方软件源配置包的最新版本
D640_ROS_APT_VERSION="$(curl -fsSL https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"])')"
# 下载适合 Ubuntu 22.04 的软件源配置包
curl -fL --retry 3 -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${D640_ROS_APT_VERSION}/ros2-apt-source_${D640_ROS_APT_VERSION}.jammy_all.deb"
# 安装软件源配置包
sudo dpkg -i /tmp/ros2-apt-source.deb
```

如果下载失败，先解决网络问题，不要继续安装空文件。软件源步骤以 [ROS 官方 Humble 安装说明](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html)为准。

### 安装 ROS2 和依赖软件

在准备阶段一次装好 ROS2、图形查看器、编译和图像处理所需的软件：

```bash
# 刷新软件包列表
sudo apt update
# 安装 ROS2、图形查看器，以及 SDK 编译和运行依赖
sudo apt install ros-humble-desktop ros-dev-tools \
  build-essential cmake ninja-build pkg-config \
  libopencv-dev zlib1g-dev python3-colcon-common-extensions \
  python3-catkin-pkg python3-yaml python3-rosdep
```

### 加载环境并检查安装

先查看当前终端使用的命令解释器：

```bash
ps -p $$ -o comm=
```

按输出点击 Bash 或 Zsh 标签，执行对应的命令：

<style>
.ros-shell-tabs { display: flex; flex-wrap: wrap; margin: 1em 0; }
.ros-shell-tabs > input { position: absolute; opacity: 0; width: 1px; height: 1px; }
.ros-shell-tabs > label { padding: .55em 1.3em; cursor: pointer; border-bottom: 2px solid transparent; }
.ros-shell-tabs > input:checked + label { color: #d33; border-bottom-color: currentColor; font-weight: bold; }
.ros-shell-tabs > input:focus-visible + label { outline: 2px solid currentColor; outline-offset: -2px; }
.ros-shell-tabs > .ros-shell-panel { display: none; width: 100%; min-width: 0; }
.ros-shell-tabs > .ros-shell-panel pre { margin-top: 0; }
.ros-shell-tabs > input.ros-shell-bash:checked ~ .ros-panel-bash,
.ros-shell-tabs > input.ros-shell-zsh:checked ~ .ros-panel-zsh { display: block; }
</style>

<div class="ros-shell-tabs" role="group" aria-label="选择当前终端的 Shell">
<input class="ros-shell-bash" type="radio" name="ros-base-shell" id="ros-base-shell-bash" checked><label for="ros-base-shell-bash">Bash</label>
<input class="ros-shell-zsh" type="radio" name="ros-base-shell" id="ros-base-shell-zsh"><label for="ros-base-shell-zsh">Zsh</label>
<div class="ros-shell-panel ros-panel-bash"><pre><code class="language-bash">source /opt/ros/humble/setup.bash</code></pre></div>
<div class="ros-shell-panel ros-panel-zsh"><pre><code class="language-zsh">source /opt/ros/humble/setup.zsh</code></pre></div>
</div>

加载后检查：

```bash
# 确认 ROS2 版本，预期输出 humble
echo "$ROS_DISTRO"
# 查看命令帮助，确认 ros2 可以使用
ros2 --help
```

若提示 ros2 找不到，先确认对应的 source 命令没有报错。新开终端后需要重新加载环境，或在后文按自己的 Shell 配置自动加载。

### 获取 SDK 并安装其依赖

下载并解压[最新 SDK 源码包](https://cdn.sipeed.com/maixsense/d640/latest/maixsense_d640_sdk_source.tar.gz)，确认其中包含 `scripts/setup-ros2.sh` 和 `ros2` 文件夹。然后在源码目录执行下面的命令。

```bash
# 进入 SDK 根目录
cd maixsense_d640_sdk
# 首次使用时初始化，已初始化可跳过
sudo rosdep init
# 更新依赖索引
rosdep update
# 根据 SDK 清单安装 ROS 依赖
rosdep install --from-paths ros2 --ignore-src -r -y --rosdistro humble
```

依赖安装完成后，继续连接设备。后面的构建、查看和录制步骤不需要重复安装这些软件。

## 连接设备

将设备通过 USB 连接到电脑。如果是 Linux 系统，请参考[快速上手](./quick-start.html#Linux-访问权限)配置访问权限。

## 首次使用

### 构建设备工具

环境准备完成后，在 SDK 根目录执行：

```bash
# 编译并安装设备工具，默认安装到 ~/.local/maixsense-d640-ros2
./scripts/setup-ros2.sh
```

只在首次安装或更新源码后执行，日常使用无需重新构建。

### 加载 ROS2 环境到终端

每个新终端都需要加载一次环境。按当前 Shell 点击 Bash 或 Zsh 标签，执行对应命令：

<div class="ros-shell-tabs" role="group" aria-label="选择当前终端的 Shell">
<input class="ros-shell-bash" type="radio" name="ros-device-shell" id="ros-device-shell-bash" checked><label for="ros-device-shell-bash">Bash</label>
<input class="ros-shell-zsh" type="radio" name="ros-device-shell" id="ros-device-shell-zsh"><label for="ros-device-shell-zsh">Zsh</label>
<div class="ros-shell-panel ros-panel-bash"><pre><code class="language-bash">source &quot;$HOME/.local/maixsense-d640-ros2/env.bash&quot;</code></pre></div>
<div class="ros-shell-panel ros-panel-zsh"><pre><code class="language-zsh">source &quot;$HOME/.local/maixsense-d640-ros2/env.zsh&quot;</code></pre></div>
</div>

把对应的 source 命令加入 `~/.bashrc`（Bash）或 `~/.zshrc`（Zsh），此后新终端就会自动加载MaixSense D640的ROS2环境。

### 检查是否可以启动

```bash
# 检查环境和连接，不开始采集
ros2 run maixsense_d640_driver maixsense_d640 doctor
```

### 查看图像与点云

在有桌面的 Ubuntu 电脑上执行：

```bash
# 启动相机采集程序和 RViz 图形查看器
ros2 run maixsense_d640_driver maixsense_d640 view
```

首次启动可能需要等待较长时间。请等待终端出现 `ready`，并确认图像和点云持续更新。若一直显示 `waiting for camera`，先检查 USB 连接和[访问权限](./quick-start.html#Linux-访问权限)。

![RViz 深度图和三维点云](../../../assets/maixsense/maixsense-d640/maix_sense_point_cloud.jpg)

伪彩图用颜色表示距离，不是真实彩色照片。点云表示物体的空间形状。将鼠标移到三维点云区域操作：

- 旋转：按住左键拖动。
- 平移：按住中键拖动。
- 缩放：滚动滚轮。

点云默认按前方深度着色，颜色范围会随画面自动调整。如果只有白点，展开左侧 **Depth PointCloud**，将 **Color Transformer** 设为 **AxisColor**、**Axis** 设为 **Z**，取消 **Use Fixed Frame**。

结束时在启动终端按 **Ctrl+C**。同一设备只运行一份采集程序，切换模式前先停止上一份。

## 日常使用

### 切换查看内容

加载环境后，选择一条命令执行：

```bash
# 查看深度图和三维点云
ros2 run maixsense_d640_driver maixsense_d640 view

# 只看左右红外图
ros2 run maixsense_d640_driver maixsense_d640 view --preset ir

# 只看设备输出的深度伪彩图，此模式不输出深度和点云
ros2 run maixsense_d640_driver maixsense_d640 view --preset pseudo
```

### 在 RViz 中添加画面

1. 在左侧 **Displays** 面板点击 **Add → By topic**。
2. 展开想看的话题，选择下表中的显示类型，点击 **OK**。
3. 确认新增显示项已勾选，并能看到持续更新的数据。

“Topic”就是设备输出数据的通道，默认名称如下：

| 内容 | Topic | 选择的显示类型 |
| :--- | :--- | :--- |
| 深度伪彩图 | `/stereo/pseudo_color/image_raw` | Image |
| 原始深度图 | `/stereo/depth/image_raw` | Image |
| 左红外图 | `/stereo/left/image_raw` | Image |
| 右红外图 | `/stereo/right/image_raw` | Image |
| 三维点云 | `/stereo/points2` | PointCloud2 |


### 选择设备

`msd-enumerate` 是前面的安装脚本一并安装的 SDK 查询工具，加载环境后即可使用。连接多台设备时，通过序列号指定设备：

```bash
# 查看当前设备，找到输出中 serial= 后面的完整序列号
msd-enumerate
# 用实际序列号替换 YOUR_SERIAL，再启动目标设备
ros2 run maixsense_d640_driver maixsense_d640 view --serial YOUR_SERIAL
```

### 查看运行状态

保持采集程序运行，在另一个已加载环境的终端执行下方命令可以检查连接状态和序列号，确认查询的是目标设备。话题出现在列表中，不代表已经收到图像。

```bash
ros2 run maixsense_d640_driver maixsense_d640 status
```

### 保存图像和点云

1. 使用默认 view 命令启动，确认图像和点云持续更新。
2. 在另一个已加载环境的终端执行：

   ```bash
   # 设置保存目录，保存在运行相机程序的电脑上
   mkdir -p "$HOME/d640-captures"
   ros2 param set /stereo/camera save_directory "$HOME/d640-captures"
   # 保存最近的图像和点云
   ros2 run maixsense_d640_driver maixsense_d640 save --kind both
   ```

3. 按命令返回的路径检查文件。默认深度采集保存的是原始深度和已开启的红外图，不包含 RViz 画面截图或主机生成的伪彩图。只保存图像时，将 `both` 改为 `images`，只保存点云时改为 `cloud`

### 录制数据

录制前先运行 view 或 start，确认设备正在输出数据。录制保存的是 ROS 消息，不是 MP4 视频。

1. 保持采集程序运行，在另一个已加载环境的终端执行：

   ```bash
   # 录制到当前目录下的新文件夹，目录名不能与已有录制重复
   ros2 run maixsense_d640_driver maixsense_d640 record --output ./d640-bag
   ```

2. 在录制终端按 **Ctrl+C** 结束录制，相机继续采集。
3. 检查录制结果：

   ```bash
   # 查看录制的话题、时长及消息数量
   ros2 bag info ./d640-bag
   ```
4. 确认录制结果中有所需的话题，且消息数量不为 0。
5. 回放前先停止实机采集，避免实时数据与录制数据混在一起。执行：

   ```bash
   ros2 bag play ./d640-bag
   ```

回放不会自动打开窗口。另开已加载环境的终端运行 `rviz2`，按[在 RViz 中添加画面](#在-RViz-中添加画面)选择录制的话题。点云的 **Global Options → Fixed Frame** 默认填 `depth_optical_frame`，显示为空时将话题的 **Reliability Policy** 设为 **Best Effort**。回放时不要运行 view，它会再次启动相机。

### 不打开图形窗口采集

通过 SSH 操作或无需看图时，使用 start 替代 view：

```bash
ros2 run maixsense_d640_driver maixsense_d640 start
```

保存、查询和录制仍在另一个已加载环境的终端执行。结束采集时，在启动终端按 **Ctrl+C**。

## 下一步

- 编写自己的数据处理程序，见 [SDK 开发指南](./sdk.md)及 SDK 内的 `ros2/README.zh-CN.md`。
- 设备连接和访问权限问题，见[快速上手](./quick-start.html)。
