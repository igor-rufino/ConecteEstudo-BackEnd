from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AlunoApp.models import Alunos
from AlunoApp.serializers import AlunoSerializer


@csrf_exempt
def alunoAPI(request, id=0):
    if request.method == "GET":
        alunos = Alunos.objects.all()
        alunos_serializer = AlunoSerializer(alunos, many=True)
        return JsonResponse(alunos_serializer.data, safe=False)

    elif request.method == "POST":
        aluno_data = JSONParser().parse(request)
        alunos_serializer = AlunoSerializer(data=aluno_data)
        if alunos_serializer.is_valid():
            alunos_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)

    elif request.method == "PUT":
        aluno_data = JSONParser().parse(request)
        aluno = Alunos.objects.get(AlunoId=aluno_data["AlunoId"])
        alunos_serializer = AlunoSerializer(aluno, data=aluno_data)
        if alunos_serializer.is_valid():
            alunos_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)

    elif request.method == "DELETE":
        aluno = Alunos.objects.get(AlunoId=id)
        aluno.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
