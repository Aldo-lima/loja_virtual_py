from django.shortcuts import render, resolve_url, redirect
from .models import  Estoque, EstoqueItens
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

           return redirect('home_estoque')
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
        context ={'form': form, 'formset':formset}
    return render(request, template_name, context )
