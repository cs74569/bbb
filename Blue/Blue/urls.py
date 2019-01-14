"""Blue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',include('main.urls', namespace='main')),
    path('login',include('login.urls', namespace='login')),
    path('connect',include('connect.urls', namespace='connect')),
    path('create',include('create.urls', namespace='create')),
    path('add',include('add.urls', namespace='add')),
    path('logined',include('logined.urls', namespace='logined')),
    path('loginedconnect',include('loginedconnect.urls', namespace='loginedconnect')),
    re_path('.*',views.main),
]
