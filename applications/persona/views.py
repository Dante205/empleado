from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView


# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """ Vista que carga la pagina de incio """
    template_name = 'inicio.html'
    



# ========================================= ListView ===============================================
# 1.- Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4                          # Paginacion en un ListView
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave          # __icontains -> Busca que la palabra clave esté presente en el contenido de, en este caso "full_name".
                                                        # En este caso, como la palabra_clave es vacío, todas las cadenas siempre tendran vacio al inicio o al final, por nede me muestra todos los registros
        )
        # print('lista resultado: ', lista)
        return lista
    
# Lista empleados Admin
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10                          # Paginacion en un ListView
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado



# 2.- Listar todos los empleados que pertenecen a un area de la empresa
class ListByAreaEmpleado(ListView):
    """ Lista de empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):

        area = self.kwargs['shorname']    # la variable "area" recoge lo que mandan luego del URL, es decir el parametro
        lista = Empleado.objects.filter(
        departamento__shor_name=area
    )
        return lista

class ListEmpleadosByKword(ListView):
    """ Lista de empleados por Palabra Clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("*****************************")
        palabra_clave = self.request.GET.get("kword",)
        lista = Empleado.objects.filter(
        first_name=palabra_clave
    )
        # print('lista resultado: ', lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=5)
        # print(empleado.habilidades.all())
        return empleado.habilidades.all()

# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- listar habilidades de un empleado


# ========================================= DetailView ===============================================

class EmpleadoDetailView(DetailView):
    model = Empleado                # Para DetailView, Indicar siempre el modelo del cual hará el detalle
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    


# ========================================= CreateView ===============================================

# Creamos un TemplateView para mostrarlo despues de que insertamos un registro, es decir, realizamos una peticion POST
class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']         # le indicamos en fields, os campos que vamos a registrar en las cajas de texto que se mostrarán en pantalla, y que internamente Django creará a traves de la variable {{ form }} que se podrá usar en el template
    # fields = ('__all__')                                # En lugar de especificar los campos, podemos contemplar todos los campos que contiene mi modelo
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):     # Ingresa a esta funcion, siempre y cuando, lso datos que el usuario ha ingresado al formulario es valido
        # Logica del proceso
        empleado = form.save()      # Guardamos los datos en la Base de Datos, y lo almacenamos en la variable "emmpleado"
        # print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()    # Guardamos el atributo full_name en la BASE DE DATOS
        return super(EmpleadoCreateView, self).form_valid(form)



# ========================================= UpdateView ===============================================

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')

    # Esta funcion me permite extraer campos del registro del cual se enviando la peticion POST
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********************** METODO POST ************************')
        print('========================================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


    def form_valid(self, form): 
        print('********************** METODO form valid ************************')
        print('********************************************************')
        
        return super(EmpleadoUpdateView, self).form_valid(form)



# ========================================= DeleteView ===============================================

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


