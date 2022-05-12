from djongo import models
from django import forms


class Event(models.Model):
    eventId = models.ObjectIdField()
    eventType = models.IntegerField()
    classId = models.IntegerField()
    teacherName = models.CharField(max_length=1500)
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    dateOfEvent = models.DateTimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    updatedBy = models.IntegerField()
    status = models.CharField(max_length=1500)


class Absence(models.Model):
    absenceId = models.ObjectIdField()
    studentId = models.IntegerField()
    count = models.IntegerField()
    classId = models.IntegerField()
    date = models.DateField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class Assignment(models.Model):
    assignmentId = models.ObjectIdField()
    identifier = models.IntegerField()
    studentId = models.IntegerField()
    title = models.CharField(max_length=1500)
    classId = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()
    updatedBy = models.IntegerField()
    deliveredAt = models.DateTimeField()
    deliveredMaterial = models.CharField(max_length=1500)
    score = models.FloatField()
    attachment = models.CharField(max_length=1500)


class Classroom(models.Model):
    classroomId = models.ObjectIdField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()


class User(models.Model):
    userId = models.ObjectIdField()
    userName = models.CharField(max_length=1500)
    email = models.CharField(max_length=1500)
    password = models.CharField(max_length=1500)
    phone = models.CharField(max_length=1500)
    birthdate = models.DateTimeField()
    profileType = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    events = models.ArrayField(model_container=Event)
    absences = models.ArrayField(model_container=Absence)
    assignments = models.EmbeddedField(model_container=Assignment)
    classrooms = models.EmbeddedField(model_container=Classroom)


class Material(models.Model):
    MaterialId = models.ObjectIdField()
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    attachment = models.CharField(max_length=1500)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()
    classId = models.IntegerField()
    teatcherId = models.IntegerField()


class TeachingPlan(models.Model):
    teachingPlanId = models.ObjectIdField()
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    teacherName = models.CharField(max_length=1500)
    state = models.IntegerField()
    workload = models.IntegerField()
    absencesLimit = models.IntegerField()
    year = models.DateField()
    evaluation = models.CharField(max_length=1500)
