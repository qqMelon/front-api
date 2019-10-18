from django.db import models


# Create your models here.
class Unicorn(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    name = models.CharField(
        max_length=255, blank=True, null=True, default="", verbose_name="Nom"
    )
    color = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Couleur"
    )
    model = models.CharField(max_length=255, verbose_name="Modele")
    price = models.FloatField(verbose_name="Prix")
    img_url = models.CharField(max_length=255, blank=True, null=True,verbose_name="Url de l'image")
    available = models.BooleanField(verbose_name="Disponible")

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.name
