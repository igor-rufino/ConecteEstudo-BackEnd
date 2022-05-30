from WebAppEAD import views

from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^user$", views.userAPI, name="userAPI"),
    re_path(r"^user/([0-9]+)$", views.userAPI),
    re_path(r"^event$", views.eventAPI, name="eventAPI"),
    re_path(r"^event/([0-9]+)$", views.eventAPI),
    re_path(r"^userEvent$", views.userEventAPI, name="userEventAPI"),
    re_path(r"^userEvent/([0-9]+)$", views.userEventAPI),
    re_path(r"^classAssignment$", views.classAssignmentAPI, name="classAssignmentAPI"),
    re_path(r"^classAssignment/([0-9]+)$", views.classAssignmentAPI),
    re_path(r"^assignment$", views.assignmentAPI, name="assignmentAPI"),
    re_path(r"^assignment/([0-9]+)$", views.assignmentAPI),
    re_path(r"^classroom$", views.classroomAPI, name="classroomAPI"),
    re_path(r"^classroom/([0-9]+)$", views.classroomAPI),
    re_path(r"^userClassroom$", views.userClassroomAPI, name="userClassroomAPI"),
    re_path(r"^userClassroom/([0-9]+)$", views.userClassroomAPI),
    re_path(r"^absence$", views.absenceAPI, name="absenceAPI"),
    re_path(r"^absence/([0-9]+)$", views.absenceAPI),
    re_path(r"^userAbsence$", views.userAbsenceAPI, name="userAbsenceAPI"),
    re_path(r"^userAbsence/([0-9]+)$", views.userAbsenceAPI),
    re_path(r"^classAbsence$", views.classAbsenceAPI, name="classAbsenceAPI"),
    re_path(r"^classAbsence/([0-9]+)$", views.classAbsenceAPI),
    re_path(r"^material$", views.materialAPI, name="materialAPI"),
    re_path(r"^material/([0-9]+)$", views.materialAPI),
    re_path(r"^teacherMaterial$", views.teacherMaterialAPI, name="teacherMaterialAPI"),
    re_path(r"^teacherMaterial/([0-9]+)$", views.teacherMaterialAPI),
    re_path(r"^classMaterial$", views.classMaterialAPI, name="classMaterialAPI"),
    re_path(r"^classMaterial/([0-9]+)$", views.classMaterialAPI),
    re_path(r"^teachingPlan$", views.teachingPlanAPI, name="teachingPlanAPI"),
    re_path(r"^teachingPlan/([0-9]+)$", views.teachingPlanAPI),
    re_path(
        r"^stateTeachingPlan$", views.stateTeachingPlanAPI, name="stateTeachingPlanAPI"
    ),
    re_path(r"^stateTeachingPlan/([0-9]+)$", views.stateTeachingPlanAPI),
]
