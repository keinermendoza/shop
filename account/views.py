from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import AddresForm

@require_POST
def registerAddressView(request):
    form = AddresForm(request.POST)
    if form.is_valid():
        address = form.save(commit=False)
        address.user = request.user
        address.save()

        form = AddresForm()
        response =  render(request, 'orders/snippets/register_address_form.html', {'form': form})
        response["HX-Trigger"] = 'reload_address_options'
        return response
    
    return render(request, 'orders/snippets/register_address_form.html', {'form': form})
    