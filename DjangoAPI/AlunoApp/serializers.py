from attr import fields
from rest_framework import serializers
from AlunoApp.models import Alunos


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ("AlunoId", "AlunoName", "AlunoEmail", "AlunoSenha")
