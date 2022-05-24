from django.test import TestCase
from django.utils.timezone import now
from wedish_menu.models import Menu, Category, MenuItem
from wedish_recipy.models import Good, VAT


class MenuTestCase(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(
            name='Daily menu 365',
            valid_from = now(),
            valid_until = now(),
            publicity = 1
        )
        self.menu2 = Menu.objects.create(
            name='Very very long name. Name is longer then you can think. Its not funny. No money, no funny.',
        )
        self.menu3 = Menu.objects.create(
        name='x',
        )
        self.category1 = Category.objects.create(
            name='Something very tasty',
            depth = 1,
            numchild = 1,
        )

    def test_menu_creation(self):
        menu1 = self.menu1
        self.assertTrue(isinstance(menu1, Menu))
        menu2 = self.menu2
        self.assertTrue(isinstance(menu2, Menu))
        menu3 = self.menu3
        self.assertTrue(isinstance(menu3, Menu))
        
    def test_category_creation(self):
        category1 = self.category1
        self.assertTrue(isinstance(category1, Category))

    def test_string_method(self):
        menu1 = Menu.objects.get(id=1)
        today_date = '2022-05-24'
        self.assertEqual(str(menu1.name), 'Daily menu 365')
        self.assertEqual(str(menu1.valid_from), today_date)
        self.assertEqual(str(menu1.valid_until), today_date)
        expected_string = f"{menu1.name} - {menu1.publicity}"
        self.assertEqual(str(menu1), expected_string)
        menu2 = Menu.objects.get(id=2)
        self.assertEqual(str(menu2.name), 'Very very long name. Name is longer then you can think. Its not funny. No money, no funny.')
        menu3 = Menu.objects.get(id=3)
        self.assertEqual(str(menu3.name), 'x')
        category1 = Category.objects.get(id=1)
        self.assertEqual(str(category1.name), 'Something very tasty')
