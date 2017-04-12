/**
 * Created by linghao on 2017/4/11.
 */
$(document).ready(function(){
    $("#select").click(function (){
        $.ajax({   //传递给后端
            type:"post",   //用post方法请求  所以调用IndexHandler类post方法
            url:"/test",
            // data:pd,   //传输的数据
            cache:false,
            // success:function(data){    //请求成功时执行回调函数   data可为任意变量名
            //     // alert(data);
            //     alert("success"+data);
            // },
            //到这里
            // success:function loadInfo(data){//请求成功时执行回调函数   data可为任意变量名
            //     $.getJSON("json",function(data){
            //         $("#info").html("");
            //         $.each(data.comments,function(i,item){
            //             alert("1111"+item.text);
            //             $("#info").append(
            //                 "<div>"+item.text+"</div><hr/>");
            //         });
            //     });
            // },
            error:function(){
                alert("error!");
            }
        });
    });
});