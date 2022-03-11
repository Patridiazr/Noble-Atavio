from pyexpat import model
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Pedido(models.Model):
    # id_pedido = models.AutoField(primary_key=True)
    rut_cliente = models.CharField(max_length=12)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    fecha_entrega = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=200)
    telefono_cliente = models.CharField(max_length=10)
    email_cliente = models.CharField(max_length=50)
    informacion_pedido = models.CharField(max_length=500)

class Producto(models.Model):
    # id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio_oferta = models.CharField(max_length=30)
    precio_real = models.CharField(max_length=30)

