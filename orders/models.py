from django.db import models
from django.core.exceptions import ValidationError
from shop.models import Product
from account.models import User, Address 

    

class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE, blank=True)
    address_to = models.ForeignKey(Address,
                                   related_name="orders",
                                   on_delete=models.DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    # prevent create a order in the admin where the address dosen't bellow to the user
    def clean(self):
        super().clean()
        if self.address_to not in self.user.addresses.all():
            raise ValidationError("the address must bellow to the user")

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity