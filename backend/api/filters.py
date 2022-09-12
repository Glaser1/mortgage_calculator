import django_filters as filters

from api.models import Offer


class OfferFilter(filters.FilterSet):
    rate_min = filters.CharFilter(field_name='rate_min', lookup_expr='lte')
    rate_max = filters.CharFilter(field_name='rate_max', lookup_expr='gte')
    payment_min = filters.CharFilter(field_name='payment_min', lookup_expr='lte')
    payment_max = filters.CharFilter(field_name='payment_max', lookup_expr='gte')

    class Meta:
        model = Offer
        fields = ('rate_min', 'rate_max')
