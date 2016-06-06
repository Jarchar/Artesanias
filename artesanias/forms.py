from django.forms import ModelForm
from artesanias.models import Artesano, Artesania, Cliente

class Artesania(ModelForm):
    class Meta:
        model=Artesania
        fields=['titulo', 'imagen', 'artesano', 'descripcion', 'precio']

