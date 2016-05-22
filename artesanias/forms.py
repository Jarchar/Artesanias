from django.forms import ModelForm
from artesanias.models import Artesano, Artesania, Cliente

class ArtesanoForm(ModelForm):
    class Meta:
        model=Artesano
