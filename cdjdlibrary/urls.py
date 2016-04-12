from django.conf.urls import patterns, url, include

from cdjdlibrary.auth.views import signup,loginform, loginlib, logoutlib
from cdjdlibrary.core.views import home, bootstrap
from cdjdlibrary.data import urls as dataurls

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup.html$', signup, name='signup'),
    url(r'^$', home, name='home'),
    url(r'^bootstrap$', bootstrap),
    url(r'^login.html$', loginform),
    url(r'^login/$', loginlib, name='login'),
    url(r'^logout/$', logoutlib, name='logout'),
    url(r'^data/', include('cdjdlibrary.data.urls'))
)
