from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# для подсказки
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.

def login_view(request:WSGIRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(
                reverse('profile')
            )
        else:
            return render(request, 'auth/login.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                reverse('profile')
            )
        else:
            return render(request, "auth/login.html", {"error", "Пользователь не найден"})


@login_required(login_url=reverse_lazy("login"))
def profile_view(request:WSGIRequest):
    return render(request, 'auth/profile.html')

def register(request:WSGIRequest):
    return render(request, 'auth/register.html')

@login_required(login_url=reverse_lazy("login"))
def logout_view(request:WSGIRequest):
    logout(request)
    return redirect(
        reverse('login')
    )
