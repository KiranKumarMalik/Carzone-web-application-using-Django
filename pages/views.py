from django.shortcuts import render

# Create your views here.

def home(request): 
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'pages/cars.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def search(request):
    return render(request, 'pages/search.html')