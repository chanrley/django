from django import forms
from .models import Exemplo

class ExemploForm(forms.ModelForm):
    class Meta:
        model = Exemplo
        fields = ('campo1', 'campo2', 'campo3')
