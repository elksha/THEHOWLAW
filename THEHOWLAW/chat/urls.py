from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='chat'),
    url('laywerchat', views.lawyerchat, name='lawyerchat'),

]