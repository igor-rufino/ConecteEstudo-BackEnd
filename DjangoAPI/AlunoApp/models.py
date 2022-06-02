from django.db import models

# Create your models here.

class Alunos(models.Model):
    AlunoId = models.AutoField(primary_key=True)
    AlunoName = models.CharField(max_length=500)
    AlunoEmail = models.CharField(max_length=500)
    AlunoSenha = models.CharField(max_length=500)


class StudentLogin(models.Model):
    AlunoEmail = models.CharField(max_length=50)
    AlunoSenha = models.CharField(max_length=50)