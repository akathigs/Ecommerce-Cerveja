from django.shortcuts import render

def makeIndex(request):
    return render (request, 'index.html')