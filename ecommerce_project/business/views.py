from ctypes import addressof
from django.shortcuts import render, redirect
from business.models import Stores
from business.forms import Forms_stores

def create_store(request):
    
    if request.method == 'POST':
        form = Forms_stores(request.POST)

        if form.is_valid():
            Stores.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number'],
                schedules = form.cleaned_data['schedules'],
            )
            
            return redirect(stores_list)

    elif request.method == 'GET':
        form = Forms_stores()
        context = {'form':form}
        return render(request, 'business/new_store.html', context=context)


def stores_list(request):
    stores = Stores.objects.all() #Trae todos
    context = {
        'stores':stores
    }
    return render(request, 'business/stores_list.html', context=context)
