from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=75, default='')
    email = models.EmailField(default='')
    message = models.TextField(default='')

    def __str__(self):
        return f'{self.email}'
