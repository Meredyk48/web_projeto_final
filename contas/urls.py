from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard_cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('dashboard_corretor/', views.dashboard_corretor,
         name='dashboard_corretor'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]
