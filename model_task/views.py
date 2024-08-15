from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from .forms import LoginForm, SignupForm

# @method_decorator(login_required(login_url="/model_task/login/"), name="dispatch")


def checkAuthentication(request):
    if request.user.is_authenticated:
        return render(request, "checknew.html")
    else:
        return HttpResponsePermanentRedirect(redirect_to=reverse_lazy("login"))


class HelloWorld(View, LoginRequiredMixin):
    template_name = "check.html"
    login_url = reverse_lazy("login")

    def post(self, request):
        logout(request)
        return HttpResponsePermanentRedirect(redirect_to=reverse_lazy("login"))

    def get(self, request):
        print("User authenticated:", request.user.is_authenticated)
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return HttpResponsePermanentRedirect(redirect_to=reverse_lazy("login"))


class Signup(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")

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
