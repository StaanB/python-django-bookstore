from django.test import TestCase
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

class ProductSerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Category 1', slug='category-1')
        self.product = Product.objects.create(title='Product 1', description='Description', price=10, active=True)

    def test_product_serializer(self):
        data = {
            'title': 'Product 2',
            'description': 'Description',
            'price': 20,
            'active': True,
            'category': [{'title': 'Category 2', 'slug': 'category-2'}],  # Usando slug único para categoria
        }
        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Category 1', slug='category-1')
    
    def test_category_serializer(self):
        data = {
            'title': 'Category 2',
            'slug': 'category-2',
            'description': 'Description',
            'active': True,
        }
        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid())
        category_data = serializer.data
        self.assertEqual(category_data['title'], 'Category 2')
        self.assertEqual(category_data['slug'], 'category-2')
        self.assertEqual(category_data['description'], 'Description')
        self.assertEqual(category_data['active'], True)
