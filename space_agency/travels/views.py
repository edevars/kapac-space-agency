from django.http import HttpResponse 

def home(request): 
    dummy_html = "<h1> Hi! You are visiting the space travel agency</h1>"

    return HttpResponse(dummy_html)