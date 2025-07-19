from django.shortcuts import render
from portfolio.models import *
# Create your views here.

def user(request):
    user = User.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'user.html', context)

def project(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'project.html')