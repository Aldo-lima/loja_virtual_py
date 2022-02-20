from django.contrib import admin
from django.urls import path
from .views import produtos, novoProduto, produtoEditar, produtoVer, produtoDetete

urlpatterns = [
    path('/produto', produtos, name='listar_produto'),
    path('/novo_produto', novoProduto, name='produto_create'),
    path('ver_produto/<int:id>', produtoVer, name='produto_ver'),
    path('editar_produto/<int:id>',produtoEditar , name='produto_edite'),
    path('delete_Produto/<int:id>', produtoDetete, name='produto_delete'),

]