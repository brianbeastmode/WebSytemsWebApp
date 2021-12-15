from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('add-post', views.addThread, name = 'add_post'),
    path('signup', views.signup, name = 'signup'),




]