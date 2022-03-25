from django.shortcuts import render
from .models import Produto, Cliente


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'contato.html', context)


def produto(request, pk):
    #  print(f'PK: {pk}')
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
