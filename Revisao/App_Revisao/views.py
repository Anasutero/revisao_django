from django.shortcuts import render
from .models import Pessoas

# Create your views here.

def abre_index(request):
    return render(request, 'index.html')

def listagem(request):
    if(request.method == 'POST'):
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        gravaCadastro = Pessoas(
            nome=nome,
            idade=idade
        )
        gravaCadastro.save()

        dados = Pessoas.objects.all()

        mensagem=(f"Dados do formulario {nome} {idade}")

        return render(request, 'index.html' ,{'mensagem': mensagem,'nome':nome,'idade':idade,'dados':dados})