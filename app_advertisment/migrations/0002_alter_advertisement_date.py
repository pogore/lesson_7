# Generated by Django 4.2.3 on 2023-07-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='дата'),
        ),
    ]