from django.shortcuts import render
from .models import Receita

def index(resquest):
    receitas = Receita.objects.all
    dados = {
        'nome_das_receitas': receitas
    }
    return render(resquest, 'index.html',context=dados  )

def receita(request):
    #renderiza recebendo a requisição e e página
    return render(request, 'receita.html')
