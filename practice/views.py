from django.shortcuts import render
from django.views.generic import TemplateView, View


# Create your views here.
def hello_world(request):
    # return HttpResponse("hello world")
    return render(request, "new.html", {"name": "hamza"})


class new_helo_msg(TemplateView, View):
    template_name = "new.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"name": "hamza"})
        return context


class new_helo_msg2(TemplateView, View):
    template_name = "new2.html"
