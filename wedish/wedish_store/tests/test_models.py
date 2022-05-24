from django.test import TestCase
from wedish_store.models import Brand, Product, GenericProduct, ProductAllergen, Service

# Create your tests here.


class BrandModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name='Utenos mesa')

    def test_brand_creation(self):
        brand = self.brand
        self.assertTrue(isinstance(brand, Brand))

    def test_brand_name_content(self):
        brand = self.brand
        self.assertEqual(brand.name, 0)
    
    def test_name_str(self):
        brand = self.brand
        self.assertEqual(str(brand), "0")


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Kiaulienos išpjova')

    def test_brand_creation(self):
        product = self.product
        self.assertTrue(isinstance(product, Product))

    def test_brand_name_content(self):
        product = self.product
        self.assertEqual(product.name, 0)
    
    def test_name_str(self):
        product = self.product
        self.assertEqual(str(product), "0")


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name='Baras')

    def test_service_creation(self):
        service = self.service
        self.assertTrue(isinstance(service, Service))

    def test_service_name_content(self):
        service = self.service
        self.assertEqual(service.name, 0)
    
    def test_service_str(self):
        service = self.service
        self.assertEqual(str(service), "0")


class GenericProductModelTest(TestCase):
    def setUp(self):
        self.generic_product = GenericProduct.objects.create(name='Coca cola')

    def test_service_creation(self):
        generic_product = self.generic_product
        self.assertTrue(isinstance(generic_product, GenericProduct))

    def test_service_name_content(self):
        generic_product = self.generic_product
        self.assertEqual(generic_product.name, 0)
    
    def test_service_str(self):
        generic_product = self.generic_product
        self.assertEqual(str(generic_product), "0")


class ProductAllergenModelTest(TestCase):
    def setUp(self):
        self.product_allergen = ProductAllergen.objects.create(name='Kiaulienos išpjova')