---
title: MaixVision Workstation Official Website
---


<div>
<script src="/static/css/tailwind.css"></script>
</div>

<style>
#page_wrapper {
    background-color: #1f2022;
}
.md_page #page_content > div {
    width: 100%;
    max-width: 100%;
}
#file_list_wrapper {
    display: none;
    position: fixed;
    width: 100vw;
    height: 100vh;
    background-color: #000000cc;
    z-index: 1000;
    top: 0;
    left: 0;
}
#file_list {
    background-color: #FAFAFA;
    border-radius: 3px;
    max-width: 80%;
    min-width: 400px;
    max-height: 80%;
    min-height: 200px;
    overflow-y: auto;
}
#maixvision_video {
    height: 35rem;
}
@media (max-width: 1670px) {
    #maixvision_video {
        height: 30rem;
    }
}
@media (max-width: 1280px) {
    #maixvision_video {
        height: 20rem;
    }
}
@media (max-width: 1024px) {
    #maixvision_video {
        width: 100%;
        height: auto;
    }
}
.btn, #page_content .btn, #content_body .btn {
    background: #005af2;
    box-shadow: 0px 0px 2px 0px #005af2;
}
.btn, #page_content .btn:hover, #content_body .btn:hover {
    background: #005af2;
    box-shadow: 0px 0px 10px 0px #005af2;
}
</style>

<div id="file_list_wrapper" class="flex justify-center items-center">
    <div id="file_list" class="flex flex-col justify-center items-center space-y-5 px-5 py-10">
    </div>
</div>

<div class="w-full flex flex-wrap-reverse justify-center items-center" style="min-height:80vh; background-color:#1f2022">
    <div class="flex flex-col justify-center items-center p-10">
        <h1 class="text-4xl font-bold text-white hidden">MaixVision</h1>
        <img src="/static/image/maixvision_hor.svg" class="pointer-events-none" />
        <p class="text-xm text-white">Empower edge AI projects</p>
        <div class="flex flex-row space-x-4 pt-10">
            <div id="win_download" class="btn flex w-32 space-x-1 justify-center items-center">
                <img src="/static/image/download.svg" class="pointer-events-none h-6 w-6" />
                <span class="text-lg">Windows</span>
            </div>
            <div id="linux_download" class="btn flex w-32 space-x-1 justify-center items-center">
                <img src="/static/image/download.svg" class="pointer-events-none h-6 w-6" />
                <span class="text-lg">Linux</span>
            </div>
            <div id="macos_download" class="btn flex w-32 space-x-1 justify-center items-center">
                <img src="/static/image/download.svg" class="pointer-events-none h-6 w-6" />
                <span class="text-lg">MacOS</span>
            </div>
        </div>
        <div class="mt-10">
            <p><span class="mr-2">More visit</span><a href="https://wiki.sipeed.com/maixpy/">MaixPy</a></p>
        </div>
    </div>
    <video id="maixvision_video" class="p-5" controls="false" autoplay loop muted preload src="https://wiki.sipeed.com/maixpy/static/video/maixvision.mp4" type="video/mp4">
    MaixVision
    </video>
</div>

<script>
async function getLatestVersion(filename) {
    const response = await fetch('https://cdn.sipeed.com/maixvision/' + filename + '.json');
    const data = await response.json();
    if(data.error) {
        showMsgInfo("load data failed: " + data.error);
        return;
    }
    return data;
}

var win_download = document.getElementById('win_download');
var linux_download = document.getElementById('linux_download');
var macos_download = document.getElementById('macos_download');
var file_list_wrapper = document.getElementById('file_list_wrapper');
var file_list = document.getElementById('file_list');

var win_info = undefined;
var linux_info = undefined;
var macos_info = undefined;

function showMsgInfo(msg) {
    file_list_wrapper.style.display = 'flex';
    let file_list = document.getElementById('file_list');
    file_list.innerHTML = '';
    var p = document.createElement('p');
    p.innerText = msg;
    file_list.appendChild(p);
}

function showList(files) {
    file_list_wrapper.style.display = 'flex';
    file_list.innerHTML = '';
    for (let i = files.length - 1; i >= 0; i--) {
        var a = document.createElement('a');

        a.href = 'https://cdn.sipeed.com/maixvision/' + win_info.version + '/' + files[i].url;
        a.innerText = files[i].url;
        a.className = 'p-4 bg-blue-700 text-lg rounded-md shadow hover:bg-blue-800 hover:shadow-xl';
        a.style = 'color: #FFFFFF';
        a.addEventListener('click', function () {
            file_list_wrapper.style.display = 'none';
        })

        file_list.appendChild(a);
    };

}

file_list_wrapper.addEventListener('click', function () {
    file_list_wrapper.style.display = 'none';
});

// listen to the click event
win_download.addEventListener('click', async function () {
    if (win_info === undefined) {
        showMsgInfo('Loading, please wait for a moment');
        return;
    }
    // if (win_info.files.length === 1) {
    //     window.location.href = 'https://cdn.sipeed.com/maixvision/' + win_info.version + '/' + win_info.files[0].url;
    // } else {
    //     showList(win_info.files);
    // }
    showList(win_info.files);
});

linux_download.addEventListener('click', async function () {
    if (linux_info === undefined) {
        showMsgInfo('Loading, please wait for a moment');
        return;
    }
    // if (linux_info.files.length === 1) {
    //     window.location.href = 'https://cdn.sipeed.com/maixvision/' + linux_info.version + '/' + linux_info.files[0].url;
    // } else {
    //     showList(linux_info.files);
    // }
    showList(linux_info.files);
});

macos_download.addEventListener('click', async function () {
    if (macos_info === undefined) {
        showMsgInfo('Loading, please wait for a moment');
        return;
    }
    // if (macos_info.files.length === 1) {
    //     window.location.href = 'https://cdn.sipeed.com/maixvision/' + macos_info.version + '/' + macos_info.files[0].url;
    // } else {
    //     showList(macos_info.files);
    // }
    showList(macos_info.files);
});

getLatestVersion("latest").then(function (data) {
    win_info = data;
});
getLatestVersion("latest-linux").then(function (data) {
    linux_info = data;
});
getLatestVersion("latest-macos").then(function (data) {
    macos_info = data;
});

</script>
