# views.py
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserAuthenticationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore
#from cryptography.hazmat.primitives import serialization
#from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode

def index(request):
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username'] = user.username
            return redirect('sign-up')  # Rediriger vers la page d'inscription WebAuthn
    else:
        form = UserRegistrationForm()
    return render(request, 'sign-up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['username']
            request.session['username'] = firstname
            return redirect('login')  # Rediriger vers la page de connexion WebAuthn
    else:
        form = UserAuthenticationForm()
    return render(request, 'login.html', {'form': form})

