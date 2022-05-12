from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from WebAppEAD.models import (
    Event,
    Absence,
    Assignment,
    Classroom,
    User,
    Material,
    TeachingPlan,
)
from WebAppEAD.serializers import (
    EventSerializer,
    AbsenceSerializer,
    AssignmentSerializer,
    ClassroomSerializer,
    UserSerializer,
    MaterialSerializer,
    TeachingPlanSerializer,
)


@csrf_exempt
def userAPI(request, id=-1):
    # GET Usuário por ID
    if request.method == "GET" and id != -1:
        user = User.objects.get(userId=id)
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
            return JsonResponse("Usuário adicionado com sucesso", safe=False)
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
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("Usuário deletado com sucesso", safe=False)


@csrf_exempt
def eventAPI(request, id=-1):
    # GET Evento por ID
    if request.method == "GET" and id != -1:
        event = Event.objects.get(eventId=id)
        event_serializer = EventSerializer(event, many=True)
        return JsonResponse(event_serializer.data, safe=False)

    # GET Todos eventos
    elif request.method == "GET":
        events = Event.objects.all()
        event_serializer = EventSerializer(events, many=True)
        return JsonResponse(event_serializer.data, safe=False)

    # POST Novo evento
    elif request.method == "POST":
        event_data = JSONParser().parse(request)
        event_serializer = EventSerializer(data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse("Evento adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar evento", safe=False)

    # PUT Editar evento por ID
    elif request.method == "PUT":
        event_data = JSONParser().parse(request)
        event = Event.objects.get(eventId=event_data["eventId"])
        event_serializer = EventSerializer(event, data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse("Evento atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar evento", safe=False)

    # DELETE deletar evento por ID
    elif request.method == "DELETE":
        event = Event.objects.get(eventId=id)
        event.delete()
        return JsonResponse("Evento deletado com sucesso", safe=False)


@csrf_exempt
def assignmentAPI(request, id=-1, classId=-1):
    # GET Tarefa pelo ID
    if request.method == "GET" and id != -1:
        assignment = Assignment.objects.get(assignmentId=id)
        assignment_serializer = AssignmentSerializer(assignment, many=True)
        return JsonResponse(assignment_serializer.data, safe=False)

    # GET Todas tarefas
    elif request.method == "GET":
        assignments = Event.objects.all()
        assignment_serializer = AssignmentSerializer(assignments, many=True)
        return JsonResponse(assignment_serializer.data, safe=False)

    # POST Nova tarefa
    elif request.method == "POST":
        assignment_data = JSONParser().parse(request)
        assignment_serializer = AssignmentSerializer(data=assignment_data)
        if assignment_serializer.is_valid():
            assignment_serializer.save()
            return JsonResponse("Tarefa adicionada com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar tarefa", safe=False)

    # PUT Editar todas pelo ClassId
    elif request.method == "PUT" and classId != -1:
        assignment_data = JSONParser().parse(request)
        assignment = Assignment.objects.get(classId=assignment_data["classId"])
        assignment_serializer = AssignmentSerializer(assignment, data=assignment_data)
        if assignment_serializer.is_valid():
            assignment_serializer.save()
            return JsonResponse("Tarefa atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar tarefa", safe=False)

    # PUT Editar tarefa pelo ID
    elif request.method == "PUT":
        assignment_data = JSONParser().parse(request)
        assignment = Assignment.objects.get(
            assignmentId=assignment_data["assignmentId"]
        )
        assignment_serializer = AssignmentSerializer(assignment, data=assignment_data)
        if assignment_serializer.is_valid():
            assignment_serializer.save()
            return JsonResponse("Tarefa atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar tarefa", safe=False)

    # DELETE deletar tarefa por ID
    elif request.method == "DELETE":
        assignment = Assignment.objects.get(assignmentId=id)
        assignment.delete()
        return JsonResponse("Tarefa deletada com sucesso", safe=False)


@csrf_exempt
def classroomAPI(request, id=-1, userId=-1):
    # GET Turma pelo ID
    if request.method == "GET" and id != -1:
        classroom = Classroom.objects.get(classroomId=id)
        classroom_serializer = ClassroomSerializer(classroom, many=True)
        return JsonResponse(classroom_serializer.data, safe=False)

    # POST Nova turma
    elif request.method == "POST":
        classroom_data = JSONParser().parse(request)
        classroom_serializer = ClassroomSerializer(data=classroom_data)
        if classroom_serializer.is_valid():
            classroom_serializer.save()
            return JsonResponse("Turma adicionada com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar turma", safe=False)

    # PUT Editar turma pelo ID
    elif request.method == "PUT":
        classroom_data = JSONParser().parse(request)
        classroom = Classroom.objects.get(classroomId=classroom_data["classroomId"])
        classroom_serializer = ClassroomSerializer(classroom, data=classroom_data)
        if classroom_serializer.is_valid():
            classroom_serializer.save()
            return JsonResponse("Turma atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar turma", safe=False)

    # DELETE deletar tarefa por ID
    elif request.method == "DELETE":
        classroom = Classroom.objects.get(classroomId=id)
        classroom.delete()
        return JsonResponse("Turma deletada com sucesso", safe=False)


@csrf_exempt
def absenceAPI(request, id=-1, classId=-1, userId=-1):
    # GET Falta pelo ID (not PROD)
    if request.method == "GET" and id != -1:
        absence = Absence.objects.get(absenceId=id)
        absence_serializer = AbsenceSerializer(absence, many=True)
        return JsonResponse(absence_serializer.data, safe=False)

    # GET Falta pelo classId e userId
    elif request.method == "GET" and classId != -1 and userId != -1:
        absence = Absence.objects.get(classId=classId, userId=userId)
        absence_serializer = AbsenceSerializer(absence, many=True)
        return JsonResponse(absence_serializer.data, safe=False)

    # GET Falta pelo userId
    elif request.method == "GET" and userId != -1:
        absence = Absence.objects.get(userId=userId)
        absence_serializer = AbsenceSerializer(absence, many=True)
        return JsonResponse(absence_serializer.data, safe=False)

    # GET Falta pelo classId
    elif request.method == "GET" and classId != -1:
        absence = Absence.objects.get(classId=classId)
        absence_serializer = AbsenceSerializer(absence, many=True)
        return JsonResponse(absence_serializer.data, safe=False)

    # POST Nova falta
    elif request.method == "POST":
        absence_data = JSONParser().parse(request)
        absence_serializer = AbsenceSerializer(data=absence_data)
        if absence_serializer.is_valid():
            absence_serializer.save()
            return JsonResponse("Falta adicionada com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar falta", safe=False)

    # PUT Editar falta pelo ID
    elif request.method == "PUT":
        absence_data = JSONParser().parse(request)
        absence = Absence.objects.get(absenceId=absence_data["absenceId"])
        absence_serializer = AbsenceSerializer(absence, data=absence_data)
        if absence_serializer.is_valid():
            absence_serializer.save()
            return JsonResponse("Falta atualizada com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar falta", safe=False)

    # DELETE deletar tarefa por ID (not PROD)
    elif request.method == "DELETE":
        absence = Absence.objects.get(absenceId=id)
        absence.delete()
        return JsonResponse("Falta deletada com sucesso", safe=False)


@csrf_exempt
def materialAPI(request, id=-1, teacherId=-1, classId=-1):
    # GET Material pelo ID
    if request.method == "GET" and id != -1:
        material = Material.objects.get(materialId=id)
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)

    # GET Material pelo teacherId
    elif request.method == "GET" and teacherId != -1:
        material = Material.objects.get(teacherId=teacherId)
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)

    # GET Material pelo classId
    elif request.method == "GET" and classId != -1:
        material = Material.objects.get(classId=classId)
        material_serializer = MaterialSerializer(material, many=True)
        return JsonResponse(material_serializer.data, safe=False)

    # POST Novo material
    elif request.method == "POST":
        material_data = JSONParser().parse(request)
        material_serializer = MaterialSerializer(data=material_data)
        if material_serializer.is_valid():
            material_serializer.save()
            return JsonResponse("Material adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar material", safe=False)

    # PUT Editar material pelo ID
    elif request.method == "PUT":
        material_data = JSONParser().parse(request)
        material = Material.objects.get(materialId=material_data["materialId"])
        material_serializer = MaterialSerializer(material, data=material_data)
        if material_serializer.is_valid():
            material_serializer.save()
            return JsonResponse("Material atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar material", safe=False)

    # DELETE deletar material por ID
    elif request.method == "DELETE":
        material = Material.objects.get(materialId=id)
        material.delete()
        return JsonResponse("Material deletado com sucesso", safe=False)


@csrf_exempt
def teachingPlanAPI(request, id=-1, state=-1):
    # GET Plano pelo ID
    if request.method == "GET" and id != -1:
        teachingPlan = TeachingPlan.objects.get(teachingPlanId=id)
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)

    # GET Plano pelo estado inativo
    elif request.method == "GET" and state == 0:
        teachingPlan = TeachingPlan.objects.get(state=0)
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)

    # GET Plano pelo estado ativo
    elif request.method == "GET" and state == 1:
        teachingPlan = TeachingPlan.objects.get(state=1)
        teachingPlan_serializer = TeachingPlanSerializer(teachingPlan, many=True)
        return JsonResponse(teachingPlan_serializer.data, safe=False)

    # POST Novo plano
    elif request.method == "POST":
        teachingPlan_data = JSONParser().parse(request)
        teachingPlan_serializer = TeachingPlanSerializer(data=teachingPlan_data)
        if teachingPlan_serializer.is_valid():
            teachingPlan_serializer.save()
            return JsonResponse("Plano adicionado com sucesso", safe=False)
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
        teachingPlan = TeachingPlan.objects.get(teachingPlanId=id)
        teachingPlan.delete()
        return JsonResponse("Plano deletado com sucesso", safe=False)
