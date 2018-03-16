from django import forms
from .models import Estado


class EstadoForm(forms.ModelForm):
    """Form definition for Estado."""

    class Meta:
        """Meta definition for Estadoform."""

        model = Estado
        fields = '__all__'
