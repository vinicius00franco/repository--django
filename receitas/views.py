from django.shortcuts import render


def index(resquest):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete',
        4: 'Bolo de chocolate'
    }
    dados = {
        'nome_das_receitas': receitas
    }
    return render(resquest, 'index.html',context=dados  )


def receita(request):
    #renderiza recebendo a requisição e e página
    return render(request, 'receita.html')
