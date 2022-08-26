from django.shortcuts import render

# Create your views here.

class Home(LoginRequiredMixin, ListView):
    model = Home #modelo que se va a mostrar
    template_name = 'home/home.html' # template que se va a mostrar
