from .cart import Cart

def get_cart(request):
    cart = Cart(request)
    return {"context_cart" : cart}