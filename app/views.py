from django.shortcuts import render, HttpResponse
from .models import Produto
from django.views.generic import ListView
from django.contrib.auth.models import User



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
    if request.method == "GET":
        return render (request, 'register.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        user = User.objects.get.filter(username=email)
        if user:
            return HttpResponse('User já cadastrado')

        return HttpResponse(email)

def makeContact(request):
    return render (request, 'contact.html')