from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name' : 'Nombre',
            'Type' : 'Tipo',
            'weight' : 'Peso',
            'height' : 'Altura',
            'trainer' : 'Entrenador',
            'picture' : 'Imagen Del Pokemon'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'Type': forms.Select(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'trainer': forms.Select(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }