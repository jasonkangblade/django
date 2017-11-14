from django.http import HttpResponse

def homepage(req):
    return  HttpResponse("<h1>Hello World!</h1>")
