from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
#
# def shop(request):
#     products = Product.objects.filter(available=True)
#     return render(request, 'shop/product/shop.html', {'products': products})


def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/shop.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


# def product_detail(request, id):
#     try:
#         product = Product.objects.get(pk=id)
#     except Product.DoesNotExist:
#         raise Http404("Product does not exist")
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product})


def product_detail(request, id, slug=None):
    product = get_object_or_404(Product, id=id, available=True, slug=slug)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
