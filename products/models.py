from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.pk} - {self.title}'
    
class Product(models.Model):
    AVAILABILITY_CHOICES = (
        ('Not available', 'Нет в наличии'),
        ('Available', 'В наличии'),
    )
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = HTMLField(verbose_name='Описание')
    images = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    price = models.IntegerField(default = 0, verbose_name='Цена')
    dish_weigth = models.IntegerField(default = 0, verbose_name='Выход НЕТТО')
    structure = HTMLField(verbose_name='Состав')
    availability = models.CharField(verbose_name='Доступность', choices=AVAILABILITY_CHOICES, max_length=255, default='Available')

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return f'{self.pk} - {self.title}'