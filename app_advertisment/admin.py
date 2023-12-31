from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'price', 'user', 'auction', 'created_date', 'updated_date', 'image_preview']
    list_filter = ['auction', 'date']
    actions = ['make_action_false', 'make_action_true']
    readonly_fields = ["image_preview"]

    fieldsets = (
        (
            'Общее',
            {
                "fields":('title', 'text', 'user')
            }
        ),
        (
            "Изображение",
            {
                "fields": ('image', 'image_preview')
            }

        ),
        (
            'Финансы',
            {
                "fields": ('price', 'auction'),
                "classes": ['collapse']
            }
        )

    )

    @admin.action(description="убрать торг")
    def make_action_false(self, request, queryset:QuerySet):
        print(queryset, type(queryset))
        queryset.update(auction=False)

    @admin.action(description="Добавить торг")
    def make_action_true(self, request, queryset:QuerySet):
        print(queryset, type(queryset))
        queryset.update(auction=True)

# Register your models here.
admin.site.register(Advertisement, AdvertisementAdmin)
