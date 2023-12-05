from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    else:
        print('is invalid')
        print(request.POST)

        # # managing the cart updated
        # if cd['override'] == True:
        #     return HttpResponse(cd['quantity'])   
        # mejor recargar todo

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    if request.method == "DELETE":
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
    # return redirect('cart:cart_detail')
    return HttpResponse('')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

# def cart_edit(request, product_id):
#     cart = Cart(request)
#     product = cart.cart[str(product_id)]
#     return render(request, 'cart/edit_quantity.html', {'quantity':product['quantity'],
#                                                         'product_id': product_id})
