from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ('CLIENTE', 'Cliente'),
        ('CORRETOR', 'Corretor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    # Campos extras para corretor
    creci = models.CharField(max_length=30, blank=True, null=True,
                             help_text='Número do registro CRECI (apenas para corretores)')
    # Campos extras para cliente
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
