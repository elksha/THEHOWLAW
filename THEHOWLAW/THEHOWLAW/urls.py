"""THEHOWLAW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include
from howlaw import views

urlpatterns = [
    url(r'^chat/', include('chat.urls'), name='chat'),
    url(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>/', views.detail, name='detail'),
    path('edit/<int:post_pk>/', views.edit, name = 'edit'),
    path('delete/<int:post_pk>/', views.delete, name = 'delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('allauth.urls')),
    path('mypage_customer/', views.mypage_customer, name='mypage_customer'),
    path('mypage_lawyer/', views.mypage_lawyer, name='mypage_lawyer'),
    path('mypage_school/', views.mypage_school, name='mypage_school'),
    path('menubar/', views.menubar, name='menubar'),
    path('centerslink/', views.centerslink, name='centerslink'),
    path('about/', views.about, name='about'),
    path('detail_list/', views.detail_list, name='detail_list'),
    path('chatbot_menu/', views.chatbot_menu, name='chatbot_menu'),
    path('chat/lawyer_chat/', views.lawyer_chat, name='lawyer_chat'),
<<<<<<< HEAD
    path('chat/room/', views.room, name='room'),
    path('about/', views.about, name='about'),
=======
    path('index/', views.index, name='index'),
>>>>>>> 94f487ba733b0ce921c4220d6c0c04a220b324d3
]
