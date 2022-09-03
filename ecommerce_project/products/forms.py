from distutils.command.upload import upload
from random import choices
from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import Products


class Forms_products(forms.ModelForm):
    choices = [('S', 'S'), ('M', 'M'), ('L', 'L'),
               ('XL', 'XL'), ('XXL', 'XXL')]
    size = forms.ChoiceField(choices=choices)

    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'stock', 'size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ImageField(required=False)
        }



'''
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    size = forms.CharField(max_length=5)
    #available = forms.BooleanField(default=True)    
    #image = forms.ImageField(upload_to='products/%Y/%m/%d', blank=True)
'''


class Forms_category(forms.Form):
    name = forms.CharField(max_length=50)

       
        
       
       