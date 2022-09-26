---
title: 使用 TinyMaix 将模型部署到单片机
date: 2022-09-15
---

<div id="title_card">
    <div class="card" style="background-color: #fafbfe">
        <img src="../../assets/m0_small.png" alt="TinyMaix 模型转换和部署">
        <div class="card_info card_green">
            <div class="title">TinyMaix 平台</div>
            <div class="brief">
                <div>单片机通用，为各种指令集优化</div>
                <div>算力具体看硬件 CPU，有限算子加速</div>
            </div>
        </div>
    </div>
</div>
<style>
#title_card {
    width:100%;
    text-align:center;
    background-color: #fafbfe;
    margin-bottom: 1em;
}
#title_card img {
  max-height: 20em;
}
.card_green {
    background-color: #b2dfdb;
    color: #009688;
}
.dark .card_green {
    background-color: #004e03;
    color: #ffffffba;
}
.title {
    font-size: 1.5em;
    font-weight: 800;
}
</style>

[TinyMaix](https://github.com/sipeed/TinyMaix) 是针对小算力小内存的芯片设计的轻量级推理框架，甚至能在`2KB`内存的`Arduino ATmega328`单片机上运行`MNIST`，对各种架构的单片机都提供了支持和优化，包括 RISC-V、ARM Cortex-M 等。


详细使用方法请看[TinyMaix 官方仓库](https://github.com/sipeed/TinyMaix)




