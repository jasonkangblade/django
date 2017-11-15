
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext,loader

def homepage(request):
    return render(request,'oauth2/home.html')
