from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^newmessage/(?P<recipientid>\d+)$', views.newmessage),
    url(r'^newcomment$', views.newcomment),
]  