from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from api.models import Offer
from config.settings import RATE_MAX, RATE_MIN, TERM_MAX, TERM_MIN, PAYMENT_MAX, PAYMENT_MIN


class CreateOrGetOfferSerializer(serializers.ModelSerializer):
    term_min = serializers.IntegerField(
        validators=(
            MinValueValidator(
                limit_value=TERM_MIN,
                message=f'Минимальный срок ипотеки: {TERM_MIN}'
            ),
        )
    )
    term_max = serializers.IntegerField(
        validators=(
            MaxValueValidator(
                limit_value=TERM_MAX,
                message=f'Максимальный срок ипотеки: {TERM_MAX}'
            ),
        )
    )
    rate_min = serializers.FloatField(
        validators=(
            MinValueValidator(
                limit_value=RATE_MIN,
                message=f'Минимальная ставка: {RATE_MIN}'
            ),
        )
    )
    rate_max = serializers.FloatField(
        validators=(
            MaxValueValidator(
                limit_value=RATE_MAX,
                message=f'Максимальная ставка: {RATE_MAX}'
            ),
        )
    )
    payment_min = serializers.IntegerField(
        validators=(
            MinValueValidator(
                limit_value=PAYMENT_MIN,
                message=f'Минимальная сумма кредита: {PAYMENT_MIN}'
            ),
        )
    )
    payment_max = serializers.IntegerField(
        validators=(
            MaxValueValidator(
                limit_value=PAYMENT_MAX,
                message=f'Максимальная сумма кредита: {PAYMENT_MAX}'
            ),
        )
    )

    class Meta:
        model = Offer
        fields = ('id', 'bankname', 'term_min', 'term_max',
                  'rate_min', 'rate_max', 'payment_min', 'payment_max'
                  )
