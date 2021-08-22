from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin
from rest_framework import routers

# Rutas para paginas
urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear_Pedido',views.crear_Pedido, name='crear_Pedido'),



    # CRUD PEDIDOS
    path('crear_Pedido',views.crear_Pedido, name='crear_Pedido'),
]