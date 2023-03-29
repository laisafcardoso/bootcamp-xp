from django.shortcuts import render

def index(request):
    return render(request, 'user/index.html')

def create(request):
    return render(request, 'user/criar.html')

    
