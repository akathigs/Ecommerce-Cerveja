from django.shortcuts import render

def makeIndex(request):
    return render (request, 'index.html')

def makeProducts(request):
    return render (request, 'products.html')