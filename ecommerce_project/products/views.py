from .forms import Forms_products
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import CreateView, UpdateView, DeleteView, ListView, DetailView
class List_products(ListView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/products_list.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/products_list/')

        return render(request, self.products_list, {'form': form})
class Detail_product(DetailView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/detail_products.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/detail_products/')

        return render(request, self.products_list, {'form': form})
class Create_product(CreateView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/new_product.html'
    #fields = '__all__'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/products_list/')

        return render(request, self.products_list, {'form': form})
class Delete_product(DeleteView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/delete_product.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/products_list/')

        return render(request, self.products_list, {'form': form})
class Update_product(UpdateView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/update_product.html'
    #fields = '__all__'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/products_list/')

        return render(request, self.products_list, {'form': form})

'''
class Search_product(ListView):
    form_class = Forms_products
    initial = {'key': 'value'}
    template_name = 'products/search_product.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.products_list, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('products/products_list/')

        return render(request, self.products_list, {'form': form})
'''
   
  

 