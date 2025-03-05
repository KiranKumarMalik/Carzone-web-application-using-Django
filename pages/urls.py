from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('cars/', views.cars, name="cars"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('admin/', views.admin, name="admin")
]