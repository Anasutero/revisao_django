from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse
from .models import Pessoas
from django.core.exceptions import ObjectDoesNotExist

# def abre_index(request):
#     return render(request, 'index.html')

def listagem(request):
    mensagem = ''
    nome = ''
    idade = ''
    dados = Pessoas.objects.all()
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
    return render(request, 'index.html' ,{'mensagem': mensagem, 'nome':nome,'idade':idade,'dados':dados})


def editar_cadastro(request,id):
    if request.method=='POST':
        try:
            pessoa = Pessoas.objects.get(pk=id)
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')


            pessoa.nome=nome
            pessoa.idade=idade
            pessoa.save()

            return HttpResponseRedirect(reverse('listagem'))
        
        except ObjectDoesNotExist:
            pass

    pessoa= Pessoas.objects.get(id=id)

    return render(request, 'editar.html', {'nome': pessoa.nome, 'idade': pessoa.idade, 'id': pessoa.id})
    
def excluir_pessoa(request,id):
    try:
        with transaction.atomic():
            pessoa = Pessoas.objects.get(id=id)
            pessoa.delete()

            return HttpResponseRedirect(reverse('listagem'))
    except Pessoas.DoesNotExist:
        pass

 


        



    