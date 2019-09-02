# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

try:
    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
                           (url(r'^site/([\w-]*)/$', 'dynamicLink.views.site')),
                           (url(r'^link/(\w{1,100})/.*$', 'dynamicLink.views.fetch')),
                           (url(r'^link/(\w{1,100})$', 'dynamicLink.views.fetch')),  # without prefix
                           )
except ImportError:
    from django.urls import include, path

    urlpatterns = [
        path(
            route='v1/',
            view=include('api.v1.urls'),
            name='version-one-of-APIs'
        ),
    ]
