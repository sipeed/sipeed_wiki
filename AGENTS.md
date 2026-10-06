# AGENTS.md — sipeed_wiki 编写指南

> 面向 AI 助手 / 自动化协作者。人类贡献者请先看 [README.md](./README.md) 与 [share_docs/zh/readme.md](./share_docs/zh/readme.md)。
> For AI agents working on this repo. Written in Chinese because the source language of this wiki is Chinese; English docs are translations.

## 0. 四条铁律

1. **不编造参数。** 事实只能来自：用户确认、官方 GitHub 仓库 / Release、官网、实物实测。拿不准就问，不要推测后当事实写。
2. **不动别人的目录。** 本仓库多个产品线共用，只改你负责的产品目录与明确授权的公共文件。
3. **不写内部信息。** 本仓库是公开仓库。内网地址、NAS/共享盘路径、本机绝对路径、内部工具链接、人员账号、密钥，一律不进文档、不进注释、不进示例命令。粘贴日志前先脱敏。
4. **改完必须本地构建 + 浏览器截图自检。** 只看代码不算验证，这里的坑大多只在构建产物里暴露。

---

## 1. 仓库结构

```
docs/hardware/zh/           中文硬件文档（主语种，图片实体都放这里）
docs/hardware/en/           英文译本（文件名必须与 zh 一一对应）
docs/hardware/{zh,en}/sidebar.yaml   左侧导航，中英各一份
docs/soft/                  软件文档（maixpy / longan / Tang ...）
pages/index/{zh,en}/        首页、短链页、404
layout/*.html               首页与分类页模板（home.html、slogic.html、maix.html ...）
layout/locales/             babel 翻译；.po/.pot 入库，.mo 构建时生成（已 gitignore）
static/                     全站静态资源（首页卡片图、轮播 banner）
site_config.json            route（路由）/ translate（双语映射）/ plugins
out/                        构建产物，gitignore
```

路由在 `site_config.json` 的 `route.docs` 里，例如 `/hardware/zh/` → `docs/hardware/zh`。
新增产品目录不需要改 `site_config.json`，只需放进已有路由下并加侧边栏条目。

---

## 2. 本地预览与构建

在仓库根目录执行：

```bash
uv sync                                          # 从 pyproject.toml/uv.lock 建 .venv，已含 teedoc 及全部插件
uv run teedoc serve --host 127.0.0.1 --port 2333  # http://127.0.0.1:2333
```

**什么时候必须干净全量构建**（增量构建会骗你）：重命名或删除文档、改 `sidebar.yaml` 结构、改 `layout/` 或 `locales/`。

```bash
pkill -f 'teedoc.*serve'                # 注意别让 pattern 匹配到你自己这条命令
rm -rf out
mkdir -p /tmp/teedoc_plugin_search      # 不建会报 FileNotFoundError .../index_0.json
.venv/bin/python -m teedoc build
```

**watch 范围**：`teedoc serve` 只可靠监听 `docs/`。
- 改了 `layout/` → touch 一下引用它的模板，或直接全量重建；
- 改了 `static/` 下的图 → 手动 `cp` 到 `out/static/...`，否则浏览器看到的还是旧图。

---

## 3. 产品文档的标准结构

参考 `logic_analyzer/slogic16u3` 与 `logic_analyzer/slogic32u3`，一个产品拆 5 页，不要堆成一篇长文：

| 文件 | 回答读者的哪个问题 |
|---|---|
| `Introduction.md` | 这是什么？能干什么？给谁用？（核心特性、规格表、产品图、相关链接） |
| `Quick_Start.md` | 我怎么把它跑起来？（开箱 → 装软件 → 驱动权限 → 连接 → 接线接地 → 第一次采集 → 查看解码 → 下一步） |
| `Hardware_Specification.md` | 硬件上有什么？（接口与引脚、指示灯、尺寸、配件、电气参数） |
| `Software_User_Guide.md` | 怎么用深入？（上位机使用、参数取舍、解码、进阶） |
| `FAQ.md` | 我卡住了怎么办？（问句式小标题，一问一答，按主题分组） |

目录下建 `assets/`，图片按 3 个子目录归类（见 §6）。

### frontmatter

每个 md 必须有，`update` 倒序排列（最新在最前）：

