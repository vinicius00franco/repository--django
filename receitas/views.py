from django.shortcuts import render
from .models import Receita

def index(resquest):
    receitas = Receita.objects.all()
    dados = {
        'nome_da_receita': receitas
    }
    return render(resquest, 'index.html',dados  )

def receita(request):
    #renderiza recebendo a requisição e e página
    return render(request, 'receita.html')
