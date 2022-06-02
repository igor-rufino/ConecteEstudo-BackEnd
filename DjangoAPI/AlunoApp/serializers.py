from attr import fields
from rest_framework import serializers
from AlunoApp.models import Alunos, StudentLogin


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ("AlunoId", "AlunoName", "AlunoEmail", "AlunoSenha")


class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLogin
        fields = (
            "AlunoEmail",
            "AlunoSenha",
        )