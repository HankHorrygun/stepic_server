from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def get_404(request, *args, **kwargs):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def test(request, *args, **kwargs):
    return HttpResponse('OK')