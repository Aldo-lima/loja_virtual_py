from django.shortcuts import render, redirect
from .models import Categoria
from  .forms import CotegoriaForm
from django.core.paginator import Paginator

# Create your views here.
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