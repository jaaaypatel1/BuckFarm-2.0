from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'products.html', {'products': products})  # Render the template with products
