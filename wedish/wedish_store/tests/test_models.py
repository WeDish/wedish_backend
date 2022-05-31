from django.test import TestCase
from wedish_store.models import Brand, Product, GenericProduct, ProductAllergen, Service

# Create your tests here.


class BrandModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Utenos mesa')

    def test_brand_creation(self):
        brand = self.brand
        self.assertTrue(isinstance(brand, Brand))
    
    def test_name_str(self):
        brand = Brand.objects.get(id=1)
        self.assertEqual(str(brand.name), 'Utenos mesa')
        expected_string = f"{brand.name}"
        self.assertEqual(str(brand), expected_string)


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Kiaulienos išpjova')

    def test_brand_creation(self):
        product = self.product
        self.assertTrue(isinstance(product, Product))
    
    def test_name_str(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), "Kiaulienos išpjova")
        expected_string = f"{product.name}"
        self.assertEqual(str(product), expected_string)


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name='Baras')

    def test_service_creation(self):
        service = self.service
        self.assertTrue(isinstance(service, Service))
    
    def test_service_str(self):
        service = Product.objects.get(id=1)
        self.assertEqual(str(service), "Baras")
        expected_string = f"{service.name}"
        self.assertEqual(str(service), expected_string)


class GenericProductModelTest(TestCase):
    def setUp(self):
        self.generic_product = GenericProduct.objects.create(name='Coca cola')

    def test_service_creation(self):
        generic_product = self.generic_product
        self.assertTrue(isinstance(generic_product, GenericProduct))
    
    def test_service_str(self):
        generic_product = Product.objects.get(id=1)
        self.assertEqual(str(generic_product), "Baras")
        expected_string = f"{generic_product.name}"
        self.assertEqual(str(generic_product), expected_string)
