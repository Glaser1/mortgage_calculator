# Generated by Django 4.1 on 2022-09-10 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_offer_payment_max_alter_offer_payment_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='term_max',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(30, message='Максимальный срок: 30')], verbose_name='Срок ипотеки, ДО'),
        ),
    ]
