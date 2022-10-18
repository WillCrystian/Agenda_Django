import imp
from django.db import models
from contato.models import Contato
from django import forms


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('data_criacao',)
        
        
        