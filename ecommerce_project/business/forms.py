from django import forms

class Forms_stores(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=150)
    phone_number = forms.IntegerField()
    schedules = forms.CharField(max_length=100)