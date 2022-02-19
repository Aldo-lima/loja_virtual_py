from django.urls import path
from .views import categorias, novaCategoria

urlpatterns = [
    path('categoria', categorias, name='home_categorias'),
    path('nova_categoria', novaCategoria, name='nova_categoria'),
]