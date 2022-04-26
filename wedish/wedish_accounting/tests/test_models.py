from django.test import TestCase
from wedish_accounting.models import Payment


class PaymentModelTest(TestCase):


    def setUp(self):
        Payment.objects.create(payment_method='Cash', currency='EUR')


    def test_payment_method_content(self):
        payment=Payment.objects.get(id=1)
        expected_payment_method= f'{payment.payment_method}'
        self.assertEqual(expected_payment_method, 'Cash')

    
    def test_currency_content(self):
        payment=Payment.objects.get(id=1)
        expected_currency= f'{payment.currency}'
        self.assertEqual(expected_currency, 'EUR')