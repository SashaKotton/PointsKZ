# Generated by Django 5.0.2 on 2024-02-12 13:36

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='structure',
            field=tinymce.models.HTMLField(verbose_name='Состав'),
        ),
    ]
