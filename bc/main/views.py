from django.shortcuts import render

from .models import *

def home(request):
    prods = Products.objects.all()
    return render(request, 'main/index.html', {'prods':prods})
