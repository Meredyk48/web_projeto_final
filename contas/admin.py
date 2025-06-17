from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'telefone',
                    'data_nascimento', 'creci', 'endereco')
    search_fields = ('user__username', 'user__email', 'role', 'creci')
    list_filter = ('role',)
