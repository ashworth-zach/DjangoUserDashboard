from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard/$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^dashboard/admin/adminadd$', views.adminadd),
    url(r'^(?P<userid>\d+)/show$', views.show),
    url(r'^register/process$', views.add),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
    url(r'^register$', views.register),
    # url(r'^(?P<userid>\d+)/edit$', views.edit),
    # url(r'^(?P<userid>\d+)/update$', views.update),


]  