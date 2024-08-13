from . import views
from django.urls import path

urlpatterns = [
    path('', view=views.new_helo_msg.as_view()),
    path('new2/', view=views.new_helo_msg2.as_view())
]