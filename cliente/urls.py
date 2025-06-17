from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardCliente, name='dashboard_cliente'),
    path('detalhe-imovel/<int:imovel_id>/',
         views.detalhe_imovel, name='detalhe_imovel'),
    path('registrar-interesse/<int:imovel_id>/',
         views.registrar_interesse, name='registrar_interesse'),
    path('clientes-interessados/<int:imovel_id>/',
         views.clientes_interessados, name='clientes_interessados'),
    path('adicionar-imovel-interesse/<int:imovel_id>/',
         views.adicionar_imovel_interesse, name='adicionar_imovel_interesse'),
]
