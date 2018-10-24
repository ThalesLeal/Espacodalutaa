# coding=utf-8

from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from accounts.models import Usuario


class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_register_ok(self):
        data = {
            'username': 'thales', 'password1': 'teste123', 'password2': 'teste123',
            'email': 'test@test.com','cep': '58010780', 'logradouro': 'teste',
            'numero': '280', 'complemento': 'Casa', 'telefone': '83986602823',
            'bairro': 'Centro', 'cidade': 'João Pessoa', 'nome_mae': 'Maria teste',
            'nome_pai':'teste', 'data_nascimento': '22/06/1990','name': 'teste'
        }
        response = self.client.post(self.register_url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(Usuario.objects.count(), 1)

    def test_register_error(self):
        data = {'username': 'thales', 'password1': 'teste123', 'password2': 'teste123'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
