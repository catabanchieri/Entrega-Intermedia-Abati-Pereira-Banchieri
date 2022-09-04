
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
            profile=Profile.objects.create(user=u,name=form.cleaned_data['name'],surname=form.cleaned_data['surname'],email=form.cleaned_data['email'],birth_date=form.cleaned_data['birth_date'],phone_number=form.cleaned_data['phone_number'],address=form.cleaned_data['address'])

            
            return render (request, 'home/index.html',context={})  
        
         return render(request,'users/create_profile.html',{'error': 'Datos incorrectos','form':form})
        

    elif request.method == 'GET':
        form = Profile_form()
        context = {'form':form}
        return render(request, 'users/create_profile.html', context=context)

#ver perfil de usuario
@login_required
def user_profile(request):
    profile=Profile.objects.filter(user=request.user.id)
    return render(request,'users/user_profile.html',context={})

@login_required
def update_profile(request):
    if request.method=='GET':
        
        profile=Profile.objects.get(user=request.user.id)
         
        form =Profile_form(initial={'name':profile.name,'surname':profile.surname, 'email':profile.email,'birth_date':profile.birth_date,'phone_number':profile.phone_number,'address':profile.address})
        context={'form':form}
        return render(request,'users/update_profile.html',context=context)
        
        
    
    elif request.method=='POST':
        form=Profile_form(request.POST)
        if form.is_valid():
            profile=Profile.objects.get(user=request.user.id)
            profile.name=form.cleaned_data['name']
            profile.surname=form.cleaned_data['surname']
            profile.email=form.cleaned_data['email']
            profile.birth_date=form.cleaned_data['birth_date']
            profile.phone_number=form.cleaned_data['phone_number']
            profile.address=form.cleaned_data['address']
            profile.save()

            return redirect(user_profile)

@login_required
def delete_profile(request):
    if request.method=='GET':
        profile=Profile.objects.get(user=request.user.id)
        context={'profile':profile}
        return render(request,'users/delete_profile.html',context)
    
    elif request.method=='POST':
        profile=Profile.objects.get(user=request.user.id)
        profile.delete()
        return redirect(user_profile)


