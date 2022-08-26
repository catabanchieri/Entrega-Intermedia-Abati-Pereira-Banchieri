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
                size = form.cleaned_data['size'],
                #is_active = form.cleaned_data['is_active']
                #image = form.cleaned_data['image']
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

def menu(request):
    return render(request, 'products/menu.html', context={})

def search_products(request):
    search=request.GET['search']
    print(search)
    products=Products.objects.filter(name__icontains=search) #Trae todos los productos que contengan el criterio de busqueda
    context={'products':products}
    return render(request,'products/search_products.html',context=context)



