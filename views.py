from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def berita(request):
    template = loader.get_template('berita.html')
    return HttpResponse(template.render())

def isi(request):
    template = loader.get_template('isi.html')
    return HttpResponse(template.render())

def isi1(request):
    template = loader.get_template('isi1.html')
    return HttpResponse(template.render())


