from django.test import TestCase
from wedish_accounting.models import Payment, Order, Bill


class PaymentModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            total_price=100.00
        )
        self.bill = Bill.objects.create(
            order =self.order,   
            total_price=100,
            discount=10,
            tips=2.00
        )
        self.payment = Payment.objects.create(payment_method='Cash', currency='EUR', bill=self.bill)

    def test_payment_creation(self):
        payment = self.payment
        self.assertTrue(isinstance(payment, Payment))

    def test_payment_method_content(self):
        payment=Payment.objects.get(id=1)
        expected_payment_method = f'{payment.payment_method}'
        self.assertEqual(expected_payment_method, 'Cash')

    def test_currency_content(self):
        payment=Payment.objects.get(id=1)
        expected_currency = f'{payment.currency}'
        self.assertEqual(expected_currency, 'EUR')


class OrderModelTest(TestCase):
    def setUp(self):
        self.order= Order.objects.create(
            total_price=100.00,
        )

    def test_order_creation(self):
        order = self.order
        self.assertTrue(isinstance(order, Order))

    def test_order_total_price_content(self):
        order = self.order
        self.assertEqual(order.total_price, 0)

    def test_order_str(self):
        order = self.order
        self.assertEqual(str(order), "0")

