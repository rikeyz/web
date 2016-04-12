from django.conf.urls import patterns, url
from cdjdlibrary.data.views import ajax_get_resourcemenu

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^menus$', ajax_get_resourcemenu),
)
