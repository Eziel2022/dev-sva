from django.http import HttpResponse
from django.shortcuts import render

def appView(request):
    return render(request, 'app/index.html')
