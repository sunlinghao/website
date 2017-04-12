/**
 * Created by linghao on 2017/4/10.
 */
$(document).ready(function(){
    //alert('good');
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        // alert("username"+user);
        var pd = {"username":user,"password":pwd};
        $.ajax({   //传递给后端
            type:"post",   //用post方法请求  所以调用IndexHandler类post方法
            url:"/",
            data:pd,   //传输的数据
            cache:false,
            success:function(data){    //请求成功时执行回调函数   data可为任意变量名
                // alert(data);
                if(data=="your password was not right.")
                    alert("your password was not right.");
                else if(data=="There is no this user.")
                    alert("There is no this user.")
                else
                    window.location.href = "/user?user="+data;
            },
            error:function(){
                alert("error!");
            }
        });
    });
});