from django.test import TestCase
from .models import Good, GoodIngradient

# Create your tests here.


class GoodModelTest(TestCase):

    def test_string_representation(self):
        entry = Good(name="test product", recommended_retail_price=1.99)
        self.assertEqual(str(entry), f'{entry.name} ({entry.category}): {entry.recommended_retail_price} EUR')

class GoodIngradientModelTest(TestCase):

    def test_string_representation(self):
        good = Good(name="test product", recommended_retail_price=1.99)
        entry = GoodIngradient(good=good, quantity=1.99)
        self.assertEqual(str(entry), f'{entry.good}: {entry.ingradient} {entry.quantity}{entry.unit}')