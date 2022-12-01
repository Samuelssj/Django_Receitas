from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse('<h1> receitas</h1')
    receitas = {
        1: 'sorvete',
        2: 'hamburger',
        3: 'batata frita',
        4: 'suco verde',
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)


def receita(request):

    return render(request, 'receita.html')
