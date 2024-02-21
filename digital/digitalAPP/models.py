# models.py
from django.db import models
    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True) # Ajoutez d'autres champs d'utilisateur selon vos besoins
    cardID = models.CharField(max_length=100, unique=True)
    webauthn_id = models.TextField(blank=True, null=True)  # Stockez l'ID WebAuthn de l'utilisateur
    