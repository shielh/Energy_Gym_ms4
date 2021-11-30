from django.db import models

from profiles.models import UserProfile
from checkout.models import Order


class Contact(models.Model):
    user = models.ForeignKey(
        UserProfile, related_name='contact', on_delete=models.CASCADE,
        blank=True, null=True)
    email = models.ForeignKey(
        Order, related_name='contact', on_delete=models.CASCADE,
        blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.user}'
