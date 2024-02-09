# Generated by Django 5.0.2 on 2024-02-08 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('images', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('dish_weigth', models.IntegerField(default=0, verbose_name='Выход НЕТТО')),
                ('structure', models.TextField(verbose_name='Состав')),
                ('availability', models.CharField(choices=[('Not available', 'Нет в наличии'), ('Available', 'В наличии')], default='Available', max_length=255, verbose_name='Доступность')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]