```yaml
---
title: SLogic32U3 简介
keywords: LogicAnalyzer, SLogic, SLogic32U3, USB3.2, sigrok, 逻辑分析仪
update:
  - date: 2026-10-06
    version: v0.3
    author: Sipeed
    content:
      - 拆出独立的快速上手页，简介只保留产品与规格
      - 校正数字信号带宽、探头线、ADC 模组等参数表述
  - date: 2026-09-30
    version: v0.1
    author: Sipeed
    content:
      - 初始化文档
---
```

`content` 写**这次改了什么**，一条一句，不要写"更新文档"这种废话。

### 标题层级

文件开头 `# 页面名`，正文从 `##` 起。不要手写 `1.1` `1.2` 这类编号（teedoc 自己生成目录）；只有"快速上手"这类真有先后顺序的步骤才用 `## 1. 开箱` `## 2. 安装软件`。

---

## 4. 中英双语

### 机制

`site_config.json` 的 `translate.docs` 把 `/hardware/zh/` 映射到 `docs/hardware/en`。
**翻译状态是构建期按「相对路径同名」匹配算出来的**：zh 下有 `logic_analyzer/foo/Bar.md`、en 下没有同名文件，英文页顶部就会出现 `This page not translated yet` 横幅。

### 规则

- **重命名中文文件时，必须同步重命名英文文件**，然后干净全量构建（增量构建不重算翻译索引，横幅不会消失，会误导你以为没修好）。
- 校验中英文件是否对齐：

  ```bash
  cd docs/hardware && comm -3 \
    <(cd zh && find . -name '*.md' | sort) \
    <(cd en && find . -name '*.md' | sort)
  ```

  输出中与你产品相关的行应为空。

- **图片只在 zh 下存一份**，英文页用相对路径回引：

  ```markdown
  ![SLogic32U3 product](../../../zh/logic_analyzer/slogic32u3/assets/DCIM/SLogic32U3-hero.jpg)
  ```

- **含文字的图（流程图、接线示意图、标注图）需要出英文版**，命名加 `_en` 后缀，与中文图放同一目录：`gba-channel-map.jpg` / `gba-channel-map_en.jpg`。生成图的脚本也一并保留两份。
- **页内锚点要用目标语言的标题 slug**。中文页 `#采样率与通道数` 在英文页是 `#sample-rate-vs-channel-count`，直接照搬会断链。
- 英文不是中文的逐句直译。中文里的口语化连接词、排比、语气词在英文里删掉；句子拆短，用主动语态。
- `sidebar.yaml` 两份都要改，**英文那份的 label 必须是英文**（最常见的漏网之鱼）。

---

## 5. 侧边栏与短链

`docs/hardware/{zh,en}/sidebar.yaml` 是嵌套的 `label` / `items` / `file`：

```yaml
-   label: SLogic32U3
    items:
    -   label: 简介
        file: ./logic_analyzer/slogic32u3/Introduction.md
    -   label: 快速上手
        file: ./logic_analyzer/slogic32u3/Quick_Start.md
```

侧边栏顺序就是推荐阅读顺序：简介 → 快速上手 → 硬件 → 软件 → FAQ，不要按字母序排。

短链在 `pages/index/zh/<product>.html`，按浏览器语言跳转到简介页。
**文档改名后一定要改这里的目标文件名**，否则 `wiki.sipeed.com/<product>` 直接 404。

---

## 6. 图片

### 来源与质感

- **先确认是否已有正式素材**：动手出图之前，先向产品 / 项目负责人确认该产品有没有现成的官方素材（六视图、透视图、爆炸图、棚拍实拍、电商切片）。**有就优先用现成的**，不要自己另做一套风格不一致的图。素材存放位置向负责人索取，**不要把路径写进文档或注释**。
- **禁用**：工程样机裸板、手机随手拍、桌面/木纹等生活化背景、带水印或截图工具红字的图。
- 产品图统一白底棚拍或渲染。

### 压缩（硬指标）

单张 **<300KB 为宜，500KB 为上限**。现状全站 4332 张图共约 897MB，其中 429 张超 500KB、118 张超 1MB——别再往上加。

```bash
# 检查自己新加的图
find docs/hardware/zh/logic_analyzer/<product> -type f -size +500k -printf '%s\t%p\n' | sort -rn
```

