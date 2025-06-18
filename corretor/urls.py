from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardCorretor, name='dashboard_corretor'),
    path('cadastrar-imovel/', views.cadastrar_imovel, name='cadastrar_imovel'),
    path('editar-imovel/<int:imovel_id>/',
         views.editar_imovel, name='editar_imovel'),
    path('detalhe-imovel/<int:imovel_id>/',
         views.detalhe_imovel, name='detalhe_imovel'),
    path('editar-status-obra/<int:imovel_id>/',
         views.editar_status_obra, name='editar_status_obra'),
]
