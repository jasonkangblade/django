
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'portals/home.html')