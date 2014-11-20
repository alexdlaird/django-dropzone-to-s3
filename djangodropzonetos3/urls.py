from django.conf.urls import url

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Alex Laird'
__version__ = '0.0.1'

urlpatterns = [
    url(r'^$', 'dropzone.views.home'),
    url(r'^get_settings$', 'dropzone.views.get_settings'),
    url(r'^check_shared_key$', 'dropzone.views.check_shared_key'),
    url(r'^upload$', 'dropzone.views.upload'),
]