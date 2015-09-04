jQuery(document).ready(function(){
    var $=jQuery; 
    //绑定链接
    $.pjax({
        selector: '[data-pjax] a, a[data-pjax]',
        container: '.ajaxdiv', //内容替换的容器
        show: 'slide',  //展现的动画，支持默认和fade, 可以自定义动画方式，这里为自定义的function即可。
        cache: false,  //是否使用缓存
        storage: true,  //是否使用本地存储
        titleSuffix: ' | Ray', //标题后缀
        filter: function(){},
        callback: function(status){
            $("#nav-menu").addClass("animated fadeInUp");
        }
    }); 
        //绑定跳转开始事件
    $(".ajaxdiv").bind("pjax.start",
         function() { 
            $(".ajaxdiv").css("opacity","0.6");
            $(".spinner").css("opacity","1");
            $(".spinner").show();               
            
     });
        //绑定跳转结束事件
    $(".ajaxdiv").bind("pjax.end",
         function() {  
            $(".spinner").hide();
            $(".ajaxdiv").css("opacity","1");
            // Main
            initHeader();
            addListeners();
            if (navigator.userAgent.indexOf('Firefox') >= 0){
                document.documentElement.scrollTop=120;
            }
            else
            {
               $('body').animate({scrollTop: 120});
            }
             
     }); 
     
});   

function is_pjax(){   
    return array_key_exists('HTTP_X_PJAX', $_SERVER) && $_SERVER['HTTP_X_PJAX'];
}