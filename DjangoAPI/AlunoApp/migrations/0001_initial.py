# Generated by Django 4.0.3 on 2022-03-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('AlunoId', models.AutoField(primary_key=True, serialize=False)),
                ('AlunoName', models.CharField(max_length=500)),
                ('AlunoEmail', models.CharField(max_length=500)),
                ('AlunoSenha', models.CharField(max_length=500)),
            ],
        ),
    ]