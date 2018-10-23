
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Usuario

class UsuarioForm(forms.Form):

    class Meta:
        model = Usuario
        exclude = ['is_staff', 'is_active', 'date_joined']
