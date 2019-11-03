from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="uploads", blank=True)


class Unicorn(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    name = models.CharField(max_length=255, verbose_name="Nom")
    color = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Couleur"
    )
    model = models.CharField(max_length=255, verbose_name="Modele")
    price = models.FloatField(verbose_name="Prix")
    img_url = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Url de l'image"
    )
    available = models.BooleanField(
        verbose_name="Disponible", blank=True, null=True, default=False
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.name
