from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.views.decorators.http import require_GET
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm

from .tasks import order_created


def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request=request)

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
            order_created.delay(order.id)

            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment

            return redirect(reverse('payment:process'))

    # Temporary change
    # return render(request, 'orders/created.html', {'order': order})

    else:
        form = OrderCreateForm(request=request)
    return render(request, 'orders/create.html', {'form': form})

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order,id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})

@require_GET
def get_updated_order_form(request):
    """returns and updated version of order_form"""
    form = OrderCreateForm(request=request)    
    return render(request, 'orders/snippets/order_form.html', {'form': form})

