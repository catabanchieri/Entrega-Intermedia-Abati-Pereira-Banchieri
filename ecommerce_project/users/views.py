
from collections import UserList
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form, Profile_form
from django.contrib.auth.views import LogoutView
from users.models import Profile

# Create your views here.

def login_request(request):
    if request.method=='POST':
        form= AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                context={'message' :f'{username} Bienvenido a TIENDA !!, Encontraras tu prenda ideal!'}
                return render (request, 'home/index.html',context=context)     
        
        return render(request,'users/login.html',{'error': 'Usuario o contraseña incorrectas','form':form})
    
    elif request.method=='GET':
        form=AuthenticationForm()
        return render (request,'users/login.html',{'form':form})

def register(request):
    if request.method=='POST':
        form=User_registration_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
        
        context={'errors':form.errors}
        form= User_registration_form
        context['form']=form
        return render(request, 'users/register.html',{'form':form})

    elif request.method=='GET':
        form=User_registration_form()
        return render(request,'users/register.html',{'form':form})


# ## PERFILES
def create_profile(request):
    if request.method=='POST':
         form=Profile_form(request.POST)
         if form.is_valid():
             form.save()
             return render (request, 'home/index.html',context=context)  
        

    elif request.method == 'GET':
         form = Profile_form()
         context = {'form':form}
         return render(request, 'users/new_profile.html', context=context)
     
