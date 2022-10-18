from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from.models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):
    lista_contatos = Contato.objects.order_by('-id').filter(mostrar= True)
    
    paginator = Paginator(lista_contatos, 2)
    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'index.html', {'contatos': contatos})

@login_required(redirect_field_name='login')
def detalhes(request, contato_id):
    # Se contato não existe 
    contato = get_object_or_404(Contato, id= contato_id)
    
    if not contato.mostrar:
        messages.add_message(request, messages.ERROR, 'Este contato está oculto.')
        return redirect('index')       
    
    return render(request, 'detalhes.html', {'contato': contato})

@login_required(redirect_field_name='login')
def busca(request):
    # buscando na url o resultado do termo
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Por favor digite sua pesquisa.')
        return redirect('index')
    
    # Concatenando o nome e sobrenome do banco de dados
    campos = Concat('nome', Value(' '), 'sobrenome')
    
    # fazendo um campo temporário nome_completo
    lista_contatos = Contato.objects.annotate(nome_completo= campos).filter(
        # procurando por nome completo ou telefone
        Q(nome_completo__icontains= termo) | Q(telefone__icontains= termo)
        )  
    
    # Listando contatos e quantidades
    paginator = Paginator(lista_contatos, 2)
    # Buscando na url o resultado de 'p'
    paginas = request.GET.get('p')
    
    contatos = paginator.get_page(paginas)
    
    return render(request, 'busca.html', {'contatos': contatos})

@login_required(redirect_field_name='index')
def excluir(request, contato_id):    
    Contato.objects.get(id= contato_id).delete()
   
    return redirect('index')
    
    