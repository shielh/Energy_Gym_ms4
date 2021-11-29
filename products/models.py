from django.db import models
from django.utils import timezone
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model so users so write reviews on products
    """
    title = models.CharField(max_length=150)
    comments = models.TextField(max_length=1000)
    rating = models.IntegerField()
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE,
        blank=True, null=True)
    user = models.ForeignKey(
        UserProfile, related_name='reviews', on_delete=models.CASCADE,
        blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
