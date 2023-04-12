from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from .models import *
from .forms import *
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

def cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)

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

def crearBarril(request):

    form = CrearBarrilForm()
    if request.method == 'POST':       
        form = CrearBarrilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/nuevo_barril.html', context)


def crearLoteBarril(request):
    if request.method == 'POST':
        form = RangoBarrilesForm(request.POST)
        if form.is_valid():
            desde = form.cleaned_data['desde']
            hasta = form.cleaned_data['hasta']
            volumen = form.cleaned_data['volumen']
            for num_barril in range(desde, hasta + 1):
                Barril.objects.create(num_barril=num_barril, volumen=volumen)
            # Redirigir a una página de éxito
    else:
        form = RangoBarrilesForm()
    return render(request, 'accounts/nuevo_lote_barril.html', {'form': form})


#def embarrilarLote(request, pk):

def updateBarril(request):

    form = UpdateBarrilForm()
    if request.method == 'POST':
        form = UpdateBarrilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = UpdateBarrilForm()

    return render(request, 'accounts/update_barril.html', {'form': form})


