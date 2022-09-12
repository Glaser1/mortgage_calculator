from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class OfferURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.url = reverse('offer-list')

    def test_offer_url_exists_at_desired_Location(self):
        """ Ensure URL /offer/ is available. """
        response = self.guest_client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
