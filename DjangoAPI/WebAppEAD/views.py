from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json


from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from WebAppEAD.models import (
    Event,
    Absence,
    Assignment,
    Classroom,
    User,
    Material,
    TeachingPlan,
    UserEvent,
    UserAbsence,
    UserAssignment,
    UserClassroom,
    UserAccount,
    UserAccountManager,
)
from WebAppEAD.serializers import (
    EventSerializer,
    AbsenceSerializer,
    UserAbsenceSerializer,
    AssignmentSerializer,
    UserAssignmentSerializer,
    ClassroomSerializer,
    UserClassroomSerializer,
    StudentClassroomSerializer,
    UserSerializer,
    UserEventSerializer,
    MaterialSerializer,
    TeachingPlanSerializer,
    UserCreateSerializer,
)


@csrf_exempt
def userAPI(request, id=-1):
    # GET Usuário por ID
    if request.method == "GET" and id != -1:
        user = User.objects.filter(userId=int(id))
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    # GET Todos usuários
    elif request.method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    # POST Novo usuário
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            userAccount = UserAccount.objects.create_user(
                email=user_data["email"],
                name=user_data["userName"],
                password=user_data["password"],
            )
            return JsonResponse(user_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar usuário", safe=False)

    # PUT Editar info do usuário por ID
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId=user_data["userId"])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Usuário atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar usuário", safe=False)

    # DELETE deletar usuário por ID (not PROD)
    elif request.method == "DELETE":
        user = User.objects.get(userId=int(id))
        user.delete()
        return JsonResponse("Usuário deletado com sucesso", safe=False)


