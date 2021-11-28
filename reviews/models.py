from django.db import models
from django.utils import timezone
from profiles.models import UserProfile


class Review(models.Model):
    """
    Model so users so write reviews on products
    """
    title = models.CharField(max_length=150)
    comments = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

