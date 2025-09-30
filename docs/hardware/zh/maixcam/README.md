---
title: MaixCAM -- 快速落地 AI 视觉、听觉项目
---

<script src="/static/js/tailwind.js"></script>

<style>
    #content_body .h1 {
        font-size: 2.2em;
        font-weight: 800;
    }
    .flex_center {
        display:flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    #content_body .card_item {
        color: #f0f5f9;
        background: linear-gradient(90deg, #26d0ce, #1a2980);
        border-radius: 1em;
        padding: 1em;
        margin: 1em 0.1em;
    }
    #content_body .card_item img {
        transition: transform 0.4s ease;
    }
    #content_body .item2 {
        width: 90%;
        align-self: start;
        background: linear-gradient(-45deg, #c471ed,  #f64f59);
    }
    #content_body .item3 {
        width: 90%;
        align-self: end;
        background: linear-gradient(-45deg, #12c2e9, #c471ed);
    }
    #content_body .card_item:visited {
        color: #f0f5f9;
    }
    #content_body .card_item:hover {
        border-radius: 1em;
        background: linear-gradient(70deg, #26d0ce, #1a2980);
        padding: 1em;
        margin: 1em 0.1em;
    }
    #content_body .item2:hover {
        background: linear-gradient(-20deg, #c471ed,  #f64f59);
    }
    #content_body .item3:hover {
        background: linear-gradient(-20deg, #12c2e9, #c471ed);
    }
    #content_body .card_item:hover > img {
        transform: rotate(10deg) scale(1.3) ;
    }
    .cams_wrapper {

    }
    .mask_wrapper {
        position: relative;
    }
    .mask {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .item_name {
        font-size: larger;
        font-weight: 800;
    }
    #content_body .btn_blue {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #0b4294;
    }
    #content_body .btn_blue:visited {
        color: white;
    }
    #content_body .btn_blue:hover {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #082a5e;
    }
    #content_body .btn_red {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #ad3838
    }
    #content_body .btn_red:visited {
        color: white;
    }
    #content_body .btn_red:hover {
        margin: 1em;
        color: white;
        font-size: 0.9em;
        border-radius: 0.3em;
        padding: 0.5em 2em;
        background-color: #630606;
    }

    .dark #content_body .card_item {
        color: #f0f5f9;
    }
    .dark #content_body a.card_item:visited {
        color: #f0f5f9;
    }
    .dark .card_item {
        background: #292929;
    }
    @media screen and (max-width: 768px) {
        #content_body .item1 {
            flex-direction: column-reverse;
        }
        #content_body .item1 img {
            padding-bottom: 1em;
        }
        #content_body .item2 {
            width: 98%;
        }
        #content_body .item3 {
            width: 98%;
        }
    }
</style>

<div style="width:100%;" class="flex_center">

<!-- ![MaixCAM](../../assets/maixcam/maixcam.jpeg) -->


</div>

<div style="margin-bottom: 4em"></div>

<div class="flex_center w-full cams_wrapper">
    <div class="flex flex-row w-full">
        <a href="./maixcam2.html" class="flex flex-row items-center justify-around w-full card_item mask_wrapper item1">
            <div class="item_name">MaixCAM2</div>
            <img src="/static/image/maixcam2_small.png">
            <div class="mask"></div>
        </a>
    </div>
    <div class="flex flex-row w-full justify-between">
        <div class="flex_center flex-row w-1/2 justify-start">
            <a href="./maixcam.html" class="flex_center card_item mask_wrapper item2">
                <img src="/static/image/maixcam_small.png">
                <div class="item_name pt-8">MaixCAM</div>
                <div class="mask"></div>
            </a>
        </div>
        <div class="flex_center flex-row w-1/2 justify-end">
            <a href="./maixcam_pro.html" class="flex_center card_item mask_wrapper item3">
                <img src="/static/image/maixcam_pro_small.png">
                <div class="item_name pt-8">MaixCAM-Pro</div>
                <div class="mask"></div>
            </a>
        </div>
    </div>
</div>


<div class="center mb-20"></div>


<div style="padding: 1em 0 0 0; display: flex; justify-content: center">
    <a target="_blank" class="btn_blue" href="https://wiki.sipeed.com/maixpy/">MaixPy </a>
    <a target="_blank" class="btn_blue" href="https://wiki.sipeed.com/maixcdk/">MaixCDK</a>
        <a target="_blank" class="btn_blue" href="https://maixhub.com">MaixHub 在线模型训练</a>
        <a target="_blank" class="btn_blue" href="https://maixhub.com/app">MaixHub 应用商店</a>
</div>

<div style="padding: 1em 0 0 0; display: flex; justify-content: center">
    <a target="_blank" class="btn_red" href="https://item.taobao.com/item.htm?id=784724795837">淘宝</a>
    <a target="_blank" class="btn_red" href="https://www.aliexpress.com/store/911876460">速卖通</a>
</div>

