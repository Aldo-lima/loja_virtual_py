from django.urls import path
from .views import estoque_entrado_list, estoque_entrado_detalhes, estoque_Saida_list, estoque_entrada_add

urlpatterns = [
    path('', estoque_entrado_list, name='home_estoque'),
    path('saidas', estoque_Saida_list, name='estoque_saida_list'),
    path('ver_estoque/<int:pk>', estoque_entrado_detalhes, name='estoque_entrada_detalhes'),
    path('add', estoque_entrada_add, name='entrada_estoque'),


]

