from django.db import models
from django.contrib import admin

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=126) # пользователь (пока что просто имя)
    date = models.DateTimeField("дата", auto_now_add=True)
    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    auction = models.BooleanField("торг", help_text="Возможен торг или нет", default=False)
    class Meta:
        db_table = "Advertisement"
        verbose_name = 'Список объявлений'
        verbose_name_plural = 'Список объявлений'

    def __str__(self):
        return f'< Advertisement: Advertisement(id={self.pk}, title={self.title}, price = {self.price}) >.'

    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.date.date() == timezone.now().date():
            create_time = self.date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weigth:bold;">Сегодня в {} </span>',create_time
            )
        return self.date.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:blue; font-weigth:bold;">Сегодня в {} </span>',updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
