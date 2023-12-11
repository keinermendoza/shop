import csv
import datetime 
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

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

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta 
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition

    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many \
              and not field.one_to_many]
    
    # WRITING THE HEADER ROW
    writer.writerow([field.verbose_name for field in fields])

    # AN IDEA
    # fields = [field for field in opts.get_fields() if not field.many_to_many] # \
    # writer.writerow([field.verbose_name if not field.one_to_many else 'outro' for field in fields])

    # ALL THE DATA
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)


    return response
export_to_csv.short_description = 'Export to CSV'

def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderCreateAdminForm
    list_display = ['user', 'address_to', 'created', 'updated', 'paid', 'total', order_detail]
    # list_filter = ['paid', 'created', 'updated']
    list_filter = []
    
    inlines = [OrderItemAdmin]
    readonly_fields = ['total']
    # autocomplete_fields = ['address_to']
    actions = [export_to_csv]

    # def get_search_results(self, request, queryset, search_term):
    #     print("In get search results")
    #     results = super().get_search_results(request, queryset, search_term)
    #     return results


    def total(self, obj):
        if obj.created is not None :
            return  sum(item.get_cost() for item in obj.items.all())
        return ''
    total.short_description = "Total Cost"
