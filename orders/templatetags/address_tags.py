from django import template 
from account.forms import AddresForm

register = template.Library()

@register.inclusion_tag('orders/snippets/register_address_form.html')
def address_form():
    return {'form':AddresForm()}