- 照片/渲染：`convert in.jpg -resize '1600x>' -quality 82 out.jpg`，宽度一般不需要超过 1600px。
- 软件截图：PNG 先做调色板量化，仍超标就转 JPG。
- **动图/示意图如果是 html 渲染出来的，去改源 html 的输出尺寸**，不要硬压已经生成的大图。

### 命名与归类

有意义的英文短名 + 连字符，**不要 `a1.jpg` / `IMG_2034.jpg` / `1.png`**：
`view-front-mini-hdmi.jpg`、`dimensions.jpg`、`tpm-spi-setup_en.jpg`。

```
assets/DCIM/         实拍与渲染产品图
assets/Screenshots/  上位机 / 网页截图
assets/MISC/         示意图、接线图、尺寸图、流程图
```

---

## 7. 叙事与可读性（图文并茂、小白友好）

**默认读者是第一次拿到这个产品的人**，不是已经熟悉它的工程师。他不知道缩写，不知道该先做哪一步，也不知道做对了没有。所有写法围绕这一条展开。

### 整站的叙事路线

5 个页面连起来要是一条完整的路：**这是什么 → 怎么跑起来 → 硬件细节 → 软件深入 → 卡住了怎么办**。
页与页之间**显式互链**，不要让读者自己在侧边栏里找：简介页末尾指向快速上手，快速上手每一步引用到硬件页/软件页的对应小节，FAQ 的每个答案链回正文。**每页结尾都要有"下一步"**，不留死胡同。

### 单页内部

- **倒金字塔**：开头 2~3 句说清"它是什么、能干什么、给谁用"，然后才展开。**不要一上来就甩参数表**。
- **先结论后细节**：长表格、长列表前先给一句话结论（"简单说：奇数脚是 GND，偶数脚是信号"），让不想细读的人也能拿走答案。
- **术语首次出现要就地解释或链接**（Stream 模式、阈值电压、annular ring 这类），不要假定读者知道。
- 面向读者用"你"，步骤用动词开头。

### 操作类内容

- **必须是线性编号步骤**，一步一个动作。
- **每步给出可验证的结果**，让读者确认自己做对了："指示灯应变为青色""设备列表里应出现 SLogic32U3"。这是小白和老手体验差别最大的地方。
- 常见失败就地给出口（"如果只亮蓝灯，见 FAQ · 指示灯"），不要让他先失败一次再去翻 FAQ。
- 危险或易错操作用引用块显式告警：接线顺序、电压范围、会清空数据的动作。

  ```markdown
  > ⚠️ 接线前先接地线，且确认被测信号电压在 0~10 V 范围内。
  ```

- **措辞不要把产品写复杂**。例：确认通道线序写"肉眼从第一根依次数过去即可"，而不是"用软件逐根拉高电平确认"——后者让人以为产品难用。

### 图文并茂

- **每一两节配一张图**，不要出现整屏纯文字。
- 按内容选图：概念/数据流用**示意图或 mermaid 流程图**；操作步骤用**界面截图**（关键位置加框标注）；产品形态用**实拍或渲染**；引脚、尺寸用**线稿标注图**。
- 较长的流程在开头先放一张总览图，读者先看懂骨架再读细节。
- 图要有说明文字，`![]()` 的 alt 写清楚图里是什么，不要留空或写 "image1"。
- mermaid 用 ```mermaid 代码块（teedoc 支持）。注意边标签不要太长，否则左侧箭头会被裁掉。

---

## 8. 内容口径

- **上位机 / 软件清单写之前，先去读对应 GitHub 仓库和 Release 资产**，不要凭印象列。
- 未实测的案例或教程，明确标注"方法与预期，非实测结果"。
- **定位性描述按产品负责人拍板的口径**，不要自由发挥。例：ALL LOGIC 写成"基于 DSView 的社区优秀上位机，适合熟悉 DSView 的用户"，不要强调"非官方出品"。
- **跨页参数必须一致**。同一参数会出现在简介、规格表、对比表、首页卡片、短链页多处，改一处后全仓库 grep 一遍：

  ```bash
  grep -rn "350 MHz\|59×51×13" docs/ layout/ pages/
  ```

---

## 9. 首页与 layout

- `layout/slogic.html` 等分类页的产品卡片 **按发布时间顺序排列**，不是新品优先。
- 同一组卡片图必须**同比例、同底色**，否则图文分割线参差。
- 卡片里产品的视觉体量要符合定位：入门款不能画得比旗舰还大。
- 图片居中要按**主体本身**居中，不要按含投影的外接矩形（投影会把主体顶偏）。
- `layout/home.html` 的轮播与文案走 babel i18n。

### babel 的坑（务必手动复查）

构建时 teedoc 会自动跑 `pybabel extract/update`，**新增的 msgid 会被 fuzzy 匹配到无关的旧翻译**（真出过商品链接、按钮文案错配到别的产品）。
而 teedoc 的 `compile_catalog` **不带 `--use-fuzzy`**，所以 fuzzy 条目**根本不会编进 `.mo`**——结果是英文页直接显示中文原文。两种错都要查。

改完 `layout/*.html` 后：

```bash
grep -n -B3 "fuzzy" layout/locales/*/LC_MESSAGES/messages.po
```

逐条核对 `msgstr`：
- 译文正确 → 删掉 `#, fuzzy` 这一行，译文才会生效；
- 译文是乱配的（尤其**商品链接**）→ **不要盲目清 fuzzy**，清了等于把错误链接发布出去；留着 fuzzy 至少会回退到中文原链接，然后找负责人要正确的对照链接再填。

