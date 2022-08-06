from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Forms_products

def create_product(request):
    
    if request.method == 'POST':
        form = Forms_products(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                stock = form.cleaned_data['stock'],
                size = form.cleaned_data['size']
            )
            
            return redirect(products_list)

    elif request.method == 'GET':
        form = Forms_products()
        context = {'form':form}
        return render(request, 'products/new_product.html', context=context)

def products_list(request):
    products = Products.objects.all() #Trae todos
    context = {
        'products':products
    }
    return render(request, 'products/products_list.html', context=context)