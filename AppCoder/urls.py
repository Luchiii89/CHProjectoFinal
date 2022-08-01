from operator import imod
from django.urls import path, include
from django.views import View
from AppCoder.views import *
from .views import *

urlpatterns = [   
    path('', Index.as_view(), name="Index"),
    
    # DOCTOR
    path('newDoctor/', NewDoctor.as_view(), name="newDoctor"),
    path('listDoctor/', ListDoctor.as_view(), name="listDoctor"), 
    path('doctor/<pk>', DoctorDetailView.as_view(), name="doctorDetail"),
    path('doctorBySurname/', GetDoctorBySurname.as_view(), name="doctorBySurname"),
    path('deleteDoctor/<pk>', DeleteDoctor.as_view(), name="deleteDoctor"),
    path('updateDoctor/<pk>', UpdateDoctor.as_view(), name="updateDoctor"),
    
    #PATIENT
    path('newPatient/', NewPatient.as_view(), name="newPatient"),
    path('listPatient/', ListPatient.as_view(), name="listPatient"),
    path('patient/<pk>', PatientDetailView.as_view(), name="patientDetail"),
    path('deletePatient/<pk>', DeletePatient.as_view(), name="deletePatient"),
    path('updatePatient/<pk>', UpdatePatient.as_view(), name="updatePatient"),
    
    path('login/', login_request, name='login'),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
]