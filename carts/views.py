from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect

# from orders.models import Order
from products.models import Product
from .models import Cart



def cart_detail(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    products = [{
            "id":x.id,
            "url":x.get_absolute_url(),
            "name":x.name,
            "price":x.price
            }
            for x in cart_obj.products.all()]
    cart_data = {"products":products,"subtotal":cart_obj.subtotal,"total":cart_obj.total}
    return JsonResponse(cart_data)


def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request,"carts/home.html",{"cart":cart_obj})



def cart_update(request):
    product_id = request.POST.get('products_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:

            print("show message to user,product is gone?")
            return redirect("cart:home")
        cart.obj.new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.procucts.remove(procuct_obj)
            added = False
        else:
            cart_obj.procucts.add(procuct_obj)
            added = True

        request.session['cart_items'] =  cart_obj.procucts.count()
        if request.is_ajax():
            print("Ajax request")
            json_data = {
                "added":added,
                "removed":not added,
                "cartItemCount":cart_obj.products.count()
            }
    return redirects("cart:home")

