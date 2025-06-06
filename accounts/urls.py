from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
