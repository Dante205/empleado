from django.shortcuts import render

# Create your views here.
from django.views.generic import (
        TemplateView,
        ListView,
        CreateView
)


# importar models
from .models import Prueba
from .forms import PruebaForm


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen_foundation.html'



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'    # Es como si fuera la variable que contien la lista del "queryset"
    queryset = ['1', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm   # fields = ['titulo', 'subtitulo', 'cantidad']
    success_url = '/'
    
