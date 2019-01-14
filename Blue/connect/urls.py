from django.urls import path
from main import views



app_name = 'connect'
urlpatterns = [
    path('', views.main, name='connect'),
    path('connect/', views.connect, name='connect'),
    
]