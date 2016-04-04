from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(max_length=4096)

    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_index_by_category', args=[self.slug])


@python_2_unicode_compatible
class Product(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sale', 'For Sale'),
        ('onstock', 'On Stock'),
        ('notavailble', 'Not Available'),
    )

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='available')

    category = models.ForeignKey(Category, verbose_name='category', related_name='products')

    slug = models.SlugField(max_length=200, db_index=True, unique=True)

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

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
