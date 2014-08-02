from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'dropzone.views.home'),
    url(r'^get_settings$', 'dropzone.views.get_settings'),
    url(r'^check_shared_key$', 'dropzone.views.check_shared_key'),
    url(r'^upload$', 'dropzone.views.upload'),
]