from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardCorretor, name='dashboard'),
]