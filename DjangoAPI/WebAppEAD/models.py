import email
from unicodedata import name
from djongo import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Descontinuado
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


class UserEvent(models.Model):
    eventId = models.ObjectIdField()
    eventType = models.IntegerField()
    classId = models.IntegerField()
    teacherName = models.CharField(max_length=1500)
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    dateOfEvent = models.DateField()
    timeOfEvent = models.TimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    updatedBy = models.IntegerField()
    status = models.CharField(max_length=1500)
    user = models.ForeignKey("User", on_delete=models.CASCADE)


# Descontinuado
class Absence(models.Model):
    absenceId = models.ObjectIdField()
    studentId = models.IntegerField()
    count = models.IntegerField()
    classId = models.IntegerField()
    date = models.DateField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class UserAbsence(models.Model):
    absenceId = models.ObjectIdField()
    count = models.IntegerField()
    classId = models.IntegerField()
    date = models.DateTimeField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    user = models.ForeignKey("User", on_delete=models.CASCADE)


# Descontinuado
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


class UserAssignment(models.Model):
    assignmentId = models.ObjectIdField()
    identifier = models.IntegerField()
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
    user = models.ForeignKey("User", on_delete=models.CASCADE)


# Descontinuado
class Classroom(models.Model):
    classroomId = models.ObjectIdField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()


class UserClassroom(models.Model):
    classroomId = models.ObjectIdField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()
    user = models.ManyToManyField("User")


class User(models.Model):
    userId = models.ObjectIdField()
    userName = models.CharField(max_length=1500)
    email = models.CharField(max_length=1500, unique=True)
    password = models.CharField(max_length=1500)
    phone = models.CharField(max_length=1500)
    birthdate = models.DateTimeField()
    profileType = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()


class Material(models.Model):
    MaterialId = models.ObjectIdField()
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    attachment = models.CharField(max_length=1500)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    createdBy = models.IntegerField()
    classId = models.IntegerField()
    teacherId = models.IntegerField()


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


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Usuário deve ter um email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.ObjectIdField()
    email = models.EmailField(max_length=1500, unique=True)
    name = models.CharField(max_length=1500)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
