# TODO — 待补内容清单

这里记录"文档已上线，但还缺素材或待确认"的事项。每条写明**缺什么、补齐后改哪里**。

- 提交前请对照本清单：手头的改动如果能顺带完成某一条，就一起做掉并把它勾选或删除；做不了的保持原样。
- 新发现的缺口随手加进来，写清楚完成条件，不要只写"待完善"。
- 本仓库是公开仓库：这里只记文档层面的待办，不写内部问题、内网地址和未公开的计划。

## SPI2HDMI 模块

- [x] **产品图**（2026-11-28 已换成实拍）：首页卡片 `static/home/spi2hdmi.jpg` 和正文开头的正反面图 `assets/DCIM/spi2hdmi-front-back.jpg`。照片是手机拍的，分辨率一般，有更好的图时可再替换。
- [ ] **购买链接**
  - `layout/modules.html`：SPI2HDMI 卡片的"购买"按钮现在是置灰状态（`disabled: true`）。有链接后填入 `link`、删掉 `disabled`，并在 `layout/locales/en/LC_MESSAGES/messages.po` 里给出对应的海外链接。
  - `docs/hardware/{zh,en}/modules/spi2hdmi/spi2hdmi.md` 末尾"相关链接"里的"购买：敬请期待"同步替换。
- [ ] **演示视频换成拉正的版本**：`assets/DCIM/demo-*.mp4` 是手持拍屏幕的原始画面。可按显示器四角做透视校正后重新导出（静态图已验证效果明显更好），仍需满足 AGENTS.md §6 的体积上限。
- [x] ~~左上角分形演示的运行平台未确认~~：2026-11-28 左上角换成了 STC8G1K17A 的演示（`assets/DCIM/demo-stc8.mp4`），原来的分形片段已删除。
- [ ] **待实测的规格**：供电电流（现写"5V，约 0.1A"，为预估值）、TE 脉宽（现为设计值）。实测后更新规格表和"复位与 TE"一节，注意跨页参数一致。
- [ ] **尺寸图**：`assets/MISC/dimensions.svg` / `dimensions_en.svg` 已按 PCB 数据画好，但正文还没引用。确认需要后加到"规格"一节。
- [ ] **短链上线后验证**：`pages/index/zh/spi2hdmi.html` 部署后，确认 `wiki.sipeed.com/spi2hdmi` 能按浏览器语言跳转（例程仓库 README 和产品二维码都指向这个地址）。

## MA-USB8 麦克风阵列驱动板

- [ ] **卡片图**：`static/home/ma_usb8.jpg` 现在用的是文档里的 3D 渲染图（紫灰底），与同组白底卡片不统一。换成白底产品图，600×450。

## 首页与翻译

- [ ] **英文翻译里有 3 条历史遗留的 fuzzy 条目**（`layout/locales/en/LC_MESSAGES/messages.po`，来源 `maix.html` 第 206、223、355 行附近）。fuzzy 条目不会编进 `.mo`，英文首页对应位置会显示中文原文。需要对应产品负责人核对译文后去掉 `#, fuzzy`，核对方法见 AGENTS.md §9。
