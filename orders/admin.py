from django.contrib import admin
from .models import Order, OrderItem
from .forms import OrderCreateAdminForm
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ['price','total']
    

    def total(self, obj):
        if obj.price is not None and obj.quantity is not None:
            return obj.get_cost()
        return ''

    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderCreateAdminForm
    list_display = ['user', 'address_to', 'created', 'updated', 'paid', 'total']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemAdmin]
    readonly_fields = ['total']
    # autocomplete_fields = ['address_to']
    

    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results


    def total(self, obj):
        if obj.created is not None :
            return  sum(item.get_cost() for item in obj.items.all())
        return ''
    total.short_description = "Total Cost"
