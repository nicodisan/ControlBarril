from django.forms import ModelForm
from .models import Cliente, Estilo, Lote
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EstiloForm(ModelForm):
    class Meta:
        model = Estilo
        fields = '__all__'

class LoteForm(ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'
