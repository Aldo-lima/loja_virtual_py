from django.db import models


class Categoria(models.Model):
       nome_categoria = models.CharField('Categoria', max_length=100)

       def __str__(self):
           return self.nome_categoria



TIPO_TELEFONE = (
     ('pessoal', 'Pessoal'),
     ('comercial', 'Comercial'),
   )

TIPO_EMAIL = (
     ('pessoal', 'Pessoal'),
     ('comercial', 'Comercial'),
    )

class Fornecedor(models.Model):
    data_cadastro = models.DateTimeField(auto_now=True)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField('Nome Fantasia', max_length=100)
    nome_r = models.CharField('Nome Razão Social', max_length=100)
    CNPJ = models.CharField('cnpj', max_length=100)
    escricao_estadual = models.CharField('Escrição Estadual', max_length=100)
    rua = models.CharField('Rua', max_length=200)
    cep = models.CharField('CEP', max_length=10)
    numero = models.IntegerField('Numéro:')
    cidade = models.CharField('Cidade', max_length=50)
    bairro = models.CharField('Bairro', max_length=30)
    proximidade = models.CharField(max_length=30)
    complemento = models.CharField('Complemento', max_length=10)
    nome_contato = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=10)
    telefone = models.CharField('Telefone', max_length=15)
    tipo_telefone = models.CharField(max_length=11, choices=TIPO_TELEFONE)
    Email = models.CharField('E-mail', max_length=100)
    tipo_email = models.CharField(max_length=11, choices=TIPO_EMAIL)

    def __str__(self):
        return self.nome