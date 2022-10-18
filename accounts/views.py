from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        # Verificando se usuario está logado
        if request.user.username:
            return redirect('index')
            
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        # verificando se existe o usuário e a senha para fazer login
        user = auth.authenticate(request, username= usuario, password= senha )
        if not user:            
            messages.error(request, 'Usuario ou senha invádo')
            return render(request, 'login.html')
        else:
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso')
            return redirect('index')
        
    elif request.method == 'GET':
        # Verificando se usuario está logado
        if request.user.username:
            return redirect('index')
        
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login') 


def cadastro(request):
    if request.method == 'POST':
        # Verificando se usuario está logado
        if request.user.username:
            return redirect('index')
        
        nome = request.POST.get('nome').strip()
        sobrenome = request.POST.get('sobrenome').strip()
        email = request.POST.get('email').strip()
        usuario = request.POST.get('usuario').strip()
        senha = request.POST.get('senha').strip()
        senha2 = request.POST.get('senha2').strip()
        
        # Verificando se os campos estão vazios
        if nome == '' or sobrenome == '' or email == '' or \
            usuario == '' or senha == '' or senha2 == '':
            messages.add_message(request, messages.ERROR, 'Algum dos campos não foi preenchido.')
            return render(request, 'cadastro.html')
        
        # Validado email
        try:
            validate_email(email)
        except Exception:
            messages.add_message(request, messages.ERROR, 'Email inválido.')
            return render(request, 'cadastro.html')        
        
        # Verificando se as senhas estão iguais
        if senha != senha2:
            messages.add_message(request, messages.ERROR, 'Senha não são iguais.')
            return render(request, 'cadastro.html')
            
        # verificando tamanho da senha
        if len(senha) < 6 or len(senha) > 10:
            messages.add_message(request, messages.ERROR, 'Sua senha dete ter de 6 a 10 caracteres.')
            return render(request, 'cadastro.html')
            
        # Verificando o tamanho do usuário
        if len(usuario) < 6 or len(usuario) > 10:
            messages.add_message(request, messages.ERROR, 'Seu usuário dete ter de 6 a 10 caracteres.')
            return render(request, 'cadastro.html')
        
        # Verificando se usuário exite
        if User.objects.filter(username= usuario).exists():
            messages.add_message(request, messages.ERROR, 'Usuário já existe.')
            return render(request, 'cadastro.html')
        
        # #verificando se e-mail existe
        if User.objects.filter(email= email).exists():
            messages.add_message(request, messages.ERROR, 'Email já existe.')
            return render(request, 'cadastro.html')  
       
        # Cadastrando no banco de dados
        user = User.objects.create_user(first_name= nome,
                                   last_name= sobrenome,
                                   username= usuario,
                                   email= email,
                                   password= senha)
        user.save()
        
        messages.add_message(request, messages.SUCCESS, 'Cadastro realizado com sucesso. Agora faça login')
        return redirect('login')
    
    elif request.method == 'GET':
        # Verificando se usuario está logado
        if request.user.username:
            return redirect('index')
        return render(request, 'cadastro.html')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'dashboard.html')
