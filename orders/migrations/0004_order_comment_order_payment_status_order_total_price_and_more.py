# Generated by Django 5.0.2 on 2024-02-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='', verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False, verbose_name='Статус оплаты'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='Итоговая сумма'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Подитог'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', 'Обрабатывается'), ('at work', 'В работе'), ('on the way', 'В пути'), ('canceled', 'Отменен'), ('completed', 'Выполнен')], max_length=255, verbose_name='Статус'),
        ),
    ]
