from django import forms

class Forms_products(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=200, null=True, blank=True)
    stock = forms.IntegerField()
    size = forms.CharField(max_length=5) # S, M, L, XL, XXL
    #image = models.ImageField(upload_to='images/', null=True, blank=True)