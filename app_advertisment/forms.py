from django import forms
#
# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=128, label="Заголовок", widget=forms.TextInput(attrs={"class": "form-control-lg"}))
#     text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control-lg"}), max_length=128, label="Описание")
#     price = forms.FloatField(widget=forms.TextInput(attrs={"class": "form-control-lg"}), label="Цена")
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}), required=False, label="Торг")
#     image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}), label="Изображение")

from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError

# Create the form class.
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'text', 'price', 'auction', 'image']
        widgets = {
           'title':forms.TextInput(attrs={"class": "form-control-lg"}),
           'text':forms.Textarea(attrs={"class": "form-control-lg"}),
           'price':forms.TextInput(attrs={"class": "form-control-lg"}),
           'auction':forms.CheckboxInput(attrs={"class": "form-check-input"}),
           'image':forms.FileInput(attrs={"class": "form-control form-control-lg"})
        }

    def clean_title(self):
        data = self.cleaned_data['title']
        if data[0] == '?':
            raise ValidationError("Заголовок объявления не может начинатся с знака вопроса!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data