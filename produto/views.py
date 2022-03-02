from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Produto
from django.core.paginator import Paginator
from .forms import ProdutoForm


def produtos(request):
    search = request.GET.get('search')
    if search:
        produtos = Produto.objects.filter(produto__icontains=search)
    else:
        produto_list = Produto.objects.all()
        paginator = Paginator(produto_list, 5)
        page = request.GET.get('page')
        produtos = paginator.get_page(page)
    return render(request, 'produto/list_produto.html', {'produtos': produtos})


def novoProduto(request):
    if request.method == "GET":
           form = ProdutoForm
           context = {
           'form': form
            }
           return render(request, 'produto/create_produto.html', context)
    elif request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('listar_produto')
        else:
            context = {
                'form': form,
            }
            return render(request, 'produto/create_produto.html', context)


def produtoEditar(request, id):
    if request.method == "GET":
        objeto = Produto.objects.filter(id=id).first()
        if objeto is None:
            return redirect('listar_produto')
        form = ProdutoForm(instance=objeto)
        context = {
           'form': form,
        }
        return render(request, 'produto/edite_produto.html', context)
    elif request.method == "POST":
        objeto = Produto.objects.filter(id=id).first()
        if objeto is None:
            return redirect(reverse('listar_produto'))
        form = ProdutoForm(request.POST, instance=objeto)
        if form.is_valid():
           form.save()
           return redirect('listar_produto')
        else:
            context = {
             'form': form,
            }
            return render(request, 'produto/create_produto.html', context)

def produtoVer(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'produto/detalhes_produto.html', {'produto': produto})


def produtoDetete(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produto')
    else:
        return render(request, 'produto/delete_confirme.html', {'produto': produto})


