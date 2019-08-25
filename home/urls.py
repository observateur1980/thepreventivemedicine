from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('services', views.Services.as_view(), name='services'),
   
   
]
