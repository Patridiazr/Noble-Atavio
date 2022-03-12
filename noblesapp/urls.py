from django.urls import path,include
# from django.conf.urls import url
from . import views
from django.contrib import admin
# from rest_framework import routers

# Rutas para paginas
urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('administrador/',views.admin, name='admin'),
    path('detalle_producto/',views.detalle_producto, name='detalle_producto'),
    path('detalle_producto/<int:pk>',views.detalle_producto, name='detalle_producto'),
    path('pedidos/crear_Pedido',views.crear_Pedido, name='crear_Pedido'),
    path('administrador/crear_Producto',views.crear_Producto, name='crear_Producto'),

    # CRUD PEDIDOS
    path('crear_Pedido',views.crear_Pedido, name='crear_Pedido'),
    path('crear_Producto', views.crear_Producto, name='crear_Producto'),

    ]