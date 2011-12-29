"""Urls for the Zinnia admin"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns


urlpatterns = patterns('zinnia.views.admin',
                       url(r'^facebook/$', 'facebook_callback',
                           name='zinnia_facebook_callback'),
                       )
