import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pystr")
    title = factory.Faker("pystr")
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Product
