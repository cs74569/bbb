from django.urls import path
from main import views



app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.login, name='main'),
    
]