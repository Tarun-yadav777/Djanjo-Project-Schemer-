from django.shortcuts import render
from django.http import HttpResponse
from .models import Schemegen

def index(request):
    return render(request, 'Index.html')


def adhaar(request):
    return render(request, 'Adhaar.html')


def requirements(request):
    return render(request, 'Requirements.html')


def detail(request):
    type = request.GET['occupation']
    schemes = Schemegen.objects.filter(type=type)
    return render(request, 'detail.html', {'schemes': schemes})


def adhaar_hindi(request):
    return render(request, 'adhaar_hindi.html')


def requirements_hindi(request):
    return render(request, 'requirements_hindi.html')
