from django.shortcuts import render, redirect
from .models import Categoria, Fornecedor
from  .forms import CotegoriaForm, ForncedorForm
from django.core.paginator import Paginator

#===============================Categoria====================================

#lista categoria
def categorias(request):
    categoria_list = Categoria.objects.all()
    paginator = Paginator(categoria_list, 5)
    page = request.GET.get('page')
    categorias = paginator.get_page(page)
    form = CotegoriaForm
    context = {
        'categorias': categorias,
        'form': form
    }
    return render(request, 'categoria/lista_categoria.html', context)

def novaCategoria(request):
    if request.method == "POST":
        form = CotegoriaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home_categorias')
    else:
        context = {
            'form': form,
        }
        return render(request, 'categoria/lista_categoria.html', context)

#===========================================Fornecedor
def fornecedores(request):
    search = request.GET.get('search')
    if search:
        fornecedores = Fornecedor.objects.filter(nome__icontains=search)
    else:

        fornecedor_list = Fornecedor.objects.all()
        paginator = Paginator(fornecedor_list, 5)
        page = request.GET.get('page')
        fornecedores = paginator.get_page(page)
    return render(request, 'fornecedor/list_fornecedor.html', {'fornecedores': fornecedores})


def novoFornecedor(request):
    form = ForncedorForm()
    if request.method == "POST":
        form = ForncedorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_fornecedor')
    else:
        context = {
            'form': form,
        }
        return render(request, 'fornecedor/create_fornecedor.html', context)


def fornecedorVer(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    return render(request, 'fornecedor/detalhes_fornecedor.html', {'fornecedor':fornecedor})

def fornecedorEditar(request, id):
    if request.method == "GET":
        objeto = Fornecedor.objects.filter(id=id).first()
        if objeto is None:
            return redirect('listar_fornecedor')
        form = ForncedorForm(instance=objeto)
        context = {
           'form': form,
        }
        return render(request, 'fornecedor/edite_fornecedor.html', context)
    elif request.method == "POST":
        objeto = Fornecedor.objects.filter(id=id).first()
        if objeto is None:
            return redirect(reverse('listar_fornecedor'))
        form = ForncedorForm(request.POST, instance=objeto)
        if form.is_valid():
             form.save()
             return redirect('listar_fornecedor')
        else:
           context = {
             'form': form,

           }
           return render(request, 'fornecedor/create_fornecedor.html', context)


def fornecedorDetete(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == "POST":
        fornecedor.delete()
        return redirect('listar_fornecedor')
    else:
        return render(request, 'fornecedor/delete_confirme.html', {'fornecedor': fornecedor})
