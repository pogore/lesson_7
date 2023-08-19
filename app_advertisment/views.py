from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

# для подсказки
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def index(request:WSGIRequest):
    advertisements : list[Advertisement] = Advertisement.objects.all()
    context = {"advertisements" : advertisements}
    return render(request, 'advertisement/index.html', context)

def top_sellers(request:WSGIRequest):
    return render(request, 'advertisement/top-sellers.html')

@login_required(login_url=reverse_lazy("login"))
def advertisement_post(request:WSGIRequest):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES) # передаем на проверку
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data) # передаю данные в модуль
            adv.user = request.user # добавил в запись пользователя
            adv.save() # сохранил
            return redirect(
                reverse('main-page')
            )
        else:
            print("Ошибка")
            print(form.errors)
            context = {"form": form}
            return render(request, 'advertisement/advertisement-post.html', context)
    else:
        form = AdvertisementForm()
        context = {"form" : form}
        return render(request, 'advertisement/advertisement-post.html', context)

def advertisement(request:WSGIRequest):
    id_advertisement = request.GET.get("adv")
    adv = Advertisement.objects.get(id=id_advertisement)
    context = {"adv": adv}
    return render(request, 'advertisement/advertisement.html', context)


