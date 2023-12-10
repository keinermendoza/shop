from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:
    def __init__(self, request):
        """gets the cart from session or create a new cart if not exists"""
        self.session = request.session
        # get the cart from the session
        cart = self.session.get(settings.SESSION_CART_ID)

        # if there is no cart in session
        if not cart:
            #  i put a 'cart' on it, and nex asing it to the cart property
            cart = self.session[settings.SESSION_CART_ID] = {}
        self.cart = cart


    def __iter__(self):
        """returns dictionaries with nesteds product instances"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # use an inbond method to get a copy of the cart
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        
        for item in cart.values():

            # this keep with the price when user add item
            # the proble if that if a user add one, the he can put as many he want and always remainds the same price until he cheakout 
            # item['price'] = Decimal(item['price'])

            # i prefer the keep the price updated
            item['price'] = Decimal(item['product'].price)
            item['total_price'] = item['price'] * item['quantity']
        
            yield item

    def __len__(self):
        """return the total num of items in the cart"""
        # i need to call values beacuse the default iteration is over the keys
        return sum(product['quantity'] for product in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """add a product or changes it's quantity 
        recieves: product instances and sotres json"""

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """tells django to store the changes, in this case in the database"""
        self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    # I thinks this works well
    def get_total_price(self):
        return sum(item['total_price'] for item in self)

    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.SESSION_CART_ID]
        self.save()