from django.urls import path
from main import views



app_name = 'loginedconnect'
urlpatterns = [
    path('', views.main, name='loginedconnect'),
    path('loginedconnect/', views.loginedconnect, name='loginedconnect'),
    
]