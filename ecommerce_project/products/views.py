from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Forms_products

# @login_required


def create_product(request):
    # if request.user.is_superuser:
    if request.method == 'POST':
        form = Forms_products(request.POST, request.FILES)

        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                stock=form.cleaned_data['stock'],
                size=form.cleaned_data['size'],
                #image = form.cleaned_data['image']
            )

            return redirect(products_list)

    elif request.method == 'GET':
        form = Forms_products()
        context = {'form': form}
        return render(request, 'products/new_product.html', context=context)
    # return redirect('login')

# @login_required
def update_product(request, pk):
    if request.method == 'POST':
        form = Forms_products(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.stock = form.cleaned_data['size']
            product.save()

            return redirect(products_list)

    elif request.method == 'GET':
        product = Products.objects.get(id=pk)

        form = Forms_products(initial={
                                        'name':product.name,
                                        'price':product.price, 
                                        'description':product.description,
                                        'stock':product.stock})
        context = {'form':form}
        return render(request, 'products/update_product.html', context=context)

# @login_required
def products_list(request):
    products = Products.objects.all()  # Trae todos
    context = {
        'products': products
    }
    return render(request, 'products/products_list.html', context=context)


def menu(request):
    return render(request, 'products/menu.html', context={})


def search_products(request):
    search = request.GET['search']
    print(search)
    products = Products.objects.filter(name__icontains=search)
    print(products)
    context = {'products': products}
    return render(request, 'products/search_products.html', context=context)

# @login_required
def delete_product(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(pk=pk)
        context = {'product':product}
        return render(request, 'products/delete_product.html', context=context)
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(products_list)

