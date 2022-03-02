from django.contrib.auth.models import User
from django.db import models
from produto.models import Produto
from core.models import TimeStampeModel
from django.urls import reverse_lazy
# Create your models here.

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampeModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estoques')
    nf = models.PositiveIntegerField('nota fiscal', null=True,blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
         ordering = ('-created',)

    def __str__(self):
        return str('{}.-.{}.-.{}'.format(self.pk, self.nf, self.created.strftime('%d-%m-Y')))

    def get_absolite_url(self):
       return reverse_lazy('estoque:estoque/estoque_entrada_detalhes', kwargs={'pk': self.pk})


    def nf_formated(self):
        return str(self.nf).zfill(3)


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField('Saldo', null=True, blank=True)
    valor_da_entrada = models.DecimalField('Valor_da_entrada', max_digits=7, decimal_places=2)


    class Meta:
         ordering = ('pk',)
    def __str__(self):
        return '{}.-.{}.-.{}.-.'.format(self.pk, self.estoque.pk, self.produto)