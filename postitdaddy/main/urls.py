from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('thread/<slug>/', views.view_thread, name = "view_thread"),
    path('community/<slug>/', views.community_view, name = "community_view"),
    path('add-thread/', views.addThread, name = "add_thread"),
    path('add-community/', views.addCommunity, name = "add_community"),

]