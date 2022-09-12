import random

import django.utils.datastructures
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from api.models import Offer
from api.serializers import CreateOrGetOfferSerializer
from api.filters import OfferFilter


class MortgageViewSet(viewsets.ModelViewSet):
    """ CRUD операции с ипотечными предложениями. """
    queryset = Offer.objects.all()
    serializer_class = CreateOrGetOfferSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = OfferFilter
    filterset_fields = ('term_min', 'term_max', 'rate_min', 'rate_max', 'payment_min', 'payment_max')

    def get_param(self, request, key):
        query_params = self.request.query_params
        try:
            value = int(query_params[key])
        except KeyError:
            value = None
        return value

    def list(self, request, *args, **kwargs):
        if not self.request.query_params:
            return super().list(request, *args, **kwargs)
        ordering_param = self.request.query_params.get('order')
        responce = super().list(request, *args, **kwargs)
        for i in range(len(responce.data)):
            rate_min = responce.data[i]['rate_min']
            rate_max = responce.data[i]['rate_max']
            rate = random.uniform(rate_min, rate_max)
            responce.data[i]['rate'] = round(rate)
            responce.data[i]['payment'] = 0
            price = self.get_param(request, 'price')
            term = self.get_param(request, 'term')
            deposit = self.get_param(request, 'deposit')
            if price and term:
                if deposit:
                    price = price - (price / 100 * deposit)
                month_rate = rate / 12 / 100
                term = term * 12
                total_rate = ((1 + month_rate) ** term)
                payment = round(price * month_rate * total_rate / (total_rate - 1))
                responce.data[i]['payment'] = payment
        if ordering_param and '-' in ordering_param:
            responce.data = sorted(responce.data, key=lambda x: (x[ordering_param.replace('-', '')],), reverse=True)
        elif ordering_param:
            responce.data = sorted(responce.data, key=lambda x: (x[ordering_param],))
        for i in range(len(responce.data)):
            responce.data[i].pop('rate')
        return responce
