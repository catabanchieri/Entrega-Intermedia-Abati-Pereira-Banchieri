from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Articles

# clases basadas en vistas
class List_articles(LoginRequiredMixin, ListView):
    model = Articles #modelo que se va a mostrar
    template_name = 'articles/list_articles.html' # template que se va a mostrar

class Detail_article(DetailView):
    model = Articles
    template_name = 'articles/detail_articles.html'

class Create_article(CreateView):
    model = Articles
    template_name = 'articles/create_article.html'
    fields = '__all__' # le indicamos que todos los campos se van a mostrar
    success_url = '/articles/list_articles/'

class Delete_article(DeleteView):
    model = Articles
    template_name = 'articles/delete_article.html'
    success_url = '/articles/list_articles/' # redireccionamos a la lista de articulos

# nos queda para nosotros hacer el UpdateView