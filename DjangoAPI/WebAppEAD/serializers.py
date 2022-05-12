# from attr import fields
from rest_framework import serializers
from WebAppEAD.models import (
    Event,
    Absence,
    Assignment,
    Classroom,
    User,
    Material,
    TeachingPlan,
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "eventId",
            "eventType",
            "classId",
            "teacherName",
            "title",
            "description",
            "dateOfEvent",
            "createdAt",
            "updatedAt",
            "updatedBy",
            "status",
        )


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = (
            "absenceId",
            "studentId",
            "count",
            "classId",
            "date",
            "createdAt",
            "updatedAt",
        )


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            "assignmentId",
            "identifier",
            "studentId",
            "title",
            "classId",
            "createdAt",
            "updatedAt",
            "createdBy",
            "updatedBy",
            "deliveredAt",
            "deliveredMaterial",
            "score",
            "attachment",
        )


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = (
            "classroomId",
            "createdAt",
            "updatedAt",
            "createdBy",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "userId",
            "userName",
            "email",
            "phone",
            "birthdate",
            "profileType",
            "createdAt",
            "updatedAt",
            "events",
            "absences",
            "assignments",
            "classrooms",
        )


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            "MaterialId",
            "title",
            "description",
            "attachment",
            "createdAt",
            "updatedAt",
            "createdBy",
            "classId",
            "teatcherId",
        )


class TeachingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingPlan
        fields = (
            "teachingPlanId",
            "title",
            "description",
            "teacherName",
            "state",
            "workload",
            "absencesLimit",
            "year",
            "evaluation",
        )
