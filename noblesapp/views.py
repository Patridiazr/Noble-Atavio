from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedido, Producto

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    return render(request, 'index.html')

def catalogo(request):
    producto = Producto.objects.all()
    contexto = {'producto': producto}
    return render(request, 'catalogo.html',contexto)

def pedidos(request):
    pedido = Pedido.objects.all()
    contexto = {'pedido': pedido}
    return render(request, 'pedidos.html',contexto)

def admin(request):
    producto = Producto.objects.all()
    contexto = {'producto': producto}
    return render(request,'admin.html',contexto)

def detalle_producto(request,pk):
    pk = Producto.objects.get(pk=pk)
    return render(request, 'detalle_producto.html',{'pk':pk})

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

def crear_Producto(request):
    nombre_producto = request.POST.get('nombre_producto')
    precio_oferta = request.POST.get('precio_oferta')
    precio_real = request.POST.get('precio_real')
    producto = Producto(nombre_producto=nombre_producto, precio_oferta=precio_oferta, precio_real=precio_real)
    producto.save()
    return HttpResponse('<script>alert("Producto registrado");'+
                        ' window.location.href="/";</script>')