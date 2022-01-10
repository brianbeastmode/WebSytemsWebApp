from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('logout/', views.logout, name="logout"),
]