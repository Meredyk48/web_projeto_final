from django.contrib import admin
from corretor.models import Imovel, StatusObra, Venda, RelatorioVenda


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'localizacao',
                    'preco', 'corretor', 'ativo')
    list_filter = ('tipo', 'ativo', 'corretor')
    search_fields = ('titulo', 'localizacao', 'corretor__user__username')


@admin.register(StatusObra)
class StatusObraAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'status', 'porcentagem', 'ultima_atualizacao')
    list_filter = ('status',)
    search_fields = ('imovel__titulo',)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'corretor',
                    'data_venda', 'valor_venda', 'status')
    list_filter = ('status', 'data_venda', 'corretor')
    search_fields = ('imovel__titulo', 'cliente__user__username',
                     'corretor__user__username')


@admin.register(RelatorioVenda)
class RelatorioVendaAdmin(admin.ModelAdmin):
    list_display = ('corretor', 'data_geracao', 'total_vendas', 'valor_total')
    list_filter = ('corretor', 'data_geracao')
    search_fields = ('corretor__user__username',)
