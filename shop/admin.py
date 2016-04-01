from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
