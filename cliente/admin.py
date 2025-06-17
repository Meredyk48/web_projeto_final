from django.contrib import admin
from .models import Notificacao, InteresseImovel, AnuncioImovelCliente


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'mensagem', 'data_envio', 'lida')
    list_filter = ('lida', 'data_envio')
    search_fields = ('cliente__user__username', 'mensagem')


@admin.register(InteresseImovel)
class InteresseImovelAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'imovel', 'data_interesse', 'receber_novos')
    list_filter = ('receber_novos',)
    search_fields = ('cliente__user__username', 'imovel__titulo')


@admin.register(AnuncioImovelCliente)
class AnuncioImovelClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'titulo', 'localizacao',
                    'preco', 'data_anuncio', 'ativo')
    list_filter = ('ativo', 'data_anuncio')
    search_fields = ('cliente__user__username', 'titulo', 'localizacao')
