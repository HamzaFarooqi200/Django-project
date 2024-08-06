from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def hello_world(request):
    #return HttpResponse("hello world")
    return render(request, "new.html")
class new_helo_msg(View):
    template_name= "new.html"
    