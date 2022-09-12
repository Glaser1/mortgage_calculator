from django.test import TestCase
from api.models import Offer


class OfferModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.offer = Offer.objects.create(
            bankname='TestBank',
            term_min=10,
            term_max=30,
            rate_min=1.8,
            rate_max=9.8,
            payment_min=1000000,
            payment_max=10000000
        )

    def test_object_name_is_bankname_field(self):
        """ Ensure offer model is represented as it's bankname field. """
        offer = OfferModelTest.offer
        self.assertEqual(offer.bankname, str(offer))

    def test_offer_help_text(self):
        """ Ensure oferr's help text is represented in correct way. """
        offer = OfferModelTest.offer
        field_help_text = {
            'bankname': 'Укажите название банка',
            'term_min': 'Введите минимальный срок ипотеки',
            'term_max': 'Введите максимальный срок ипотеки',
            'rate_min': 'Введите минимальную ставку',
            'rate_max': 'Введите максимальную ставку',
            'payment_min': 'Введите минимальную сумму кредита',
            'payment_max': 'Введите максимальную сумму кредита'
        }
        for field, expected in field_help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    offer._meta.get_field(field).help_text,
                    expected
                )

    def test_offer_verbose_name(self):
        """ Ensure oferr's verboses is represented in correct way. """
        offer = OfferModelTest.offer
        field_verboses = {
            'bankname': 'Название банка',
            'term_min': 'Срок ипотеки, ОТ',
            'term_max': 'Срок ипотеки, ДО',
            'rate_min': 'Ставка, ОТ',
            'rate_max': 'Ставка, ДО',
            'payment_min': 'Сумма кредита, ОТ',
            'payment_max': 'Сумма кредита, ДО'
        }
        for field, expected in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    offer._meta.get_field(field).verbose_name,
                    expected
                )
