from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
def hello_world(request):
    return render(request, "check.html", {'name':'hamza'})