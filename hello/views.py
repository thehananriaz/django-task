from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponse


def home(request):
    return HttpResponse("yo")
def showformdata(request):
    sf=StudentRegistration()
    return render(request, 'forms/regi.html', {'form':sf})