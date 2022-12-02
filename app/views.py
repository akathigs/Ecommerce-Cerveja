from django.shortcuts import render
from .models import Produto
from django.views.generic import ListView


class ProdctListView(ListView):
    model = Produto


def makeIndex(request):
    return render (request, 'index.html')

def makeProducts(request):
    return render (request, 'products.html')

def makeAbout(request):
    return render (request, 'about.html')

def makeLogin(request):
    return render (request, 'login.html')

def makeRegister(request):
    return render (request, 'register.html')

def makeContact(request):
    return render (request, 'contact.html')