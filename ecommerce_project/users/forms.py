
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class User_registration_form(UserCreationForm):
   
    password1= forms.CharField(label='Password',widget=forms.PasswordInput)
    password2= forms.CharField(label='Password confirmation',widget=forms.PasswordInput)
    


    class Meta:
        model=User
        fields=('username','password1', 'password2')
        help_texts={k:'' for k in fields} 


class Profile_form(forms.ModelForm):
    name= forms.CharField(label='Nombre')
    surname= forms.CharField(label='Apellido')
    email=forms.EmailField(label='Email')
    birth_date= forms.DateField(label='Fecha de nacimiento')
    phone_number= forms.IntegerField(label='Telefono')
    address= forms.CharField(label='Direccion')

    class Meta:
        model = Profile
        fields=('name','surname','email','birth_date', 'phone_number','address')

    
