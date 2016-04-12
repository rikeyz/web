/**
 * Created by zhongrui8 on 2016/3/24.
 */
$(document).ready(
    function(){

        $.ajax({
            type: 'POST',
            url: '/data/menus',
            timeout: 5000,
            async:true   ,
            error: function(){
                alert("Error to get menu data.");
            },
            success: function(menus){
                var list = $("<ul id='resourcemenu' class='nav navbar-default'></ul>");
                $.each(menus, function(index, menu){
                    //list = list + "<li><a class='clickEvent' href='#'> "+ menu.fields.catetoryname +"</a> </li>"
                    var ahref = $("<a class='clickEvent' href='/category.html?menuid="+menu.fields.unique_code + "'> "+ menu.fields.catetoryname +"</a>");
                    //ahref.bind('click', function () {
                    //    renderMain($(this).attr("href"));
                    //    return false;
                    //});
                    var li = $("<li></li>").append($(ahref));
                    $(list).append($(li));
                    //href='/category.html?menuid="+menu.fields.unique_code+"'>"+menu.fields.catetoryname+"
                });

                $('#listcontent').append($(list));
                $("#resourcemenu").find("li:first").find("a").trigger('click');
            }
            }
        );

        //$(this).delay(1000, 's');

        $(".clickEvent").on('click', function(){
            renderMain($(this).attr("href"));
            return false;
        });

    }
);