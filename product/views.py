from django.shortcuts import render, get_object_or_404
from .models import Product


def envelopes(request):
    products = Product.objects.all().order_by('name')
    envelopes = []
    for product in products:
        if product.product_type == 'ENV':
            envelopes.append(product)
    return render(request, 'product.html', {'products': envelopes})


def wineBags(request):
    products = Product.objects.all().order_by('name')
    wineBags = []
    for product in products:
        if product.product_type == 'WBA':
            wineBags.append(product)
    return render(request, 'product.html', {'products': wineBags})


def giftTags(request):
    products = Product.objects.all().order_by('name')
    giftTags = []
    for product in products:
        if product.product_type == 'GTA':
            giftTags.append(product)
    return render(request, 'product.html', {'products': giftTags})
