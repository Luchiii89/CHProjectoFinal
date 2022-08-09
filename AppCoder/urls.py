from operator import imod
from django.urls import path, include
from django.views import View
import django.contrib.auth.views
from AppCoder.views import *
from AppCoder import views
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [   
    path('', views.Index, name="Index"),
    
    #Login
    path('login/', login_request, name='login'), 
    path('register/', register, name='register'), 
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'), 
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar/', views.agregarAvatar, name="AgregarAvatar"),
    
    # DOCTOR
    path('newDoctor/', NewDoctor.as_view(), name="newDoctor"),
    path('listDoctor/', ListDoctor.as_view(), name="listDoctor"), 
    path('doctor/<pk>', DoctorDetailView.as_view(), name="doctorDetail"),
    path('deleteDoctor/<pk>', DeleteDoctor.as_view(), name="deleteDoctor"),
    path('updateDoctor/<pk>', UpdateDoctor.as_view(), name="updateDoctor"),
    path('getDoctorBySurname', views.getDoctorBySurname, name="getDoctorBySurname"), #incompleto
    path('getDoctor/', views.getDoctor, name="getDoctor"), #incompleto
    
    #PATIENT
    path('newPatient/', NewPatient.as_view(), name="newPatient"),
    path('listPatient/', ListPatient.as_view(), name="listPatient"),
    path('patient/<pk>', PatientDetailView.as_view(), name="patientDetail"),
    path('deletePatient/<pk>', DeletePatient.as_view(), name="deletePatient"),
    path('updatePatient/<pk>', UpdatePatient.as_view(), name="updatePatient"),

    #DEPARTMENT
    path('newDepartment/', NewDepartment.as_view(), name="newDepartment"),
    path('listDepartment/', ListDepartment.as_view(), name="listDepartment"),
    path('department/<pk>', DepartmentDetailView.as_view(), name="departmentDetail"),
    path('deleteDepartment/<pk>', DeleteDepartment.as_view(), name="deleteDepartment"),
    path('updateDepartment/<pk>', UpdateDepartment.as_view(), name="updateDepartment"),

    #HISTORIAS CLINICAS
    path('newHistory/', NewHistory.as_view(), name="newHistory"),
    path('listHistory/', ListHistory.as_view(), name="listHistory"),
    path('history/<pk>', HistoryDetailView.as_view(), name="historyDetail"),
    path('deleteHistory/<pk>', DeleteHistory.as_view(), name="deleteHistory"),
    path('updateHistory/<pk>', UpdateHistory.as_view(), name="updateHistory"),

    path('ourServices', OurServices.as_view(), name="ourServices"),
    path('aboutUs', About.as_view(), name="aboutUs"),
]