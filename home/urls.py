from django.contrib import admin
from django.urls import path, include
#ye likhna padega alag se
from home import views

urlpatterns = [
    path('',views.index, name='home'),# agr khali req hai toh index fuction jo view me hai waha jayega
    
    #path('about',views.about, name='about'),#agr /about req krenge to views ke about function ko trigger krega

    path('portfolio',views.portfolio, name='portfolio'),

    path('contact',views.contact, name='contact'),  #yaha se views ke andar contact function ko jayega

    
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    
]
