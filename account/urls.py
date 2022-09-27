
from django.urls import path
from .views import *
from . import views




app_name = 'account'
urlpatterns =[
    path('login/',views.loginPage, name='login'),
     path('logout/',views.logoutPage, name='logout'),
    path('register_page/',views.registration, name='register_page'),
    path('p_dashboard/',views.dashboard, name='p_dashboard'),
 
]

