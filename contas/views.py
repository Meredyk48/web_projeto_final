from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from contas.models import Profile
from corretor.models import Imovel, StatusObra, Venda, RelatorioVenda


def login(request):
    if request.user.is_authenticated:
        # Usuário já está logado, pode redirecionar conforme a role.
        role = request.user.profile.role
        if role == 'CLIENTE':
            return redirect('dashboard_cliente')
        elif role == 'CORRETOR':
            return redirect('dashboard_corretor')

    if request.method == "POST":
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        verificar_usuario = auth.authenticate(username=usuario, password=senha)

        if verificar_usuario is not None:
            auth.login(request, verificar_usuario)

            role = verificar_usuario.profile.role
            if role == 'CLIENTE':
                return redirect('dashboard_cliente')
            elif role == 'CORRETOR':
                return redirect('dashboard_corretor')
            else:
                return render(request, 'login.html', {'error_message': "Perfil sem role definida."})
        else:
            return render(request, 'login.html', {'error_message': "Usuário ou senha inválidos"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        role = request.user.profile.role
        if role == 'CLIENTE':
            return redirect('dashboard_cliente')
        elif role == 'CORRETOR':
            return redirect('dashboard_corretor')

    if request.method == "POST":
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('password_confirm')
        role = request.POST.get('role')

        if not usuario or not email or not senha or not confirmar_senha or not role:
            return render(request, 'register.html', {'error_message': "Todos os campos são obrigatórios."})

        if senha != confirmar_senha:
            return render(request, 'register.html', {'error_message': "As senhas não coincidem."})

        try:
            novo_usuario = User.objects.create_user(
                username=usuario, email=email, password=senha)

            profile = Profile.objects.get(user=novo_usuario)
            profile.role = role
            profile.save()

            return redirect('login')
        except Exception as e:
            return render(request, 'register.html', {'error_message': f"Erro ao registrar: {str(e)}"})
    else:
        return render(request, 'register.html')


@login_required
def dashboard_cliente(request):
    if request.user.profile.role != 'CLIENTE':
        return HttpResponseForbidden('Acesso restrito a clientes.')
    return render(request, 'pages/dashboard_cliente.html')


@login_required
def dashboard_corretor(request):
    if request.user.profile.role != 'CORRETOR':
        return HttpResponseForbidden('Acesso restrito a corretores.')
    return render(request, 'pages/dashboard_corretor.html')


@login_required
def perfil(request):
    profile = request.user.profile
    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        creci = request.POST.get('creci')
        endereco = request.POST.get('endereco')
        profile.telefone = telefone
        profile.data_nascimento = data_nascimento or None
        profile.creci = creci
        profile.endereco = endereco
        profile.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
    return render(request, 'pages/perfil.html', {'profile': profile})


@login_required
def editar_perfil(request):
    profile = request.user.profile
    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        creci = request.POST.get('creci')
        endereco = request.POST.get('endereco')
        profile.telefone = telefone
        profile.data_nascimento = data_nascimento or None
        profile.creci = creci
        profile.endereco = endereco
        profile.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('perfil')
    return render(request, 'pages/editar_perfil.html', {'profile': profile})
