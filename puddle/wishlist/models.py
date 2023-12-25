from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Wishlist(models.Model):
    user = models.OneToOneField(User, related_name="wishlist", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="wishlists")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name