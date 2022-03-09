from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib import auth
from django.contrib.messages import constants

from decouple import config

import pyrebase


config={
    "apiKey": config('apiKey'),
    "authDomain": config('authDomain'),
    "databaseURL": config('databaseURL'),
    "projectId": config('projectId'),
    "storageBucket": config('storageBucket'),
    "messagingSenderId": config('messagingSenderId'),
    "appId": config('appId'),
    #measurementId: config('measurementId') # não precisa deste
}
# Inicializando banco de dados, autenticação e firebase para uso posterior
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def login(request):
    if request.method == 'GET':
        # Se o ususario já estiver logado, será direcionado para pagina principal
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'index.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        # existe um usuario e senha igual o que foi digitado?
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto!')
            return redirect('/registation/login/')
        else:
            auth.login(request, usuario) #logar e ser redirecionado para a raiz do sistema
            return redirect('/')

def logout_request(request):
    logout(request)
    return redirect("home")


def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")

def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # se não houver erro, conecte o usuário com o e-mail e a senha fornecidos
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Credenciais inválidas!!Por favor, verifique seus dados"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    message="Login efetuado com sucesso"
    return render(request,"index.html",{"email":email})

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # criando um usuário com o e-mail e senha fornecidos
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
        messages.warning(request, 'Preencha todos os campos corretamente')
    except:
        
        return render(request, "Registration.html")
    messages.success(request, 'Cadastro realizado com sucesso')
    return render(request,"Login.html")

def reset(request):
    return render(request, "Reset.html")
 
def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "Um e-mail para redefinir a senha foi enviado com sucesso"
        return render(request, "Reset.html", {"msg":message})
    except:
        message  = "Algo deu errado, por favor, verifique se o e-mail que você forneceu está registrado ou não"
        return render(request, "Reset.html", {"msg":message})