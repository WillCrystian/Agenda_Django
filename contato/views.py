from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from.models import Contato

def index(request):
    lista_contatos = Contato.objects.order_by('-id').filter(mostrar= True)
    
    paginator = Paginator(lista_contatos, 3)
    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'index.html', {'contatos': contatos})

def detalhes(request, contato_id):
    # Se contato não existe 
    contato = get_object_or_404(Contato, id= contato_id)
    
    if not contato.mostrar:
        raise Http404()
    
    return render(request, 'detalhes.html', {'contato': contato})
    