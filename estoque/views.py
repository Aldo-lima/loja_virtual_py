from django.shortcuts import render
from .models import  Estoque, EstoqueItens
from django.http import JsonResponse
import json
from django.http import HttpResponse




def estoque_entrado_list(request):
    template_name = 'estoque/estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)



def estoque_entrado_detalhes(request, pk):
    template_name = 'estoque/estoque_entrada_detalhes.html'
    objects = Estoque.objects.get(pk=pk)
    context = {'objects': objects}
    return render(request, template_name, context)


def estoque_saida_list(request):
    template_name = 'estoque/estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='s')
    context = {'object_list': objects}
    return render(request, template_name, context)


# Create your views here.
