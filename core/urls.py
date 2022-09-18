from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create-patient/", views.create_patient, name="create-patient"),
    path("edit-patient/<int:id>/", views.edit_patient, name="edit-patient"),
    path("delete-patient/", views.delete_patient, name="delete-patient"),
    path("patients-list/", views.patients, name="patients"),
]
