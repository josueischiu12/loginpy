from django import forms
from .models import Paginas

class PaginaForm(forms.ModelForm):
    """Form definition for Pagina."""

    class Meta:
        """Meta definition for Paginaform."""

        model = Paginas
        fields = ('titulo', 'contenido', 'orden')
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'contenido' : forms.Textarea(attrs={'class':'form-control'}),
            'orden' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Orden'}),
        }
        labels = {
            'titulo' : '', 'contenido' : '', 'orden' : ''
        }
