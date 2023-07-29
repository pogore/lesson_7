from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=126) # пользователь (пока что просто имя)
    date = models.DateField("дата", auto_now_add=True)

    class Meta:
        db_table = "Advertisement"

    def __str__(self):
        return f'< Advertisement: Advertisement(id={self.pk}, title={self.title}, price = {self.price}) >.'