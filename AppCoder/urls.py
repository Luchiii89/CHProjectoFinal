from operator import imod
from django.urls import path, include
from django.views import View
from AppCoder.views import *
from .views import *

urlpatterns = [   
    path('', Start.as_view(), name="Start"),
    # DOCTOR
    path('newDoctor/', newDoctor.as_view(), name="newDoctor"),
    path('listDoctor/', ListDoctor.as_view(), name="listDoctor"), 
    path('doctorBySurname/', getDoctorBySurname.as_view(), name="doctorBySurname"),
    path('deleteDoctor/<pk>', deleteDoctor.as_view(), name="deleteDoctor"),
    path('updateDoctor/<pk>', updateDoctor.as_view(), name="updateDoctor"),
    
    #PATIENT
    path('newPatient/', newPatient.as_view(), name="newPatient"),
    path('listPatient/', ListPatient.as_view(), name="listPatient"),
    path('deletePatient/<pk>', deletePatient.as_view(), name="deletePatient"),
    path('updatePatient/<pk>', updatePatient.as_view(), name="updatePatient"),
    
    path('login/', login_request, name='login'),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
]