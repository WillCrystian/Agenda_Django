from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from.models import Contato
from django.db.models import Q, Value
from django.db.models.functions import Concat

def index(request):
    lista_contatos = Contato.objects.order_by('-id').filter(mostrar= True)
    
    paginator = Paginator(lista_contatos, 2)
    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'index.html', {'contatos': contatos})

def detalhes(request, contato_id):
    # Se contato não existe 
    contato = get_object_or_404(Contato, id= contato_id)
    
    if not contato.mostrar:
        raise Http404()
    
    return render(request, 'detalhes.html', {'contato': contato})

def busca(request):
    termo = request.GET.get('termo')
    if termo is None:
        raise Http404()
    
    campos = Concat('nome', Value(' '), 'sobrenome')
    
    lista_contatos = Contato.objects.annotate(
        nome_completo= campos
    ).filter(
        Q(nome_completo__icontains= termo) | Q(telefone__icontains= termo)
        )  
    
    paginator = Paginator(lista_contatos, 2)
    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'busca.html', {'contatos': contatos})
    