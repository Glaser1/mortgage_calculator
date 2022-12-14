# Generated by Django 4.1 on 2022-09-10 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_offer_term_max'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='payment_max',
            field=models.PositiveIntegerField(help_text='Введите максимальную сумму кредита', validators=[django.core.validators.MinValueValidator(10000000, message='Максимальная кредит: 10000000')], verbose_name='Сумма кредита, ДО'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='payment_min',
            field=models.PositiveIntegerField(help_text='Введите минимальную сумму кредита', validators=[django.core.validators.MinValueValidator(1000000, message='Минимальный кредит: 1000000')], verbose_name='Сумма кредита, ОТ'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='rate_max',
            field=models.FloatField(help_text='Введите максимальную ставку', validators=[django.core.validators.MaxValueValidator(9.8, message='Максимальная ставка: 9.8')], verbose_name='Ставка, ДО'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='rate_min',
            field=models.FloatField(help_text='Введите минимальную ставку', validators=[django.core.validators.MinValueValidator(1.8, message='Минимальная ставка: 1.8')], verbose_name='Ставка, ОТ'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='term_max',
            field=models.PositiveSmallIntegerField(help_text='Введите максимальный срок ипотеки', validators=[django.core.validators.MaxValueValidator(30, message='Максимальный срок: 30')], verbose_name='Срок ипотеки, ДО'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='term_min',
            field=models.PositiveSmallIntegerField(help_text='Введите минимальный срок ипотеки', validators=[django.core.validators.MinValueValidator(10, message='Минимальный срок: 10')], verbose_name='Срок ипотеки, ОТ'),
        ),
    ]
