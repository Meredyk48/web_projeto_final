from django.db import models
from django.contrib.auth.models import User


class Notificacao(models.Model):
    cliente = models.ForeignKey(
        'contas.Profile', on_delete=models.CASCADE, limit_choices_to={'role': 'CLIENTE'})
    mensagem = models.CharField(max_length=255)
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificação para {self.cliente.user.username}: {self.mensagem[:30]}"


class InteresseImovel(models.Model):
    cliente = models.ForeignKey(
        'contas.Profile', on_delete=models.CASCADE, limit_choices_to={'role': 'CLIENTE'})
    imovel = models.ForeignKey('corretor.Imovel', on_delete=models.CASCADE)
    data_interesse = models.DateTimeField(auto_now_add=True)
    receber_novos = models.BooleanField(
        default=True, help_text='Receber notificações de novos imóveis semelhantes')

    def __str__(self):
        return f"{self.cliente.user.username} interessado em {self.imovel.titulo}"


class AnuncioImovelCliente(models.Model):
    cliente = models.ForeignKey(
        'contas.Profile', on_delete=models.CASCADE, limit_choices_to={'role': 'CLIENTE'})
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    foto = models.ImageField(
        upload_to='anuncios_clientes/', blank=True, null=True)
    data_anuncio = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Anúncio de {self.cliente.user.username}: {self.titulo}"
