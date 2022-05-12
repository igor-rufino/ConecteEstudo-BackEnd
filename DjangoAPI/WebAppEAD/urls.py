from WebAppEAD import views

from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^user$", views.userAPI, name="userAPI"),
    re_path(r"^user/([0-9]+)$", views.userAPI),
    re_path(r"^event$", views.eventAPI, name="eventAPI"),
    re_path(r"^event/([0-9]+)$", views.eventAPI),
    re_path(r"^assignment$", views.assignmentAPI, name="assignmentAPI"),
    re_path(r"^assignment/([0-9]+)$", views.assignmentAPI),
    re_path(r"^classroom$", views.classroomAPI, name="classroomAPI"),
    re_path(r"^classroom/([0-9]+)$", views.classroomAPI),
    re_path(r"^absence$", views.absenceAPI, name="absenceAPI"),
    re_path(r"^absence/([0-9]+)$", views.absenceAPI),
    re_path(r"^material$", views.materialAPI, name="materialAPI"),
    re_path(r"^material/([0-9]+)$", views.materialAPI),
    re_path(r"^teachingPlan$", views.teachingPlanAPI, name="teachingPlanAPI"),
    re_path(r"^teachingPlan/([0-9]+)$", views.teachingPlanAPI),
]
