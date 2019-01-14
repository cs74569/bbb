from django.urls import path
from main import views



app_name = 'add'
urlpatterns = [
    path('', views.main, name='add'),
    path('add/', views.add, name='add'),
    
]