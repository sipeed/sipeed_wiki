---
title: SLogic Agent Stories
keywords: SLogic, Agent, Story, SLogic32U3
update:
  - date: 2026-08-07
    version: v0.2
    author: taorye
    content:
      - Added a campaign summary table highlighting coupon limits and restrictions
  - date: 2026-08-06
    version: v0.1
    author: taorye
    content:
      - Added SLogic Agent story rewards and submission rules
---

| Campaign information | Details |
|---|---|
| Starts | August 8, 2026 |
| Ends | The day SLogic32U3 is officially listed for sale by Sipeed |
| Submission method | Open a Pull Request against the official [`sipeed/sipeed_wiki`](https://github.com/sipeed/sipeed_wiki) repository |
| Submission content | A real problem solved with an Agent and `sigrok-cli-slogic`, plus specific suggestions for improvement |
| Reward | **SLogic32U3 discount coupon worth up to USD 30** |
| Redemption period | Valid only during the SLogic32U3 launch week; expires when that week ends |
| Recipient | May be used only by the winner; it may not be transferred, gifted, or traded |
| Selection | Eligible submissions are ranked, with a lottery among the remaining eligible entries |
| To be announced | Coupon tiers and minimum-spend requirements, reward count, ranking publication method, and lottery rules |

## SLogic Agent Story Rewards

If you used an Agent and `sigrok-cli-slogic` to solve a real problem, you may submit the story together with suggestions for improvement. Selected submissions may help improve the guide, the Plugin workflow, and practical examples for the upcoming SLogic32U3.

### Campaign Period

The campaign starts on August 8, 2026 and ends on the day SLogic32U3 is officially listed for sale by Sipeed. This page will be updated with the closing date when the official listing is announced.

### How to Submit

To submit, open a Pull Request against the official [`sipeed/sipeed_wiki`](https://github.com/sipeed/sipeed_wiki) repository. Put Chinese stories in `docs/hardware/zh/logic_analyzer/slogic_agent/stories/` and English stories in `docs/hardware/en/logic_analyzer/slogic_agent/stories/`. The PR must also update the corresponding `sidebar.yaml` and add the article under **SLogic Agent 故事分享** for Chinese or **SLogic Agent Stories** for English. An external link by itself, or story text included only in the PR description, is not a submission.

> Tip: If you are unfamiliar with the Wiki directory layout or sidebar configuration, ask an Agent that can work with Git repositories to place the Markdown file, add the navigation entry, and verify rendering. You may also study the `sipeed_wiki` contribution documentation and do it yourself. For example: “Put my story Markdown in the SLogic Agent stories directory in `sipeed_wiki`, update the sidebar for the correct language, and check that links, images, and the page render correctly. Do not modify unrelated files.”

### Submission Format

Submissions must use Markdown and include every required field below. Incomplete submissions are not eligible for evaluation.

| Field | Requirement |
|---|---|
| Title | State the problem solved in one sentence |
| Context | Describe the target, objective, and original difficulty; omit unrelated background |
| Hardware and environment | SLogic model, operating system, protocol, and necessary software versions |
| Wiring and capture settings | Channel mapping, sample rate, duration/sample count/frame count, and trigger conditions |
| Agent prompts | Preserve the important original prompts; for long conversations, include only the parts that affected the result |
| Analysis result | Decoder, pin mapping, options, key data, warnings, and verification method |
| Evidence | Include only the waveform screenshots, decode excerpts, or reproduction steps needed to support the result; do not publish sensitive data |
| Suggestions | Identify a specific improvement to the documentation, Plugin workflow, or SLogic32U3 user experience |

Submissions must describe the author's own real use. Remove secrets, device serial numbers, customer data, and other sensitive information. Images must show relevant channel names and waveform details clearly. A conclusion without supporting details, promotional copy, an unreproducible screenshot, or an AI-generated experience is not eligible.

### Selection and Rewards

We will first check whether a submission is complete, authentic, and reproducible. Eligible submissions will then be ranked by technical completeness, reproduction value, clarity, and whether the suggestions can be acted on. Top-ranked entries, shortlisted entries, and entries selected by lottery from the remaining eligible submissions will receive different tiers of SLogic32U3 discount coupons.

The English page shows the international reward, worth up to USD 30. The applicable reward region is determined by the shipping address used to purchase SLogic32U3: addresses in mainland China follow the domestic reward rules, while other addresses follow the international reward rules. The submission language does not affect the reward tier. Each coupon may be used only by its recipient during the SLogic32U3 launch week. It expires when that week ends and may not be transferred, gifted, or traded.

The specific coupon tiers and minimum-spend requirements, the number of rewards, the ranking publication method, and lottery rules will be announced on this page. Eligibility is determined from the article included in the PR and the format requirements above.
