from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$',views.base),
    url(r'^display$',views.display),
    url(r'^create$',views.create),
    url(r'^show/(?P<show_id>\d+)$', views.show),
    url(r'^show/(?P<show_id>\d+)/edit$', views.edit),
    url(r'^show/(?P<show_id>\d+)/delete$', views.delete),
    url(r'^update/(?P<show_id>\d+)$', views.update),




]