from django.urls import path
from .views import homepage,reg_star,sing_in, logout_fan,home_to_fulpag

urlpatterns = [
    path('', homepage, name='homepa'),
    path('reg', reg_star, name='reg_ur'),
    path('si', sing_in, name='sing_ins'),
    path('log',logout_fan , name='logout'),
    path('home-to',home_to_fulpag, name='home_to_fulpag'),
    
]