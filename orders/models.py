from django.db import models
from django.utils import timezone
from deliverers.models import Deliverer
from products.models import Product

class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('card','Карточка'),
        ('cash','Наличка'),
        ('transer','Перевод'),
    )
    title = models.CharField(max_length=255, verbose_name='Вид платежа', choices=PAYMENT_CHOICES)
    total_price = models.IntegerField(default=0, verbose_name='Общая сумма')

    class Meta:
        verbose_name ='Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.pk} - {self.title}'
    
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('processing','Обрабатывается'),
        ('at work', 'В работе'),
        ('on the way', 'В пути'),
        ('canceled', 'Отменен'),
        ('completed', 'Выполнен'),
    )
    created_at = models.DateTimeField(verbose_name='Создано', default=timezone.now)
    status = models.CharField(max_length=255, choices = STATUS_CHOICES, verbose_name='Статус')
    deliverer = models.ForeignKey(Deliverer, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Доставщик')
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Вид платежа')
    comment = models.TextField(default='',verbose_name='Комментарий')
    total_price = models.IntegerField(default=0, verbose_name='Итоговая сумма')
    payment_status = models.BooleanField(default= False, verbose_name='Статус оплаты')

    class Meta:
        verbose_name ='Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.pk} - {self.created_at} - {self.status}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete = models.CASCADE, verbose_name='Продукт')
    quantity = models.IntegerField(default = 0, verbose_name='Количество')
    amount = models.IntegerField(default=0, verbose_name='Подитог')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Заказ')

    class Meta:
        verbose_name ='Заказаный товар'
        verbose_name_plural = 'Заказаные товары'

    def __str__(self):
        return f'{self.pk} - {self.order}.{self.product}'
# Create your models here.
