from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,UpdateView,FormView,ListView
from django.core.urlresolvers import reverse_lazy
from .models import Usuario
from checkout.models import Order
from .forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm



class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'


class RegisterView(CreateView):

    model = Usuario
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = Usuario
    template_name = 'accounts/update_user.html'
    # fields = ['name', 'email']
    fields = ['username','name', 'email','cep','logradouro','numero','complemento',
             'telefone','bairro','cidade','nome_mae','nome_pai','data_nascimento']

    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):

    template_name = 'accounts/area_do_aluno.html'
    success_url = reverse_lazy('accounts:index')
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('pk')


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
order_list_aluno = OrderListView.as_view()
