---
title: Sipeed Wiki - Documentation
keywords: sipeed, wiki, documentation, open source, open source hardware, Lichee, Lichee PI, AI, AIOT, edge AI, face recognization
desc: Wiki of Sipeed, include software documentation and hardware infomation, and AIOT data etc.
id: wiki_home
---


<div>
    <script src="/static/js/scrolloverflow.min.js"></script>
    <script src="/static/js/jquery.fullpage.min.js"></script>
    <link rel="stylesheet" href="/static/css/jquery.fullpage.min.css" type="text/css"/>
</div>

<div id="fullpage">
    <div class="section" style="height: 100vh;">
        <div>
            <h1>Sipeed Wiki - Documentation</h1>
        </div>
        <div>
            <a href="./soft/maixpy/zh/index.html"><img src="/static/image/MaixPy.png"></a>
            <a href="./soft/Lichee/zh/index.html"><img src="/static/image/licheepi.png"></a>
            <a href="./soft/Tang/zh/index_bak.html"><img src="/static/image/tang.png"></a><br/>
            <a href="./soft/longan/zh/index.html"><img src="/static/image/longan.png"></a>
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
            scrollOverflow: true,
	        scrollOverflowReset: true,
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



