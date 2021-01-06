from django.shortcuts import render
from .models import Resume


def home(request):
    return render(request, 'resume/home.html')


def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {"resume": resume})
    
