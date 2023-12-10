from django.shortcuts import render
from .models import Sills

def index(request):
    projects = Sills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})
