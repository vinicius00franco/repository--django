# linkando a url do meu app com meu projeto
from django.contrib import admin
from django.urls import path
# para linkar a rota do nosso projeto para a view do nosso app
from . import views

urlpatterns = [
    #path ( localhosts , nome do arquivo a ser exibido....)
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
]