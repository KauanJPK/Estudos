from django.shortcuts import render
from django.http import HttpResponse   

# Logica de Programação

def show_homepages(request):
    return render(request, 'homepage.html')

def show_cadastro(request):
    return render(request, 'cadastro.html')
