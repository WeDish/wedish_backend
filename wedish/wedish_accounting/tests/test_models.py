from django.test import TestCase
from wedish_accounting.models import Payment, Order
from wedish_pub.models import Space, SpaceCategory


class PaymentModelTest(TestCase):


    def setUp(self):
        Payment.objects.create(payment_method='Cash', currency='EUR')

    def test_payment_method_content(self):
        payment=Payment.objects.get(id=1)
        expected_payment_method = f'{payment.payment_method}'
        self.assertEqual(expected_payment_method, 'Cash')

    def test_currency_content(self):
        payment=Payment.objects.get(id=1)
        expected_currency = f'{payment.currency}'
        self.assertEqual(expected_currency, 'EUR')














# class OrderModelTest(TestCase):


#     def setUp(self):
#         self.user = 

#         self.space_category = SpaceCategory.objects.create(
#             name="Bar seat",
#             description="Short seat"
#         )

#         self.space = Space.objects.create(
#             name="Bar",
#             space_category = self.space_category,
#             accepts_for_production=True,
#             description="description"
#         )

#         self.order = Order.objects.create(
#             estimated_to_complete="2022-04-27 15:37:00",
#             price=90.85,
#             completed_at="2022-04-27 15:47:00",
#             table_number= "Bar 15",
#             place = self.space,
            

#         )