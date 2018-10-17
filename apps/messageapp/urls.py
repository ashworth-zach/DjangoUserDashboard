from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<recipientid>\d+)/newmessage$', views.newmessage),
    url(r'^comment$', views.newcomment),
]  