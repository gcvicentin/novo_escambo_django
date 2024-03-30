from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'escambo_app/index.html')

def sobre(request):
    return render(request, 'escambo_app/sobre.html')

def anuncie(request):
    return render(request, 'escambo_app/anuncie.html')
