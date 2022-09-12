# Generated by Django 4.1 on 2022-09-08 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='payment_max',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000000, message='Максимальная кредит: 10000000')], verbose_name='Сумма кредита, ДО'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='payment_min',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000, message='Минимальный кредит: 1000000')], verbose_name='Сумма кредита, ОТ'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='rate_max',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(9.8, message='Максимальная ставка: 9.8')], verbose_name='Ставка, ДО'),
        ),
    ]