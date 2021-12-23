from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('thread/<slug>/', views.view_thread, name = 'view_thread'),
    path('thread/<slug>/', views.view_thread, name = 'view_thread'),
    path('community/<slug>/', views.community_view, name = 'community_view'),

]