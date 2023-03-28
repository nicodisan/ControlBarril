from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from .models import *
from .forms import ClienteForm, EstiloForm, CreateUserForm
from .filter import OrderFilter

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == "POST":
        request.POST.get('username')
        request.POST.get('password')

        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, username)
            return redirect('home')
    context = {}
    return render(request, 'accounts/login.html', context)


def home(request):
    orders = Embarrilado.objects.all()
    clientes = Cliente.objects.all()
    barriles = Barril.objects.all()
    estilos = Estilo.objects.all()
    lotes = Lote.objects.all()

    total_clientes = clientes.count()
    total_orders = orders.count()
    

    context = {'orders':orders, 'clientes':clientes, 'total_orders':total_orders, 'barriles': barriles, 'estilos': estilos, 'lotes': lotes}

    return render(request, 'accounts/dashboard.html', context)

def barriles(request):
    barriles = Barril.objects.all()

    return render(request, 'accounts/barriles.html', {'barriles': barriles})

def cliente(request, pk_test):
    cliente = Cliente.objects.get(id=pk_test)

    context = {'cliente':cliente}
    return render(request, 'accounts/cliente.html', context)

def nuevoCliente(request):

    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    
    context = {'form': form}
    return render(request, 'accounts/nuevo_cliente.html', context)


def crearEstilo(request):

    form = EstiloForm()
    if request.method == 'POST':
        form = EstiloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

   
    context = {'form': form}
    return render(request, 'accounts/nuevo_estilo.html', context)


def crearLote(request):

    form = LoteForm()
    if request.method == 'POST':
        form = LoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

   
    context = {'form': form}
    return render(request, 'accounts/nuevo_lote.html', context)