from django.shortcuts import render
from .models import Product


# Create your views here.


def shop(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/shop.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
