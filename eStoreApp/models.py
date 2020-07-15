from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

TYPE = (
    ('Mobile', 'Mobile'),
    ('Laptop', 'Laptop')
    )


class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=False)
    product_type = models.CharField(max_length=15, choices=TYPE ,default ="Mobile", blank=False)
    processor = models.TextField(blank=False, null=False)
    RAM = models.TextField(blank=False, null=False)
    screen_size = models.TextField(blank=False, null=False)
    color = models.TextField(blank=False, null=False)
    hd_capacity = models.TextField(blank=False, null=False)


    def __str__(self):
        return 'Id: {}, \n Name: {}, \n Type: {}, \n '.format(self.id, self.name, self.product_type)


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(null=False, blank=False, upload_to='productImages/')