from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from helloworld.models import Funcionario

class Index(TemplateView):
    template_name = 'website/index.html'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'website/funcionario_list.html'

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'website/funcionario_update.html'
    success_url = ('../funcionario-list/')
    fields = ['name', 'lastName', 'cpf', 'serviceTime', 'salary']

class FuncionarioCreate(CreateView):
    model = Funcionario
    template_name = 'website/funcionario_add.html'
    success_url = ('../funcionario-list/')
    fields = ['name', 'lastName', 'cpf', 'serviceTime', 'salary']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'website/funcionario_delete.html'
    success_url = ('../funcionario-list')

    