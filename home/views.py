from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'escambo_app/pages/index.html')

def sobre(request):
    return render(request, 'escambo_app/pages/sobre.html')

def anuncie(request):
    return render(request, 'escambo_app/pages/anuncie.html')