@csrf_exempt
def userEventAPI(request, id=-1):
    # GET Eventos por userId
    if request.method == "GET" and id != -1:
        userEvent = UserEvent.objects.filter(user_id=int(id))
        userEvent_serializer = UserEventSerializer(userEvent, many=True)
        return JsonResponse(userEvent_serializer.data, safe=False)

    # POST Novo evento
    elif request.method == "POST":
        userEvent_data = JSONParser().parse(request)
        userEvent_serializer = UserEventSerializer(data=userEvent_data)
        if userEvent_serializer.is_valid():
            userEvent_serializer.save()
            return JsonResponse(userEvent_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar evento", safe=False)


@csrf_exempt
def eventAPI(request, id=-1):
    # GET Evento por ID
    if request.method == "GET" and id != -1:
        userEvent = UserEvent.objects.filter(eventId=int(id))
        userEvent_serializer = UserEventSerializer(userEvent, many=True)
        return JsonResponse(userEvent_serializer.data, safe=False)

    # GET Todos eventos
    elif request.method == "GET":
        userEvents = UserEvent.objects.all()
        userEvent_serializer = UserEventSerializer(userEvents, many=True)
        return JsonResponse(userEvent_serializer.data, safe=False)

    # PUT Editar evento por ID
    elif request.method == "PUT":
        userEvent_data = JSONParser().parse(request)
        userEvent = UserEvent.objects.get(eventId=userEvent_data["eventId"])
        userEvent_serializer = UserEventSerializer(userEvent, data=userEvent_data)
        if userEvent_serializer.is_valid():
            userEvent_serializer.save()
            return JsonResponse("Evento atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar evento", safe=False)

    # DELETE deletar evento por ID
    elif request.method == "DELETE":
        userEvent = UserEvent.objects.get(eventId=int(id))
        userEvent.delete()
        return JsonResponse("Evento deletado com sucesso", safe=False)


@csrf_exempt
def classAssignmentAPI(request, id=-1):
    # GET Tarefa pelo ID
    if request.method == "GET" and id != -1:
        userAssignment = UserAssignment.objects.filter(classId=int(id))
        userAssignment_serializer = UserAssignmentSerializer(userAssignment, many=True)
        return JsonResponse(userAssignment_serializer.data, safe=False)

    # PUT Editar todas pelo ClassId
    elif request.method == "PUT":
        userAssignment_data = JSONParser().parse(request)
        userAssignments = UserAssignment.objects.filter(
            classId=userAssignment_data["classId"]
        )
        try:
            for userAssignment in userAssignments:
                print(userAssignment.assignmentId)
                userAssignment_data["assignmentId"] = userAssignment.assignmentId
                userAssignment_serializer = UserAssignmentSerializer(
                    userAssignment, data=userAssignment_data
                )
                if userAssignment_serializer.is_valid():
                    userAssignment_serializer.save()
            return JsonResponse("Tarefas atualizadas com sucesso", safe=False)
        except:
            return JsonResponse("Falha ao atualizar tarefas", safe=False)


@csrf_exempt
def assignmentAPI(request, id=-1):
    # GET Tarefa pelo ID
    if request.method == "GET" and id != -1:
        userAssignment = UserAssignment.objects.filter(assignmentId=int(id))
        userAssignment_serializer = UserAssignmentSerializer(userAssignment, many=True)
        return JsonResponse(userAssignment_serializer.data, safe=False)

    # GET Todas tarefas
    elif request.method == "GET":
        userAssignments = UserAssignment.objects.all()
        userAssignment_serializer = UserAssignmentSerializer(userAssignments, many=True)
        return JsonResponse(userAssignment_serializer.data, safe=False)

    # POST Nova tarefa
    elif request.method == "POST":
        userAssignment_data = JSONParser().parse(request)
        userAssignment_serializer = UserAssignmentSerializer(data=userAssignment_data)
        if userAssignment_serializer.is_valid():
            userAssignment_serializer.save()
            return JsonResponse(userAssignment_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar tarefa", safe=False)

    # PUT Editar tarefa pelo ID
    elif request.method == "PUT":
        userAssignment_data = JSONParser().parse(request)
        userAssignment = UserAssignment.objects.get(
            assignmentId=userAssignment_data["assignmentId"]
        )
        userAssignment_serializer = UserAssignmentSerializer(
            userAssignment, data=userAssignment_data
        )
        if userAssignment_serializer.is_valid():
            userAssignment_serializer.save()
            return JsonResponse("Tarefa atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar tarefa", safe=False)

    # DELETE deletar tarefa por ID
    elif request.method == "DELETE":
        userAssignment = UserAssignment.objects.get(assignmentId=int(id))
        userAssignment.delete()
        return JsonResponse("Tarefa deletada com sucesso", safe=False)


@csrf_exempt
def userClassroomAPI(request, id=-1):
    # GET alunos pelo classroomID
    if request.method == "GET" and id != -1:
        studentClassroom = UserClassroom.objects.filter(classroomId=int(id))
        studentClassroom_serializer = StudentClassroomSerializer(
            studentClassroom, many=True
        )
        return JsonResponse(studentClassroom_serializer.data, safe=False)


@csrf_exempt
def classroomAPI(request, id=-1):
    # GET Turma pelo ID
    if request.method == "GET" and id != -1:
        userClassroom = UserClassroom.objects.filter(classroomId=int(id))
        userClassroom_serializer = UserClassroomSerializer(userClassroom, many=True)
        return JsonResponse(userClassroom_serializer.data, safe=False)

    # GET todas Turmas
    if request.method == "GET":
        userClassroom = UserClassroom.objects.all()
        userClassroom_serializer = UserClassroomSerializer(userClassroom, many=True)
        return JsonResponse(userClassroom_serializer.data, safe=False)

    # POST Nova turma
    elif request.method == "POST":
        userClassroom_data = JSONParser().parse(request)
        userClassroom_serializer = UserClassroomSerializer(data=userClassroom_data)
        if userClassroom_serializer.is_valid():
            userClassroom_serializer.save()
            return JsonResponse(userClassroom_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar turma", safe=False)

    # PUT Editar turma pelo ID
    elif request.method == "PUT":
        userClassroom_data = JSONParser().parse(request)
        userClassroom = UserClassroom.objects.get(
            classroomId=userClassroom_data["classroomId"]
        )
        userClassroom_serializer = UserClassroomSerializer(
            userClassroom, data=userClassroom_data
        )
        if userClassroom_serializer.is_valid():
            userClassroom_serializer.save()
            return JsonResponse("Turma atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar turma", safe=False)

    # DELETE deletar tarefa por ID
    elif request.method == "DELETE":
        userClassroom = UserClassroom.objects.filter(classroomId=int(id))
        userClassroom.delete()
        return JsonResponse("Turma deletada com sucesso", safe=False)


@csrf_exempt
def userAbsenceAPI(request, id=-1):
    # GET faltas por userId
    if request.method == "GET" and id != -1:
        userAbsence = UserAbsence.objects.filter(user_id=int(id))
        userAbsence_serializer = UserAbsenceSerializer(userAbsence, many=True)
        return JsonResponse(userAbsence_serializer.data, safe=False)

    # POST Nova falta por userId
    elif request.method == "POST":
        userAbsence_data = JSONParser().parse(request)
        userAbsence_serializer = UserAbsenceSerializer(data=userAbsence_data)
        if userAbsence_serializer.is_valid():
            userAbsence_serializer.save()
            return JsonResponse(userAbsence_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar falta", safe=False)


@csrf_exempt
def classAbsenceAPI(request, id=-1):
    # GET faltas por classId
    if request.method == "GET" and id != -1:
        userAbsence = UserAbsence.objects.filter(classId=int(id))
        userAbsence_serializer = UserAbsenceSerializer(userAbsence, many=True)
        return JsonResponse(userAbsence_serializer.data, safe=False)


@csrf_exempt
def absenceAPI(request, id=-1):
    # GET Falta pelo ID (not PROD)
    if request.method == "GET" and id != -1:
        userAbsence = UserAbsence.objects.filter(absenceId=int(id))
        userAbsence_serializer = UserAbsenceSerializer(userAbsence, many=True)
        return JsonResponse(userAbsence_serializer.data, safe=False)

    # PUT Editar falta pelo ID
    elif request.method == "PUT":
        userAbsence_data = JSONParser().parse(request)
        userAbsence = UserAbsence.objects.get(absenceId=userAbsence_data["absenceId"])
        userAbsence_serializer = UserAbsenceSerializer(
            userAbsence, data=userAbsence_data
        )
        if userAbsence_serializer.is_valid():
            userAbsence_serializer.save()
            return JsonResponse("Falta atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar falta", safe=False)

    # DELETE deletar tarefa por ID (not PROD)
    elif request.method == "DELETE":
        userAbsence = UserAbsence.objects.get(absenceId=id)
        userAbsence.delete()
        return JsonResponse("Falta deletada com sucesso", safe=False)


@csrf_exempt
def teacherMaterialAPI(request, id=-1):
    # GET Material pelo teacherId
    if request.method == "GET" and id != -1:
        material = Material.objects.filter(teacherId=int(id))
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)


@csrf_exempt
def classMaterialAPI(request, id=-1):
    # GET Material pelo classId
    if request.method == "GET" and id != -1:
        material = Material.objects.filter(classId=int(id))
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)


@csrf_exempt
def materialAPI(request, id=-1):
    # GET Material pelo ID
    if request.method == "GET" and id != -1:
        material = Material.objects.filter(MaterialId=int(id))
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)

    # POST Novo material
    elif request.method == "POST":
        material_data = JSONParser().parse(request)
        material_serializer = MaterialSerializer(data=material_data)
        if material_serializer.is_valid():
            material_serializer.save()
            return JsonResponse(material_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar material", safe=False)

    # PUT Editar material pelo ID
    elif request.method == "PUT":
        material_data = JSONParser().parse(request)
        material = Material.objects.get(MaterialId=material_data["MaterialId"])
        material_serializer = MaterialSerializer(material, data=material_data)
        if material_serializer.is_valid():
            material_serializer.save()
            return JsonResponse("Material atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar material", safe=False)

    # DELETE deletar material por ID
    elif request.method == "DELETE":
        material = Material.objects.filter(MaterialId=int(id))
        material.delete()
        return JsonResponse("Material deletado com sucesso", safe=False)


@csrf_exempt
def stateTeachingPlanAPI(request, state=-1):
    # GET Plano pelo estado inativo
    if request.method == "GET" and int(state) == 0:
        teachingPlan = TeachingPlan.objects.filter(state=int(0))
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)

    # GET Plano pelo estado ativo
    elif request.method == "GET" and int(state) == 1:
        teachingPlan = TeachingPlan.objects.filter(state=int(1))
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)


