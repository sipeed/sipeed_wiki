# 固件与标定管理

## 固件更新

MaixSense-D640 支持三种固件更新方式：

### 方式一：GUI 更新（推荐）

1. 打开 GUI 应用，连接设备
2. 点击设备菜单 → "固件更新"
3. 选择固件包 (`maixsense_d640-*.tar.gz`)
4. 等待上传进度完成
5. 设备自动重启

### 方式二：命令行工具

```bash
# 使用 SDK 工具
./msd-upload firmware maixsense_d640-v1.0.tar.gz --restart
```

通过 USB 批量传输直接写入设备，无需网络连接。

### 方式三：SSH 手动部署

```bash
# 登录设备
ssh root@10.253.24.1    # 密码: sipeed

# 停止服务
systemctl stop maixsense-d640

# 上传新固件
scp maixsense_d640_live root@10.253.24.1:/opt/maixsense-d640/

# 重启服务
systemctl restart maixsense-d640
```

### 固件更新说明

- 固件更新**不会覆盖**标定数据 (`calibration/` 目录被跳过)
- 更新前设备会自动验证包的 SHA256 校验和
- 失败时自动回滚，不会导致设备变砖

## 标定文件管理

标定数据决定深度精度，每台设备出厂时已预置标定。

### 上传新标定

**GUI 方式：**
1. 设备菜单 → "上传标定"
2. 选择标定目录或包文件
3. 设备自动备份旧标定并应用新数据
4. 重启后生效

**命令行方式：**
```bash
./msd-upload calibration calib.tar.gz --restart
```

**SSH 方式：**
```bash
scp -r calibration/ root@10.253.24.1:/opt/maixsense-d640/calibration/
ssh root@10.253.24.1 "systemctl restart maixsense-d640"
```

### 下载当前标定

```bash
# 命令行
./msd-upload fetch-calibration current_calib.tar.gz

# SSH
ssh root@10.253.24.1 "tar czf - -C /opt/maixsense-d640 calibration" > calib_backup.tar.gz
```

### 恢复历史标定

GUI 方式：设备菜单 → "标定管理" → 选择历史备份版本

命令行方式：
```bash
# 在设备上查看备份
ssh root@10.253.24.1 "ls /opt/maixsense-d640/calibration.bak-*"

# 恢复指定备份
ssh root@10.253.24.1 "
  mv /opt/maixsense-d640/calibration /opt/maixsense-d640/calibration.current
  mv /opt/maixsense-d640/calibration.bak-20261023 /opt/maixsense-d640/calibration
  systemctl restart maixsense-d640
"
```

### 标定文件格式

标定包需包含以下文件：

```
calibration/
├── stereo_calib.ini              # INI 格式，必须含 [P1] [P2] [Q] 段
├── stereo_calib_left_mesh.bin    # 左目 GDC 校正网格 (9504 bytes)
└── stereo_calib_right_mesh.bin   # 右目 GDC 校正网格 (9504 bytes)
```

## 设备目录结构

```
/opt/maixsense-d640/
├── maixsense_d640_live           # 主固件二进制
├── VERSION                       # 版本号
├── manifest.sha256               # 文件校验和
├── bin/msd_file_service          # USB 文件传输守护进程
├── lib/                          # 运行时库
├── models/620E.axmodel           # 深度 NPU 模型
├── calibration/                  # 标定数据（更新时保留）
└── scripts/
    ├── maixsense-d640-start.sh
    ├── maixsense-d640-stop.sh
    ├── maixsense-d640-uvc-gadget.sh
    └── maixsense-d640.service
```

## systemd 服务

```bash
# 查看状态
systemctl status maixsense-d640

# 重启
systemctl restart maixsense-d640

# 查看日志（日志在 tmpfs，断电后丢失）
cat /run/log/maixsense-d640/current.log

# 查看上一次运行日志
cat /run/log/maixsense-d640/previous.log
```

> 日志存放在 `/run/log/maixsense-d640/`（tmpfs），不占用 NAND Flash，重启后清空。最大 4MB 自动轮转。
