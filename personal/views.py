from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from personal.models import Produtos, Carrosel

def Home(request):
    lista_produtos = Produtos.objects.all()
    lista_imagens = Carrosel.objects.all()

    return render(request, "personal/home.html", {
        'lista_produtos': lista_produtos,
        'lista_imagens': lista_imagens,
        })

    