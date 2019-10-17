from django.db import models


# Create your models here.
class Unicorn(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    color = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255)
    price = models.FloatField()
    available = models.BooleanField()

    class Meta:
        ordering = ["created"]
