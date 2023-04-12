from django.forms import ModelForm
from .models import *
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


class CrearBarrilForm(ModelForm):
    class Meta:
        model = Barril
        fields = ['num_barril', 'volumen']
        

    def clean(self):
        cleaned_data = super().clean()
        num_barril = cleaned_data.get('num_barril')        
        if Barril.objects.filter(num_barril=num_barril).exists():
            raise forms.ValidationError('Ya existe un barril con esos valores.')


class aaaRangoBarrilesForm(ModelForm):
    class Meta:
        model = Barril
        fields = ['num_barril', 'volumen']

    def clean(self):
        cleaned_data = super().clean()
        num_barril = cleaned_data.get('num_barril')        
        if Barril.objects.filter(num_barril=num_barril).exists():
            raise forms.ValidationError('Ya existe un barril con esos valores.')


class RangoBarrilesForm(forms.Form):
    model = Barril

    desde = forms.IntegerField()
    hasta = forms.IntegerField()
    volumen = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        num_barril = cleaned_data.get('num_barril')        
        if Barril.objects.filter(num_barril=num_barril).exists():
            raise forms.ValidationError('Ya existe un barril con esos valores.')



class EmbarrilarLoteForm(ModelForm):
    class Meta:
        model = Embarrilado
        fields = '__all__'