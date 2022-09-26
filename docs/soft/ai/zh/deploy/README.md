---
title: 制作可部署到边缘设备的模型和部署方法汇总
keywords: 模型部署, 模型转换, 模型部署边缘设备
desc: 汇总如何部署模型到边缘设备的相关文档，边缘设备包含单片机、SBC、SOC、NPU等。
date: false
class: heading_no_counter
---

<div id="maixhub">
    到<a href="https://maixhub.com/model/zoo">MaixHub 查看</a>或<a href="https://maixhub.com/model/zoo/share">上传分享</a>能直接部署到边缘设备的模型
</div>

<div id="deploy_items">
    <a href="./k210.html">
        <div class="card">
            <img src="/hardware/zh/maix/assets/dk_board/maix_duino/maixduino_0.png" alt="K210 模型转换和部署">
            <div class="card_info card_red">
                <h2>Maix-I 系列 K210</h2>
                <div class="brief">
                    <div>高性价比带硬件 AI 加速的单片机</div>
                    <div>1Tops@INT8，有限算子加速</div>
                </div>
            </div>
        </div>
    </a>
    <a href="./v831.html">
        <div class="card">
            <img src="/hardware/assets/maixII/m2dock.jpg" alt="V831 模型转换和部署">
            <div class="card_info card_blue">
                <h2>Maix-II 系列 v831</h2>
                <div class="brief">
                    <div>高性价比带硬件 AI 加速，支持 Linux</div>
                    <div>0.2Tops@INT8，有限算子加速</div>
                </div>
            </div>
        </div>
    </a>
    <a href="./tinymaix.html">
        <div class="card" style="background-color: #fafbfe">
            <img src="../../assets/m0_small.png" alt="TinyMaix 模型转换和部署">
            <div class="card_info card_green">
                <h2>TinyMaix 平台</h2>
                <div class="brief">
                    <div>单片机通用，为各种指令集优化</div>
                    <div>算力具体看硬件 CPU，有限算子加速</div>
                </div>
            </div>
        </div>
    </a>
    <a href="./ax-pi.html">
        <div class="card" style="background-color: #fafbfe">
            <img src="../../assets/maix-iii-small.png" alt="AX-Pi 模型转换和部署">
            <div class="card_info card_purple">
                <h2>Maix-III 系列 AX-Pi</h2>
                <div class="brief">
                    <div>高算力、独特 AI-ISP 影像系统</div>
                    <div>最高 3.6Tops@INT8，丰富算子支持</div>
                </div>
            </div>
        </div>
    </a>
</div>

<style>
#deploy_items {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    margin: 0 -10px;
}
#deploy_items a:hover {
    background-color: transparent;
}
#deploy_items > a {
    margin: 1em;
}
.card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    box-shadow: 5px 6px 20px 4px  rgba(0, 0, 0, 0.1);
    border-radius: 0.6rem;
    transition: 0.4s;
    background: white;
}
.card:hover {
    box-shadow: 5px 6px 40px 4px  rgba(0, 0, 0, 0.1);
    scale: 1.05;
}
.card_info {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 0 0 0.6rem 0.6rem;
}
.card img {
    height: 10em;
    width: 14em;
    object-fit: cover;
}
.card_info > h2 {
    font-size: 1.2em;
    margin: 0.2em;
    padding: 0.2em 1em;
}
.card_info > .brief {
    margin: 0.2em;
    padding: 0.2em 1em;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.card_red {
    background-color: #ffcdd2;
    color: #cf4f5a;
}
.card_blue {
    background-color: #90caf9;
    color: #105aa9;
}
.card_green {
    background-color: #b2dfdb;
    color: #009688;
}
.card_purple {
    background-color: #d1c4e9;
    color: #673ab7;
}
#maixhub {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1em 0;
    width: 100%;
    background-color: #f5f5f5;
    color: #727272;
    border-radius: 0.6rem;
    padding: 1em;
}
.dark #maixhub {
    background-color: #2d2d2d;
    color: #bfbfbf;
}
.dark .card_blue {
    background-color: #003c6c;
    color: #ffffffba;
}
.dark .card_red {
    background-color: #5a0000;
    color: #ffffffba;
}
.dark .card_green {
    background-color: #004e03;
    color: #ffffffba;
}
.dark .card_purple {
    background-color: #370040;
    color: #ffffffba;
}
</style>



