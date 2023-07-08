from django.urls import path

from . import views

urlpatterns = [
    path("text/", views.serve_text),
    path("word/<str:word>", views.update_word)
]