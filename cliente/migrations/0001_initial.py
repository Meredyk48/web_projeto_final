# Generated by Django 5.2.1 on 2025-06-16 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contas', '0002_profile_creci_profile_data_nascimento_and_more'),
        ('corretor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnuncioImovelCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('localizacao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='anuncios_clientes/')),
                ('data_anuncio', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(limit_choices_to={'role': 'CLIENTE'}, on_delete=django.db.models.deletion.CASCADE, to='contas.profile')),
            ],
        ),
        migrations.CreateModel(
            name='InteresseImovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_interesse', models.DateTimeField(auto_now_add=True)),
                ('receber_novos', models.BooleanField(default=True, help_text='Receber notificações de novos imóveis semelhantes')),
                ('cliente', models.ForeignKey(limit_choices_to={'role': 'CLIENTE'}, on_delete=django.db.models.deletion.CASCADE, to='contas.profile')),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corretor.imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=255)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('lida', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(limit_choices_to={'role': 'CLIENTE'}, on_delete=django.db.models.deletion.CASCADE, to='contas.profile')),
            ],
        ),
    ]
