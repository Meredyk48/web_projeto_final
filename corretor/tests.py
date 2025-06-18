from django.test import TestCase
from django.contrib.auth import get_user_model
from contas.models import Profile
from .models import Imovel


class ImovelModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='corretor', password='123456')
        self.profile = Profile.objects.get(user=self.user)
        self.profile.role = 'CORRETOR'
        self.profile.save()

    def test_criar_imovel_com_status(self):
        imovel = Imovel.objects.create(
            corretor=self.profile,
            titulo='Apartamento Teste',
            descricao='Descrição teste',
            tipo='AP',
            status='ACABAMENTO',
            localizacao='Rua Teste, 123',
            preco=500000,
            quartos=2,
            banheiros=2,
            vagas=1,
            area=80,
            condicoes_pagamento='À vista',
            ativo=True
        )
        self.assertEqual(imovel.status, 'ACABAMENTO')
        self.assertEqual(imovel.get_status_display(), 'Acabamento')

    def test_status_default(self):
        imovel = Imovel.objects.create(
            corretor=self.profile,
            titulo='Casa Default',
            descricao='Desc',
            tipo='CA',
            localizacao='Rua X',
            preco=300000,
            quartos=3,
            banheiros=2,
            vagas=2,
            area=120,
            condicoes_pagamento='Parcelado',
            ativo=True
        )
        self.assertEqual(imovel.status, 'ESTRUTURACAO')
        self.assertEqual(imovel.get_status_display(), 'Estruturação')
