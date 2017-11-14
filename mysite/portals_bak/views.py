from django.http import HttpResponse

def home(reg):
    return HttpResponse("welcome")

