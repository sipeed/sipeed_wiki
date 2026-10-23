# 常见问题

## 连接问题

### 连接后没有识别到设备

1. 确认使用的是**数据线**而非充电线
2. 设备上电后需要约 **10 秒**完成初始化
3. Linux 下运行 `lsusb` 确认设备出现
4. Windows 检查设备管理器 → "照相机"是否有 4 个 UVC 设备
5. 尝试更换 USB 端口（建议使用主板直连端口，避免 Hub）

### SSH 连接不上设备

- 确认 USB NCM 网络接口已获取到 IP
- Linux：`ip addr` 查看 `usb0` 或 `enx*` 接口
- Windows：设备管理器 → "网络适配器" 查看 NCM/RNDIS 设备
- 设备默认 IP `10.253.24.1`，密码 `sipeed`
- 如果 IP 不通，尝试 `ping` 或检查子网配置

### macOS 无法使用深度滤波/曝光控制

macOS 的 UVC 驱动不支持本设备的厂商扩展描述符。这些功能通过 NCM 网络通道实现：

- GUI：设置 → 连接方式 → 选择 NCM
- SDK：`MSD_CAPTURE_TRANSPORT=ncm` 环境变量
- UVC 预览（QuickTime/VLC）不受影响

## 深度图像问题

### 深度图帧率只有 12fps

这是正常的。深度帧率由 NPU 推理速度决定（AX620Q 800MHz NPU，约 75ms/帧），设备描述符声明 12fps。IR 流可独立达到 30fps。

### 深度图有黑色区域

黑色像素表示深度无效（像素值 = 0），常见原因：

- **物体反光或透明**：玻璃、镜面金属、光滑塑料会导致双目匹配失败
- **超出测量范围**：短基线 >2m 或长基线 >3m 时精度下降，低置信度像素被过滤
- **遮挡区域**：物体边缘因两个摄像头视角不同产生的遮挡带
- **纹理不足**：纯色、无纹理的平面区域难以进行立体匹配

**优化建议**：
- 降低置信度阈值（GUI 或 SDK 中设置，例如从 0.5 降到 0.3）
- 增加场景纹理（投射结构光或纹理图案）
- 确保 IR 补光灯正常工作

### 深度值如何转换为毫米

使用 Z16 格式打开 Raw Depth 流时，每个像素是 `uint16_t` 类型，**单位直接就是毫米**。值为 0 表示无效像素。

### IR 流能否输出 Raw YUV

目前 IR 流仅支持 MJPEG 格式。Raw YUV (NV12) 在 USB 2.0 带宽下不可行：

- 单目 NV12 640×480@30fps = 110 Mbps
- 双目 = 220 Mbps
- 加上深度流 = 266 Mbps
- USB 2.0 HS ISO 可用带宽仅 ~280 Mbps

如需 Raw 灰度数据，可通过 MJPEG 解码获取（JPEG quality 70，压缩比约 12:1）。

## 固件问题

### 标定数据丢失

标定数据独立于固件存储，固件更新不会覆盖它。如需恢复：

```bash
# 下载当前标定（备份）
./msd-upload fetch-calibration backup.tar.gz

# 上传标定
./msd-upload calibration new_calib.tar.gz --restart
```

也可在 GUI 中操作：设备菜单 → "标定管理"。

### 固件更新后无法启动

1. SSH 登录设备：`ssh root@10.253.24.1`
2. 查看日志：`cat /run/log/maixsense-d640/current.log`
3. 检查服务状态：`systemctl status maixsense-d640`
4. 手动重启：`systemctl restart maixsense-d640`

### 设备发热

AX620Q SoC 在持续运行 NPU 推理时会有一定发热，属于正常现象。典型功耗约 1.5W。建议：
- 保持通风良好
- 避免密封环境长时间运行
- 环境温度 0°C ~ 50°C

## 性能问题

### 延迟太高

当前设备侧延迟约 126ms（NPU 推理 75ms + 后处理 18ms + 其他开销），加上 USB 传输 27ms，端到端约 153ms。这是 USB 2.0 + AX620Q NPU 的硬件极限。

如需更低延迟：
- 确认使用的是 800MHz NPU 固件（可查看 `cat /proc/ax_proc/npu/clk`）
- 减少 USB Hub 层级（直连主板端口）
- 考虑使用支持 USB 3.0 的未来硬件版本
