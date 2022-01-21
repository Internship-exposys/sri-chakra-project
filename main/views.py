from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def kriston(request):
    return render(request, 'main/kriston.html')

def srichakra(request):
    return render(request, 'main/srichakra.html')


def suryaIntech(request):
    return render(request, 'main/suryaIntech.html')

def products(request):
    return render(request, 'main/products.html')

def products_kriston(request):
    return render(request, 'main/kriston.html')

def products_srichakra(request):
    return render(request, 'main/srichakra.html')

def products_suryaIntech(request):
    return render(request, 'main/suryaIntech.html')
