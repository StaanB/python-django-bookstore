import factory
from factory import SubFactory
from django.contrib.auth.models import User
from product.factories import ProductFactory
from order.models import Order

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')

    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)

    class Meta:
        model = Order
