from .cart import Cart

def get_cart(request):
    cart = Cart(request)
    return {"cart" : cart}