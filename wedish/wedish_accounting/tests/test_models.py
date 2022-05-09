from django.test import TestCase
from wedish_accounting.models import Payment, Order, VAT, Bill
from wedish_pub.models import Table




class PaymentModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            total_price=100.00
        )
        self.bill = Bill.objects.create(
            order =self.order, #create order
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

        

class VATModelTest(TestCase):

    def setUp(self):
        self.vat = VAT.objects.create(
        rate=21.00
        )

    def test_vat_creation(self):
        vat = self.vat
        self.assertTrue(isinstance(vat, VAT))

    def test_unit_rate_content(self):
        vat = self.vat
        self.assertEqual(vat.rate, 21.00)

    


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

