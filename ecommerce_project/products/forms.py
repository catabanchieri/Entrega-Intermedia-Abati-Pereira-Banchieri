from pyexpat import model
from django import forms

class Forms_products(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    size = forms.CharField(max_length=5)  # S, M, L, XL, XXL
    #image = forms.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    #created = forms.DateTimeField(auto_now_add=True)
    #updated = forms.DateTimeField(auto_now=True)

class Forms_category(forms.Form):
    name = forms.CharField(max_length=50)

       
        
       
       