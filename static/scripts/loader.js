//Loader Scripting
$(document).ready(function(){
    $(this).scrollTop(0);
});

$(window).on("load",function(){
    $(".loader").slideUp("slow");
    $("html").css("overflow-y", "scroll");
    typeWriter();
    setTimeout(disBtn, (speed * txt.length)+100 );
});