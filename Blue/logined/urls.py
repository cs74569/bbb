from django.urls import path
from main import views



app_name = 'logined'
urlpatterns = [
    path('', views.main, name='logined'),
    path('logined/', views.logined, name='logined'),
    
]