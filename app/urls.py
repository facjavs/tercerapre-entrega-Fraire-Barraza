from django.urls import path, include
from .views import *                #Para importar todo de views en la misma carpeta

urlpatterns = [
    path('',inicio, name='inicio'),
    path('registrate/',registrate, name='registrate'),
    path('vender/', vender, name='vender'),
    path('comprar/',comprar, name='comprar'),
    path('catalogo/',catalogo, name='catalogo'),
    path('piezaform/',PiezaForm, name='piezaform'),
    path('compradorform/',ComprarForm, name='compradorform'),
    path('vendedorform/',VenderForm, name='vendedorform'),
    path('buscarPieza/', buscarPieza, name='buscarPieza'),
    path('buscar2/', buscar2, name='buscar2'),

    ]