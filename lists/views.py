from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    response = render(request, 'home.html')
    # response is an HttpResponse
    # whose .content is the html from home.html
    return response
