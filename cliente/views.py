from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from corretor.models import Imovel, StatusObra
from cliente.models import InteresseImovel, Notificacao
from django.contrib.auth.decorators import login_required
from corretor.forms import AdicionarImovelInteresseForm

# Create your views here.


@login_required
def dashboardCliente(request):
    interesses = InteresseImovel.objects.filter(cliente=request.user.profile)
    notificacoes = Notificacao.objects.filter(
        cliente=request.user.profile).order_by('-data_envio')[:10]
    return render(request, 'pages/dashboard_cliente.html', {
        'interesses': interesses,
        'notificacoes': notificacoes
    })


@login_required
def detalhe_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    status_obra = getattr(imovel, 'status_obra', None)
    return render(request, 'pages/detalhe_imovel.html', {
        'imovel': imovel,
        'status_obra': status_obra
    })


@login_required
def registrar_interesse(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    interesse, created = InteresseImovel.objects.get_or_create(
        cliente=request.user.profile, imovel=imovel)
    if created:
        Notificacao.objects.create(
            cliente=request.user.profile,
            mensagem=f'Interesse registrado no imóvel: {imovel.titulo}'
        )
    return redirect('detalhe_imovel', imovel_id=imovel.id)


@login_required
def clientes_interessados(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    interesses = InteresseImovel.objects.filter(imovel=imovel)
    return render(request, 'pages/clientes_interessados.html', {
        'imovel': imovel,
        'interesses': interesses
    })


@login_required
def adicionar_imovel_interesse(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    if request.method == 'POST':
        form = AdicionarImovelInteresseForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            interesse, created = InteresseImovel.objects.get_or_create(
                cliente=cliente, imovel=imovel)
            if created:
                Notificacao.objects.create(
                    cliente=cliente,
                    mensagem=f'Imóvel adicionado à sua lista de interesse: {imovel.titulo}'
                )
            return redirect('detalhe_imovel', imovel_id=imovel.id)
    else:
        form = AdicionarImovelInteresseForm()
    return render(request, 'pages/adicionar_imovel_interesse.html', {
        'imovel': imovel,
        'form': form
    })
