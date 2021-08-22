from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedido

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def pedidos(request):
    pedido = Pedido.objects.all()
    contexto = {'pedido': pedido}
    return render(request, 'pedidos.html',contexto)


# CRUD Pedidos
def crear_Pedido(request):
    rut_cliente = request.POST.get('rut_cliente')
    nombre_cliente = request.POST.get('nombre_cliente')
    apellido_cliente = request.POST.get('apellido_cliente')
    informacion_pedido = request.POST.get('informacion_pedido')
    fecha_entrega = request.POST.get('fecha_entrega')
    direccion_entrega = request.POST.get('direccion_entrega')
    telefono_cliente = request.POST.get('telefono_cliente')
    email_cliente = request.POST.get('email_cliente')
    pedido = Pedido(rut_cliente=rut_cliente, nombre_cliente=nombre_cliente,apellido_cliente=apellido_cliente,
    informacion_pedido=informacion_pedido,fecha_entrega=fecha_entrega,direccion_entrega=direccion_entrega,
    telefono_cliente=telefono_cliente,email_cliente=email_cliente)
    pedido.save()
    return HttpResponse('<script>alert("Pedido registrado");'+
                        ' window.location.href="/";</script>')