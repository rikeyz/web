# --*-- coding:utf-8 --*--

from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from cdjdlibrary.data.models import Menu
from django.http import HttpResponse

@csrf_exempt
@login_required
def ajax_get_resourcemenu(request):
    menus = []
    for i in range(10):
        menu = Menu()
        menu.catetoryname = "类目%d"%i
        menu.unique_code = "000%d"%i
        menus.append(menu)
    menusJson = serializers.serialize("json", menus)
    return HttpResponse(menusJson, content_type="application/json")
