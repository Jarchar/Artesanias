from django.shortcuts import render
from artesanias.models import Artesania
from django.views.generic import ListView

# Create your views here.
class ArtesaniaList(ListView):
    model = Artesania
    template_name = 'artesanias/artesanias.html'
