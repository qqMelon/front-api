from django.test import TestCase
from ..models import Unicorn


class UnicornTest(TestCase):
    """ Test Unicorn model """

    def setUp(self):
        Unicorn.objects.create(
            name="Bernard",
            color="Bleue",
            model="Dark edition",
            price=9.9,
            img_url="https://cdn.shopify.com/s/files/1/2551/6908/products/unicorn-01_300x.png?v=1543257623",
            available=True,
        )
        Unicorn.objects.create(name="Jean", model="Model S", price=87.96)

    def test_Unicorn(self):
        unicorn_bernard = Unicorn.objects.get(name="Bernard")
        unicorn_jean = Unicorn.objects.get(name="Jean")
        self.assertEqual(unicorn_bernard.model, "Dark edition")
        self.assertEqual(unicorn_jean.model, "Model S")
