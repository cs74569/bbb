from django.urls import path
from main import views



app_name = 'create'
urlpatterns = [
    path('', views.main, name='create'),
    path('create/', views.create, name='create'),
    
]