@csrf_exempt
def teachingPlanAPI(request, id=-1):
    # GET Plano pelo ID
    if request.method == "GET" and id != -1:
        teachingPlan = TeachingPlan.objects.filter(teachingPlanId=int(id))
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)

    # POST Novo plano
    elif request.method == "POST":
        teachingPlan_data = JSONParser().parse(request)
        teachingPlan_serializer = TeachingPlanSerializer(data=teachingPlan_data)
        if teachingPlan_serializer.is_valid():
            teachingPlan_serializer.save()
            return JsonResponse(teachingPlan_serializer.data, safe=False)
        return JsonResponse("Falha ao adicionar plano", safe=False)

    # PUT Editar plano pelo ID
    elif request.method == "PUT":
        teachingPlan_data = JSONParser().parse(request)
        teachingPlan = TeachingPlan.objects.get(
            teachingPlanId=teachingPlan_data["teachingPlanId"]
        )
        teachingPlan_serializer = TeachingPlanSerializer(
            teachingPlan, data=teachingPlan_data
        )
        if teachingPlan_serializer.is_valid():
            teachingPlan_serializer.save()
            return JsonResponse("Plano atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar plano", safe=False)

    # DELETE deletar plano por ID
    elif request.method == "DELETE":
        teachingPlan = TeachingPlan.objects.filter(teachingPlanId=int(id))
        teachingPlan.delete()
        return JsonResponse("Plano deletado com sucesso", safe=False)
