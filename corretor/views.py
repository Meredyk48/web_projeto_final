from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from corretor.models import Imovel, StatusObra, Venda, RelatorioVenda
from contas.models import Profile
from corretor.forms import ImovelForm

# Create your views here.


@login_required
def dashboardCorretor(request):
    imoveis = Imovel.objects.filter(corretor=request.user.profile)
    clientes = Profile.objects.filter(role='CLIENTE')
    relatorios = RelatorioVenda.objects.filter(corretor=request.user.profile)
    return render(request, 'pages/dashboard_corretor.html', {
        'imoveis': imoveis,
        'clientes': clientes,
        'relatorios': relatorios
    })


@login_required
def cadastrar_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.corretor = request.user.profile
            imovel.save()
            return redirect('dashboard_corretor')
    else:
        form = ImovelForm()
    return render(request, 'pages/cadastrar_imovel.html', {'form': form})


@login_required
def editar_imovel(request, imovel_id):
    imovel = get_object_or_404(
        Imovel, id=imovel_id, corretor=request.user.profile)
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('dashboard_corretor')
    else:
        form = ImovelForm(instance=imovel)
    return render(request, 'pages/editar_imovel.html', {'form': form, 'imovel': imovel})


@login_required
def detalhe_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    status_obra = getattr(imovel, 'status_obra', None)
    return render(request, 'pages/detalhe_imovel.html', {
        'imovel': imovel,
        'status_obra': status_obra
    })


@login_required
def editar_status_obra(request, imovel_id):
    imovel = get_object_or_404(
        Imovel, id=imovel_id, corretor=request.user.profile)
    status_obra, created = StatusObra.objects.get_or_create(imovel=imovel)
    status_choices = StatusObra.STATUS_CHOICES
    if request.method == 'POST':
        status_obra.status = request.POST.get('status')
        status_obra.porcentagem = int(request.POST.get('porcentagem', 0))
        status_obra.cronograma = request.POST.get('cronograma', '')
        status_obra.save()
        return redirect('dashboard_corretor')
    return render(request, 'pages/editar_status_obra.html', {
        'imovel': imovel,
        'status_obra': status_obra,
        'status_choices': status_choices
    })
