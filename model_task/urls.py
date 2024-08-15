from django.urls import path

from . import views

urlpatterns = [
    path("thanks/", view=views.HelloWorld.as_view(), name="thanks_view"),
    path("signup/", view=views.Signup.as_view()),
    path("login/", view=views.Login.as_view(), name="login"),
    path("check/", view=views.checkAuthentication),
]
