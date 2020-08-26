from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/products")
    ENVELOPE = 'ENV'
    GIFT_TAG = 'GTA'
    WINE_BAG = 'WBA'
    PRODUCT_CHOICES = [
        (ENVELOPE, 'Envelope'),
        (GIFT_TAG, 'Gift Tag'),
        (WINE_BAG, 'Wine Bag')
    ]
    product_type = models.CharField(
        max_length=3, choices=PRODUCT_CHOICES, default=ENVELOPE)

    def __str__(self):
        return self.name
