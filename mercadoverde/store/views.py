from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Product

def home(request):
    return render(request, 'index.html')

def api(request):
    return render(request, 'api.html')


def watch_products(request):
    products = Product.objects.all()
    context = {
        'section': 'products',
        'products': products,
        'estados': {
            'A': 'Active',
            'I': 'Inactive',
        }
    }
    return render(request, 'products.html', context)

def watch_product(request, id):
    product = Product.objects.filter(id = id)
    if not product:
        return redirect('')
    context = {
        'product': product.first()
    }
    return render(request, 'product.html', context)

def about(request):
    return render(request, 'about_us.html')