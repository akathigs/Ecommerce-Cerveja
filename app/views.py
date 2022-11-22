from django.shortcuts import render

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