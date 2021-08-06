---
title: Sipeed Wiki - 资料和文档
keywords: sipeed, wiki, 文档, 开源软件, 开源硬件, Lichee, 荔枝派, AI, AIOT, 边缘计算, 人脸识别, 嵌入式AI, maixpy, maixpy3
desc: Sipeed的文档（Wiki），包含了开源软件和开源硬件资料，AIOT资料等等
id: wiki_home
---


<div>
    <script src="/static/js/jquery.fullpage.min.js"></script>
    <link rel="stylesheet" href="/static/css/jquery.fullpage.min.css" type="text/css"/>
</div>

<div id="fullpage">
    <div class="section" style="height: 100vh;">
        <div>
            <h1>Sipeed Wiki - 资料和文档</h1>
        </div>
        <div>
            <a href="./soft/maixpy/zh/readme.md"><img src="/static/image/MaixPy.png"></a>
            <a href="./soft/Lichee/zh/readme.md"><img src="/static/image/licheepi.png"></a>
            <a href="./soft/Tang/zh/index_bak.md"><img src="/static/image/tang.png"></a><br/>
            <a href="./soft/longan/zh/readme.md"><img src="/static/image/longan.png"></a>
            <a href="https://dl.sipeed.com/" target="_blank"><img src="/static/image/DOWNLOAD.png"></a>
            <a href="https://bbs.sipeed.com/" target="_blank"><img src="/static/image/BBS.png"></a>
        </div>
    </div>
</div>

<div>
<script type='text/javascript'>
    $(document).ready(function () {
        var html = $("#page_footer").html();
        $("#page_footer").remove();
        $("#fullpage").append('<div id="page_footer" class="section fp-auto-height">' + html + "</div>");
        var nav_height = $("#navbar").height();
        $('#fullpage').fullpage({
            menu: '#navbar',
            navigation: true,
            css3: true,
            dragAndMove: true,
            paddingBottom: nav_height + "px"
            // fixedElements: "#navbar"
        });
        $("#to_top").on("click", function(){
            $.fn.fullpage.moveTo(1);
        });
    });
</script>
</div>



