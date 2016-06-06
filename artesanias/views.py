from django.shortcuts import render
from artesanias.models import Artesania
from django.views.generic import DetailView, ListView, CreateView

# Create your views here.
class ArtesaniaList(ListView):
    model = Artesania
    fields =['titulo','artesano', 'descripcion', 'imagen','precio']
    template_name = 'artesanias/galeria.html'

class ArtesaniaCrear(CreateView):
    model = Artesania
    fields =['titulo','artesano', 'descripcion', 'imagen','precio']
    template_name='artesanias/registro.html'

class ArtesaniaDetalle(DetailView):
    model = Artesania
    #fields =['titulo', 'artesano','descripcion', 'precio', 'categoria']
    template_name='artesanias/artesania_detalle.html'

