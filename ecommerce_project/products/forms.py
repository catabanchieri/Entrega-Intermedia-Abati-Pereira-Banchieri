from django import forms
class Forms_products(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    size = forms.CharField(max_length=5)
    #is_active = forms.BooleanField(default=True)
    #image = forms.ImageField(upload_to='img/', null=True, blank=True)