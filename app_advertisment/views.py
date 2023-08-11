from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

# Create your views here.

def index(request):
    advertisements : list[Advertisement] = Advertisement.objects.all()
    context = {"advertisements" : advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    id_advertisement = request.GET.get("adv")
    adv = Advertisement.objects.get(id=id_advertisement)
    context = {"adv": adv}
    return render(request, 'advertisement.html', context)


