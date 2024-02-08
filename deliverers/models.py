from django.db import models

class DeliveryCompany(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование Компании')
    phone = models.CharField(max_length=255, verbose_name='Телефон компании', null = True, blank=True)

    class Meta:
        verbose_name='Компания доставки'
        verbose_name_plural='Компании доставки'

    def __str__(self):
        return f'{self.pk} - {self.title}'
    
class Deliverer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    delivery_company = models.ForeignKey(DeliveryCompany, verbose_name='Компания доставки', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Доставщик'
        verbose_name_plural='Доставщики'

    def __str__(self):
        return f'{self.pk} - {self.name} {self.surname}'
    
# Create your models here.