重建后抽查英文产物里有没有中文漏出：

```bash
grep -o '[一-龥]\{2,\}' out/en/index.html | sort -u | head
```

`.mo` 是构建产物（已 gitignore），只提交 `.po` / `.pot`。

---

## 10. 提交前自检清单

- [ ] 干净全量构建通过（`.venv/bin/python -m teedoc build` 输出 build ok）
- [ ] `comm -3` 中英文件名对齐无差异
- [ ] 浏览器实际点一遍：侧边栏每个二级页、短链、页内锚点、所有图片都正常
- [ ] 英文页顶部没有 `This page not translated yet` 横幅；英文页没有中文漏出
- [ ] 新加图片全部 <500KB、命名有意义、放对了 assets 子目录
- [ ] 含文字的图有 `_en` 版本
- [ ] 每页有"下一步"出口，操作步骤有可验证结果
- [ ] 跨页参数一致（grep 过）
- [ ] frontmatter 的 `update` 写了这次的实际改动
- [ ] **没有内网地址、共享盘路径、本机绝对路径、账号或密钥**
- [ ] 只改了自己负责的目录

---

## 11. 坑速查表

| 现象 | 原因 | 解法 |
|---|---|---|
| 英文页顶部 `This page not translated yet` | 改名/删文件后增量构建没重算翻译索引 | 中英文件名对齐 + 干净全量构建 |
| 英文页显示中文原文 | 该条目在 .po 里被标了 `#, fuzzy`，compile 时被跳过 | 核对译文后删掉 `#, fuzzy` 行再重建 |
| 首页商品链接/文案串到别的产品 | babel fuzzy 误配 | 核对后改 `msgstr`；拿不到正确链接就保留 fuzzy |
| 构建报 `FileNotFoundError .../teedoc_plugin_search/index_0.json` | 临时目录不存在 | `mkdir -p /tmp/teedoc_plugin_search` |
| 改了 `layout/` 页面没变化 | serve 不监听 layout | touch 引用它的模板，或全量重建 |
| 改了 `static/` 下的图没变化 | 未同步到 `out/` | `cp` 到 `out/static/...`，或全量重建 |
| 短链 404 | 文档改名后短链目标文件名没跟着改 | 改 `pages/index/zh/<product>.html` |
| 访问目录路径以为 404 | `readme.md` 会构建成该目录的 `index.html` | 直接访问目录路径即可，不是 bug |
| CI 显示构建完成但线上还是 404 | `build_doc_upload` 在对象存储上传步失败（RequestTimeout，teedoc-upload 无重试） | 去 Actions 重跑失败的 job |
| `pkill` 把自己的命令也杀了 | pattern 匹配到了自身命令行 | 用 `pkill -f 'teedoc.*serve'` 之类不自匹配的写法 |

---

## 12. 参考

- 本地预览：http://127.0.0.1:2333
- CI：`.github/workflows/publish.yml`，push 到 main 后构建 → 推 gh-pages → 上传对象存储
- 构建工具文档：[teedoc](https://github.com/teedoc/teedoc)
