from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(max_length=4096)

    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    #category = models.ForeignKey(Category, related_name='products')

    name = models.CharField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()

    available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
