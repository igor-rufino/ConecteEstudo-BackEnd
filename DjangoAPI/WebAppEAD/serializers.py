# from attr import fields
from rest_framework import serializers
from WebAppEAD.models import (
    Event,
    UserEvent,
    Absence,
    UserAbsence,
    Assignment,
    UserAssignment,
    Classroom,
    UserClassroom,
    User,
    Material,
    TeachingPlan,
)
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

DjoserUser = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = DjoserUser
        fields = ("id", "email", "name", "password")


# Descontinuado
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


class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = (
            "eventId",
            "eventType",
            "classId",
            "teacherName",
            "title",
            "description",
            "dateOfEvent",
            "timeOfEvent",
            "createdAt",
            "updatedAt",
            "updatedBy",
            "status",
            "user",
        )


# Descontinuado
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


class UserAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAbsence
        fields = (
            "absenceId",
            "count",
            "classId",
            "date",
            "createdAt",
            "updatedAt",
            "user",
        )


# Descontinuado
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


class UserAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssignment
        fields = (
            "assignmentId",
            "identifier",
            "title",
            "description",
            "classId",
            "createdAt",
            "updatedAt",
            "createdBy",
            "updatedBy",
            "dueDate",
            "deliveredAt",
            "deliveredMaterial",
            "score",
            "attachment",
            "user",
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


class UserClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassroom
        fields = (
            "classroomId",
            "createdAt",
            "updatedAt",
            "createdBy",
            "user",
        )


class StudentClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClassroom
        fields = (
            "classroomId",
            "user",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "userId",
            "userName",
            "email",
            "password",
            "phone",
            "birthdate",
            "profileType",
            "createdAt",
            "updatedAt",
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
            "teacherId",
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
