from django.shortcuts import render
from .models import *

# Create your views here.
def sports(request) :
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'sports/sports.html', context)

def cart(request) :

    context = {}

    return render (request, 'sports/cart.html', context)

def checkout(request) :
    context = {}
    return render (request, 'sports/checkout.html', context)

def main(request) :
    context = {}
    return render (request, 'sports/main.html', context)
