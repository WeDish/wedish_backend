# from django.test import TestCase
# from django.utils.timezone import now

# from wedish_menu.models import Menu, Category, MenuItem


# class MenuTestCase(TestCase):
#     def setUp(self):
#         self.menu1 = Menu.objects.create(
#             name='Daily menu 365',
#             valid_from=now(),
#             valid_untill=now(),
#             publicity = 1
#         )
#         # self.menu2 = Menu.objects.create(
#         #     name='1234567890 1234567890 1234567890 1234567890',
#         #     # valid_from=now(),
#         #     publicity = 2
#         # )        

#     def test_string_method(self):
#         menu1 = Menu.objects.get(id=1)
#         today_date = '2022-04-21'
#         self.assertEqual(str(menu1.name), 'Daily menu 365')
#         self.assertEqual(str(menu1.valid_from), today_date)
#         self.assertEqual(str(menu1.valid_untill), today_date)
#         # menu2 = Menu.objects.get(id=2)
#         # expected_string = f"{menu2.name} - {menu2.publicity} 1"
#         # self.assertEqual(str(menu2.name), '1234567890 1234567890 1234567890 1234567890')
