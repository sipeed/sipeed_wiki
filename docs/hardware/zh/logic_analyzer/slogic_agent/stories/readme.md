---
title: SLogic Agent 故事分享
keywords: SLogic, Agent, Story, SLogic32U3
update:
  - date: 2026-08-06
    version: v0.1
    author: taorye
    content:
      - 增加 SLogic Agent 故事悬赏和投稿规则
---

## SLogic Agent 故事悬赏

如果你使用 Agent 和 `sigrok-cli-slogic` 解决了真实问题，欢迎提交使用故事和改进建议。入选内容将用于完善教程及 Plugin，也会帮助我们为新品 SLogic32U3 准备更贴近实际需求的示例。

活动从 2026 年 8 月 8 日开始，至 SLogic32U3 由 Sipeed 正式官方上架当天结束。结束时间将随 SLogic32U3 上架信息在本页更新。

投稿方式：向官方 [`sipeed/sipeed_wiki`](https://github.com/sipeed/sipeed_wiki) 仓库提交 Pull Request。中文故事放在 `docs/hardware/zh/logic_analyzer/slogic_agent/stories/`，英文故事放在 `docs/hardware/en/logic_analyzer/slogic_agent/stories/`。PR 还须修改对应语言的 `sidebar.yaml`，将文章添加到中文的 **SLogic Agent 故事分享** 或英文的 **SLogic Agent Stories** 分组；只提交外部链接或仅在 PR 描述中粘贴正文不计为投稿。

> 提示：如果不熟悉 Wiki 目录和 sidebar 配置，可以让支持操作 Git 仓库的 Agent 协助放置 Markdown、添加导航并检查渲染，也可以自行查阅 `sipeed_wiki` 的贡献文档。例如：“请把我的故事 Markdown 放到 `sipeed_wiki` 的 SLogic Agent stories 目录，更新对应语言的 sidebar，并检查链接、图片和页面能否正常渲染。不要修改无关文件。”

投稿须使用 Markdown，并按以下字段组织；缺少必填项的内容不进入评选：

| 字段 | 要求 |
|---|---|
| 标题 | 用一句话说明解决了什么问题 |
| 使用背景 | 说明被测对象、目标和原有困难，不写无关经历 |
| 硬件与环境 | SLogic 型号、操作系统、协议和必要的软件版本 |
| 接线与采集参数 | 通道映射、采样率、时长/样本数/帧数、触发条件 |
| 给 Agent 的提示词 | 保留关键原文；较长对话只摘录影响结果的部分 |
| 分析结果 | decoder、引脚映射、选项、关键数据、warning 和验证方法 |
| 证据 | 提供必要的波形截图、解码片段或可复现步骤，不上传敏感数据 |
| 改进建议 | 明确指出希望改进的文档、Plugin 流程或 SLogic32U3 使用体验 |

投稿必须为本人真实使用记录，并移除密钥、设备序列号、客户数据等敏感信息。图片应能看清通道名和关键波形；不要只提交结论、宣传文案、无法复现的截图或由 AI 编造的经历。

我们会先检查内容是否完整、真实且可复现，再根据技术完整度、复现价值、表达清晰度和建议的可执行性进行排名。排名靠前、进入候选名单以及从其余合格投稿中抽取的内容，将分别获得不同等级的 SLogic32U3 满减券。

满减券按地区发放：国内奖励最高为 200 CNY，海外奖励最高为 30 USD。满减券仅限获奖者本人在 SLogic32U3 首发周购买该产品时使用，首发周结束后自动失效，不得转赠或交易。

满减券的具体档位与使用门槛、名额、排名公布方式和抽奖规则将在本页另行公布。投稿是否合格以 PR 中的文章内容和上述格式要求为准。
