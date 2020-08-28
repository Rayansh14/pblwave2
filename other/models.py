from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    review = models.TextField()

    def __str__(self):
        return self.name
