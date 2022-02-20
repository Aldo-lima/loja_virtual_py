from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto',
                  'fornecedor',
                  'descricao',
                  'unidade_medida',
                  'quantidade_embalagem',
                  'preco',
                 ]

