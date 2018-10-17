from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard/$', views.dashboard),
    url(r'^dashboard/admin$', views.dashboardadmin),
    url(r'^logout$', views.logout),
    url(r'^dashboard/admin/adminadd$', views.adminadd),
    url(r'^(?P<userid>\d+)/show$', views.show),
    url(r'^(?P<userid>\d+)/delete$', views.delete),
    url(r'^(?P<userid>\d+)/showedit$', views.showedit),
    url(r'^(?P<userid>\d+)/edit$', views.edit),
    url(r'^edit/(?P<userid>\d+)$', views.useredit),
    url(r'^(?P<userid>\d+)/userupdate$', views.userupdate),
    url(r'^(?P<userid>\d+)/update$', views.update),
    url(r'^register/process$', views.add),
    url(r'^login$', views.login),
    url(r'^signin$', views.signin),
    url(r'^register$', views.register),
    # url(r'^(?P<userid>\d+)/edit$', views.edit),
    # url(r'^(?P<userid>\d+)/update$', views.update),


]  