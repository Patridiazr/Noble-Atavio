from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Pedido(models.Model):
    # id = models.IntegerField(max_length=50)
    rut_cliente = models.CharField(max_length=12)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    fecha_entrega = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=200)
    telefono_cliente = models.IntegerField(max_length=10)
    email_cliente = models.CharField(max_length=50)
    informacion_pedido = models.CharField(max_length=500)
