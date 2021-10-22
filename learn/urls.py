"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from learn import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('CreateBio', views.CreateBio, name='CreateBio'),
    path('updatebio/<int:pk_id>/delete', views.updatebio, name='updatebio'),
    path('contact', views.contact, name='contact'),
    path('share/<str:username>', views.share, name='share'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('profile', views.profile, name='profile'),
    path('intro/', views.intro, name='intro'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('user_q', views.search_users, name='search_users')
    #<int:pk_id>/change/ 
    #<int:id>/update


]
