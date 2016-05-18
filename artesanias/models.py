from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Artesano(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    calle=models.CharField(max_length=100)
    num_dir=models.CharField(max_length=10)
    clave_ref = models.IntegerField("Clave de referencia",)
    rfc = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Telefono(models.Model):
    Telefono = models.CharField(max_length=100)
    telefonos = models.ForeignKey(Artesano, on_delete=models.CASCADE)
    def __str__(self):
        return self.Telefono

class Artesania(models.Model):
    titulo=models.CharField(max_length=15)
    artesano = models.ForeignKey(Artesano, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=500)
    precio=models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    categoria=(
        ('TM', 'Talla de Madera'),
        ('CE','Cerámica'),
        ('TJ','Tejido'),
        ('VI','Vidrio'),
        ('OR','Orfebrería'),

    )
    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    pedidos = models.ManyToManyField(Artesania, through="Pedido")
    telefono = models.IntegerField()
    estado=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    calle=models.CharField(max_length=100)
    num_dir=models.CharField(max_length=10)
    def __str__(self):
        return self.user.username

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    artesania = models.ForeignKey(Artesania, on_delete=models.CASCADE)
    fecha_pedio=models.DateTimeField('Fecha de Registro')
    fecha_entrega=models.DateTimeField('Fecha de Entrega')



