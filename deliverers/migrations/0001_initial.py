# Generated by Django 5.0.2 on 2024-02-08 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование Компании')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон компании')),
            ],
            options={
                'verbose_name': 'Компания доставки',
                'verbose_name_plural': 'Компании доставки',
            },
        ),
        migrations.CreateModel(
            name='Deliverer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('delivery_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deliverers.deliverycompany', verbose_name='Компания доставки')),
            ],
        ),
    ]
