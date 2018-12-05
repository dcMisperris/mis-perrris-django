from django import forms
from .models import forms

class LoginForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('email','passwd')
