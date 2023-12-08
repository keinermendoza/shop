from django.shortcuts import render
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm

def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            cart = Cart(request)
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        quantity=item['quantity'])
            cart.clear()

            return render(request, 'orders/created.html', {'order': order})

    else:
        form = OrderCreateForm(request=request)
    return render(request, 'orders/create.html', {'form': form})
