from AlunoApp import views

from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^aluno$", views.alunoAPI, name="alunoAPI"),
    re_path(r"^aluno/([0-9]+)$", views.alunoAPI),
    re_path(r"^studentLogin$", views.alunoLoginAPI),
]
