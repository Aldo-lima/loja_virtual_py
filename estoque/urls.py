from django.urls import path
from .views import estoque_entrado_list, estoque_entrado_detalhes

urlpatterns = [
    path('', estoque_entrado_list, name='home_estoque'),
    path('ver_estoque/<int:pk>', estoque_entrado_detalhes, name='estoque_entrada_detalhes'),

]

