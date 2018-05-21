from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse

def health(request):
    return HttpResponse("<html><body>I'm healthy</body></html>")

def index(request, template_name='index.html'):
    data = {}
    return render(request, template_name, data)
