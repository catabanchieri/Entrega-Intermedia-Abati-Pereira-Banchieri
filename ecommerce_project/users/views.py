
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form, Profile_form
from django.contrib.auth.views import LogoutView
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        
        
        form= User_registration_form
        
        return render(request,'users/register.html',{'error':'Datos incorrectas','form':form})
       
        

    elif request.method=='GET':
        form=User_registration_form()
        return render(request,'users/register.html',{'form':form})


# ## PERFILES

@login_required
def create_profile(request):
    if request.method=='POST':

         form=Profile_form(request.POST)
         if form.is_valid():

            u=User.objects.get(username=request.user)
            profile=Profile.objects.create(user=u,name=form.cleaned_data['name'],surname=form.cleaned_data['surname'],birth_date=form.cleaned_data['birth_date'],address=form.cleaned_data['address'])

            
            return render (request, 'home/index.html',context={})  
        
         return render(request,'users/create_profile.html',{'error': 'Datos incorrectos','form':form})
        

    elif request.method == 'GET':
        form = Profile_form()
        context = {'form':form}
        return render(request, 'users/create_profile.html', context=context)
     