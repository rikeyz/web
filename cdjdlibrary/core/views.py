# --*-- coding:utf-8 --*--
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/index.html', {})
    else:
        return render(request, 'core/index.html', {}) # 应该跳到登陆页


def bootstrap(request):
    tpl = request.GET['template']
    return render(request, tpl, {})
