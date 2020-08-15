from django.urls import path
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
 # GET /
 path('', views.Index.as_view(), name='index'),
 path('funcionario-list/', views.FuncionarioList.as_view(), name='funcionario-list'),
 path('funcionario-update/<pk>', views.FuncionarioUpdate.as_view(), name='funcionario-update'),
 path('funcionario-add', views.FuncionarioCreate.as_view(), name = 'funcionario-add'),
 path('funcionario-delete/<pk>', views.FuncionarioDelete.as_view(), name = 'funcionario-delete'),

]
