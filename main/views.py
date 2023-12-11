from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.all()
    return render(request, 'index.html', {'products': products,'cart_items': cart_items})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('product_list')

def cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

