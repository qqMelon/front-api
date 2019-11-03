import factory
from ..models import Unicorn, User, UserProfile
from django.contrib.auth.hashers import make_password


class BaseUnicornFactory(factory.DjangoModelFactory):
    """
    Define Customer Factory
    """

    class Meta:
        model = Unicorn

    color = "Blanc"
    model = "Model S"
    price = 9.9
    img_url = "random.png"
    available = True


class SimpleUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = "user@user.com"
    username = "simpleUser"
    password = factory.LazyFunction(lambda: make_password("useruser"))

    is_active = True


class AdminUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("email",)

    email = "admin@admin.com"
    username = "adminUser"
    password = factory.LazyFunction(lambda: make_password("adminadmin"))

    is_superuser = True
    is_staff = True
    is_active = True


class AdminUserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    address = "2 rue de la soif"


class SimpleUserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    address = "2 rue de la boisson"
