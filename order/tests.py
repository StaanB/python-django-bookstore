from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product, Category
from order.serializers import OrderSerializer

class OrderSerializerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(title='Category 1', slug='category-1')
        self.product = Product.objects.create(title='Product 1', description='Description', price=10, active=True)
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.order = Order.objects.create(user=self.user)
        self.order.product.add(self.product)

        self.token = Token.objects.create(user=self.user)

    def test_order_serializer(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        data = {
            'product': [self.product.id],
            'total': 10,
            'user': self.user.id,
        }
        serializer = OrderSerializer(instance=self.order, data=data)
        self.assertTrue(serializer.is_valid())
        order_data = serializer.data
        self.assertEqual(order_data['product'], [self.product.id])
        self.assertEqual(order_data['total'], 10)
        self.assertEqual(order_data['user'], self.user.id)
