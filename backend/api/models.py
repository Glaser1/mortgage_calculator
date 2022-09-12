from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from config.settings import RATE_MAX, RATE_MIN, TERM_MAX, TERM_MIN, PAYMENT_MAX, PAYMENT_MIN


class Offer(models.Model):
    bankname = models.CharField(
        max_length=30,
        verbose_name='Название банка',
        help_text='Укажите название банка',
        db_index=True,
        unique=True
    )
    term_min = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(TERM_MIN, message=f'Минимальный срок: {TERM_MIN}'),),
        verbose_name='Срок ипотеки, ОТ', help_text='Введите минимальный срок ипотеки'
    )
    term_max = models.PositiveSmallIntegerField(
        validators=(MaxValueValidator(TERM_MAX, message=f'Максимальный срок: {TERM_MAX}'),),
        verbose_name='Срок ипотеки, ДО', help_text='Введите максимальный срок ипотеки'
    )
    rate_min = models.FloatField(
        validators=(MinValueValidator(RATE_MIN, message=f'Минимальная ставка: {RATE_MIN}'),),
        verbose_name='Ставка, ОТ', help_text='Введите минимальную ставку'
    )
    rate_max = models.FloatField(
        validators=(MaxValueValidator(RATE_MAX, message=f'Максимальная ставка: {RATE_MAX}'),),
        verbose_name='Ставка, ДО', help_text='Введите максимальную ставку'
    )
    payment_min = models.PositiveIntegerField(
        validators=(MinValueValidator(PAYMENT_MIN, message=f'Минимальный кредит: {PAYMENT_MIN}'),),
        verbose_name='Сумма кредита, ОТ', help_text='Введите минимальную сумму кредита'
    )
    payment_max = models.PositiveIntegerField(
        validators=(MaxValueValidator(PAYMENT_MAX, message=f'Максимальная кредит: {PAYMENT_MAX}'),),
        verbose_name='Сумма кредита, ДО', help_text='Введите максимальную сумму кредита'
    )

    class Meta:
        ordering = ('-bankname',)
        verbose_name = 'Ипотечное предложения'
        verbose_name_plural = 'Ипотечные предложения'

    def __str__(self):
        return self.bankname
