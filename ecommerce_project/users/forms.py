
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_registration_form(UserCreationForm):
    email=forms.EmailField(required=True)
    password1= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Password confirmation',widget=forms.PasswordInput)
    


    class Meta:
        model=User
        fields=('username','email','password1', 'password2')
        help_texts={k:'' for k in fields} 


class Profile_form(forms.Form):
    name= forms.CharField(label='Nombre')
    surname= forms.CharField(label='Apellido')
    birth_date= forms.DateField(label='Fecha de nacimiento')
    address= forms.CharField(label='Direccion')
    
