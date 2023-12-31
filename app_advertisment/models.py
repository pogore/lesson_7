from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model() # создание модели пользователя


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    text = models.TextField("Текст")
    price = models.FloatField("Цена")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField("Дата", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    auction = models.BooleanField("Торг", help_text="Возможен торг или нет", default=False)
    image = models.ImageField("Изображение", upload_to='advertisment/media/')

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

    @admin.display(description="Миниатюра изображения")
    def image_preview(self):
        from django.utils.html import format_html
        if self.image:
            a = self.image.url
        else:
            a = '/static/img/adv.png'

        return format_html(
            '<img src = "{}" class ="img-fluid rounded-start" alt="Card title" height = 100px>', a)



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
