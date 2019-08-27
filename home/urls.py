from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('services', views.Services.as_view(), name='services'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('sending_email', views.sending_email, name='sending_email'),
    path('make_appointment_home', views.make_appointment_home, name='make_appointment_home'),
   
   
]
