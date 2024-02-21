# forms.py
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname']
        fields = ['lastname']
        fields = ['cardID']
        fields = ['username']# Ajoutez d'autres champs d'utilisateur selon vos besoins

class UserAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=100)
    cardID = forms.IntegerField(max_value=50)
    # Ajoutez d'autres champs d'authentification selon vos besoins
