from django.shortcuts import render
from django.views.generic import FormView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy



# Create your views here.
def hello_world(request):
    return render(request, "check.html", {'name':'hamza'})

class Signup(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("thanks_view")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("thanks_view")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            response = super().form_valid(form)
            return response
        else:
            form.add_error(None, "Invalid email or password")
            return self.form_invalid(form)