from django.shortcuts import render
from django.contrib import messages

def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
    

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        
        return render(request, 'cadastro.html')
    
    elif request.method == 'GET':
        return render(request, 'cadastro.html')



def dashboard(request):
    return render(request, 'dashboard.html')
