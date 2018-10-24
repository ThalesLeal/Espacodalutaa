
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username','name', 'email','cep','logradouro','numero','complemento','telefone','bairro','cidade',
                 'nome_mae','nome_pai','data_nascimento']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Usuario
        # exclude = ['date_joined']
        fields = ['username', 'email', 'name','is_active', 'is_staff']
