from django.db import models

class Products(models.Model):
    product_id = models.CharField(max_length=10)
    subcategory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    popularity = models.IntegerField()

    def __str__(self):
        return self.title
