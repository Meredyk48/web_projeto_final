from django.db import models
from django.contrib.auth.models import User


class Imovel(models.Model):
    TIPO_CHOICES = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('CO', 'Cobertura'),
        ('TE', 'Terreno'),

    ]
    STATUS_CHOICES = [
        ('ESTRUTURACAO', 'Estruturação'),
        ('ACABAMENTO', 'Acabamento'),
        ('FINALIZADO', 'Finalizado'),
    ]
    corretor = models.ForeignKey(
        'contas.Profile', on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'CORRETOR'})
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='ESTRUTURACAO')
    localizacao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    quartos = models.PositiveIntegerField()
    banheiros = models.PositiveIntegerField()
    vagas = models.PositiveIntegerField(default=0)
    area = models.DecimalField(
        max_digits=8, decimal_places=2, help_text='Área em m²')
    condicoes_pagamento = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='imoveis/', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class StatusObra(models.Model):
    imovel = models.OneToOneField(
        Imovel, on_delete=models.CASCADE, related_name='status_obra')
    FUNDACAO = 'FUNDACAO'
    ESTRUTURA = 'ESTRUTURA'
    ACABAMENTO = 'ACABAMENTO'
    ENTREGUE = 'ENTREGUE'
    STATUS_CHOICES = [
        (FUNDACAO, 'Fundação'),
        (ESTRUTURA, 'Estrutura'),
        (ACABAMENTO, 'Acabamento'),
        (ENTREGUE, 'Entregue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    porcentagem = models.PositiveIntegerField(default=0)
    cronograma = models.TextField(
        help_text='Linha do tempo e previsão de entrega')
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.imovel.titulo} - {self.get_status_display()} ({self.porcentagem}%)"


class Venda(models.Model):
    imovel = models.ForeignKey('corretor.Imovel', on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        'contas.Profile', on_delete=models.CASCADE, limit_choices_to={'role': 'CLIENTE'}, related_name='compras')
    corretor = models.ForeignKey(
        'contas.Profile', on_delete=models.SET_NULL,
        null=True, blank=True, limit_choices_to={'role': 'CORRETOR'}, related_name='vendas')
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_venda = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=30, default='Em andamento')

    def __str__(self):
        return f"Venda de {self.imovel.titulo} para {self.cliente.user.username}"


class RelatorioVenda(models.Model):
    corretor = models.ForeignKey(
        'contas.Profile', on_delete=models.CASCADE, limit_choices_to={'role': 'CORRETOR'})
    data_geracao = models.DateTimeField(auto_now_add=True)
    total_vendas = models.PositiveIntegerField(default=0)
    valor_total = models.DecimalField(
        max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return f"Relatório de {self.corretor.user.username} em {self.data_geracao.strftime('%d/%m/%Y')}"
