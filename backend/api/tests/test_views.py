import json
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Offer


class OfferTests(APITestCase):
    def setUp(self):
        self.url = '/api/offer/'
        self.offer_attrubutes = {
            'id': 1,
            'bankname': 'TestBank1',
            'term_min': 10,
            'term_max': 30,
            'rate_min': 1.8,
            'rate_max': 9.8,
            'payment_min': 1000000,
            'payment_max': 10000000
        }
        Offer.objects.create(**self.offer_attrubutes)

    def test_get_offer_list(self):
        """ Ensure we can get an object list. """
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Offer.objects.count(), 1)
        for i in range(len(response.data)):
            self.assertEqual(response.data[i].items(), self.offer_attrubutes.items())

    def test_get_offer(self):
        """ Ensure we can get a singular object. """
        pk = 1
        response = self.client.get(self.url + f'{pk}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.items(), self.offer_attrubutes.items())

    def test_create_offer(self):
        """ Ensure we can create a new offer object. """
        create_offer_attributes = {
            'id': 2,
            'bankname': 'TestBank2',
            'term_min': 15,
            'term_max': 25,
            'rate_min': 2,
            'rate_max': 7.4,
            'payment_min': 1500000,
            'payment_max': 8000000
        }
        offers_count = Offer.objects.count()
        response = self.client.post(self.url, data=create_offer_attributes, format='json')
        id = response.data.get('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), offers_count + 1)
        obj = Offer.objects.get(id=id)
        obj = model_to_dict(obj)
        self.assertEqual(obj, create_offer_attributes)

    def test_patch_offer(self):
        """ Ensure we can update an object. """
        patch_offer_attritutes = {
            'id': 1,
            'bankname': 'TestBank3',
            'term_min': 13,
            'term_max': 29,
            'rate_min': 1.9,
            'rate_max': 8,
            'payment_min': 1700000,
            'payment_max': 6000000
        }
        id = patch_offer_attritutes['id']
        offers_count = Offer.objects.count()
        response = self.client.patch(self.url + f'{id}/', data=patch_offer_attritutes, format='json')
        obj = Offer.objects.get(id=id)
        obj = model_to_dict(obj)
        self.assertEqual(obj, patch_offer_attritutes)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Offer.objects.count(), offers_count)

    def test_delete_offer(self):
        """ Ensure we can delete an object. """
        offers_count = Offer.objects.count()
        id = 1
        response_del = self.client.delete(self.url + f'{id}/', format='json')
        response_get = self.client.get(self.url + f'{id}/', format='json')
        self.assertEqual(response_del.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Offer.objects.count(), offers_count - 1)

    def test_get_filtered_object_list(self):
        offer2_attrubutes = {
            'bankname': 'TestBank2',
            'term_min': 15,
            'term_max': 25,
            'rate_min': 3,
            'rate_max': 7,
            'payment_min': 1500000,
            'payment_max': 6000000
        }
        Offer.objects.create(**offer2_attrubutes)
        query_params = (
                '?rate_min=3&' +
                'rate_max=7&' +
                'payment_min=1500000&' +
                'payment_max=10000000&' +
                'price=10000000&' +
                'deposit=10&' +
                'term=20'
        )
        expected = {
            "id": 1,
            "bankname": "TestBank1",
            "term_min": 10,
            "term_max": 30,
            "rate_min": 1.8,
            "rate_max": 9.8,
            "payment_min": 1000000,
            "payment_max": 10000000,
        }
        response = self.client.get(self.url + query_params, format='json')
        response.data[0].pop('payment')
        response = json.dumps(response.data[0])
        expected = json.dumps(expected)
        self.assertEqual(response, expected)
