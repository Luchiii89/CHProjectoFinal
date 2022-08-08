from operator import imod
from django.urls import path, include
from django.views import View
import django.contrib.auth.views
from AppCoder.views import *
from .views import *
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [   
    path('', Index.as_view(), name="Index"),
    
    # DOCTOR
    path('newDoctor/', NewDoctor.as_view(), name="newDoctor"),
    path('listDoctor/', ListDoctor.as_view(), name="listDoctor"), 
    path('doctor/<pk>', DoctorDetailView.as_view(), name="doctorDetail"),
    
    path('doctorBySurname/<pk>', GetDoctorBySurname.as_view(), name="doctorBySurname"),
    path('doctorBySurname/', GetDoctorBySurname.as_view(), name="doctorBySurname"), #NO FUNCIONA
    
    path('deleteDoctor/<pk>', DeleteDoctor.as_view(), name="deleteDoctor"),
    path('updateDoctor/<pk>', UpdateDoctor.as_view(), name="updateDoctor"),
    
    #PATIENT
    path('newPatient/', NewPatient.as_view(), name="newPatient"),
    path('listPatient/', ListPatient.as_view(), name="listPatient"),
    path('patient/<pk>', PatientDetailView.as_view(), name="patientDetail"),
    path('deletePatient/<pk>', DeletePatient.as_view(), name="deletePatient"),
    path('updatePatient/<pk>', UpdatePatient.as_view(), name="updatePatient"),

    #DEPARTMENT
    path('listDepartment/', ListDepartment.as_view(), name="listDepartment"),
    path('department/<pk>', DepartmentDetailView.as_view(), name="departmentDetail"),
    path('deleteDepartment/<pk>', DeleteDepartment.as_view(), name="deleteDepartment"),
    path('updateDepartment/<pk>', UpdateDepartment.as_view(), name="updateDepartment"),
    
    path('ourServices', OurServices.as_view(), name="ourServices"),
    
    #Login
    path('login/', login_request, name='login'), 
    path('admin/', admin.site.urls),
    #path('login/',include('home.urls')), 
]