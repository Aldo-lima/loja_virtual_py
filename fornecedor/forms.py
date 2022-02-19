from django import forms
from .models import Fornecedor, Categoria

class CotegoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ForncedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

    #def __init__(self, *args, **kwargs):
    #  super().__init__(self, *args, **kwargs)
    #   self.fields['CNPJ'].widget.attrs.update({'class': 'CNPJ'})
     #  self.fields['cep'].widget.attrs.update({'class': 'cep'})
