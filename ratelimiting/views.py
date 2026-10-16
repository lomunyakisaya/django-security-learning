from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django_ratelimit.decorators import ratelimit
from django_ratelimit.decorators import ratelimit
# Create your views here.
def home_view(request):
    return render(request, "ratelimiting/home.html")
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        

    return render(request, "ratelimiting/signup.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,
                            password=password,
                            )
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "ratelimiting/login.html")

def dashboard_view(request):
    return render(request, "ratelimiting/dashboard.html")
def logout_view(request):
    return render(request, "ratelimiting/home.html")