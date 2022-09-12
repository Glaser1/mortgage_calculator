from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import MortgageViewSet


router = DefaultRouter()
router.register('offer', MortgageViewSet)

urlpatterns = [
    path('', include(router.urls), name='offer-list')
]
