from django import forms
from .models import Imovel
from contas.models import Profile


class ImovelForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=Imovel.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Situação do Imóvel',
        required=True
    )

    class Meta:
        model = Imovel
        fields = ['titulo', 'descricao', 'tipo', 'status', 'localizacao', 'preco', 'quartos',
                  'banheiros', 'vagas', 'area', 'condicoes_pagamento', 'foto', 'ativo']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quartos': forms.NumberInput(attrs={'class': 'form-control'}),
            'banheiros': forms.NumberInput(attrs={'class': 'form-control'}),
            'vagas': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'condicoes_pagamento': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AdicionarImovelInteresseForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Profile.objects.filter(role='CLIENTE'),
        label='Selecione o cliente',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
