from django.urls import path
from main import views



app_name = 'login'
urlpatterns = [
    path('', views.main, name='login'),
    path('login', views.main, name='lgoin'),
    
]