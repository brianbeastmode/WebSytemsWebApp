from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login_request, name = 'login'),
    path('logout', views.logout_request, name = 'logout'),
    path('add-post', views.addThread, name = 'add_post'),
    path('<int:id>/', views.view_post, name = 'view_post'),
    path('addcomment/<int:id>/', views.addComment, name = 'comment'),
    



]