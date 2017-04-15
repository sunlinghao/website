/**
 * Created by linghao on 2017/4/11.
 */
$(document).ready(function(){
    $("#select").click(function (){
        var value = $("#key").val();
        var pd = {"value":value};
        $.ajax({   //传递给后端
            type:"post",   //用post方法请求  所以调用IndexHandler类post方法
           // url:"1.json",  //下面function中data来自这里
            data:pd,   //传输的数据
            cache:false,
            success:function (){//请求成功时执行回调函数   data可为任意变量名
                $.getJSON(url= "1.json",callback=function(data) {
                    //alert(data);
                    $("#info").html("");
                    $.each(data, function (i, item) { //显示json
                        // alert(i+item.text);
                        $("#info").append(
                            "<hr /><div>" + item.text + "</div><hr/>");
                    });
                });
            },
            error:function(){
                alert("error!");
            }
        });
    });
});


// $(document).ready(function() {
//     $("#select").click(function () {
//         var value = $("#key").val();
//         var pd = {"value": value};
//         $(function () {
//             $.getJSON("1.json", function (data) {
//                 $("#info").html("");
//                 alert("hahaha");
//                 $.each(data, function (i, item) { //显示json
//                     $("#info").append(
//                         "<hr /><div>" + item.text + "</div><hr/>"
//                     );
//                 });
//             });
//         });
//     });
// });