from django.shortcuts import render, resolve_url, redirect
from .models import  Estoque, EstoqueItens
from produto.models import Produto
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from .forms import EstoqueForm, EstoqueItensForm




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

def dar_entrada_estoque(form):

    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        quantidade = int(item.quantidade)
        produto.estoque = produto.estoque + quantidade
        produto.save()
    print ('Estoque atualizado com sucesso.')

def dar_baixa_estoque(form):

    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        quantidade = int(item.quantidade)
        produto.estoque = produto.estoque - quantidade
        produto.save()
    print ('Estoque atualizado com sucesso.')


def estoque_saida_list(request):
    template_name = 'estoque/estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='s')
    context = {'object_list': objects}
    return render(request, template_name, context)


def estoque_entrada_add(request):
    template_name = 'estoque/estoque_entrada_for.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST,instance=estoque_form, prefix='estoque'
        )
        if form.is_valid() and formset.is_valid():
           form = form.save()
           formset.save()
           if form.movimento == 's':
                dar_baixa_estoque(form)
                return redirect('home_estoque')
           else:
               dar_entrada_estoque(form)
               return redirect('home_estoque')
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
        context ={'form': form, 'formset': formset}
    return render(request, template_name, context)
