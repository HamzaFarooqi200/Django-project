from . import views
from django.urls import path

urlpatterns = [
    path('thanks/', view=views.hello_world, name="thanks_view"),
    path('signup/', view=views.Signup.as_view()),
    path('login/', view=views.Login.as_view())
]