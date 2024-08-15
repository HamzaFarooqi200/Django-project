from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.new_helo_msg.as_view()),
    path("new2/", view=views.new_helo_msg2.as_view()),
]
