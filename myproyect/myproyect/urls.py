from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproyect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^update', 'cms_barrapunto.views.updateNoticias'),
    url(r'^(.*)', "cms_barrapunto.views.processCMS"),
)
