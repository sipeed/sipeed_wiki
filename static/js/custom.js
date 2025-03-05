// get language from html element's lang attribute to lower case
var lang = $("html").attr("lang").split("-")[0].toLowerCase();

var content;
// get editPage element's parent element's href
var sourceUrl = $("#editPage").parent().attr("href");
if (lang == "zh") {
    content = "<div>查看<a href='" + sourceUrl + "' target='_blank'>源文档</a></div><div>修改文档请参考<a href='/share_docs/zh/' target='_blank'>贡献编辑文档指南</a></div>";
} else {
    content = "<div>View <a href='" + sourceUrl + "' target='_blank'>source doc</a></div><div>For editing, please refer to <a href='/share_docs/en/' target='_blank'>contribution guide</a></div>";
}
// add editPageHelp after editPage's parent element
$("#editPage").parent().after("<div id='editPageHelp' style='display:none;'>" + content + "</div>");
// remove editPage element's href and add click event
$("#editPage").parent().removeAttr("href").click(function() {
    // show editPageHelp if editPageHelp is hidden
    if ($("#editPageHelp").is(":hidden")) {
        $("#editPageHelp").show();
    }
    // hide editPageHelp if editPageHelp is shown
    else {
        $("#editPageHelp").hide();
    }
});

