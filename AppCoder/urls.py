from operator import imod
from django.urls import path, include
from django.views import View
from AppCoder import views
from AppCoder.views import *
from .views import ListView

urlpatterns = [   
    path('', views.Start.as_view(), name="Start"),
    path('newDoctor/', views.newDoctor.as_view(), name="newDoctor"),
    path('newPatient/', views.newPatient.as_view(), name="newPatient"),
    path('listDoctor/', views.ListDoctor.as_view(), name="listDoctor"), #Clase Vista, name="listDoctor" ->tiene que coincidir con el TP
    path('listPatient/', views.ListPatient.as_view(), name="listPatient"),
    path('doctorBySurname/', views.getDoctorBySurname.as_view(), name="doctorBySurname"),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    path('login/', views.login_request, name='login'),

    path('getDoctorBySurname/', views.getDoctorBySurname.as_view(), name="getDoctor"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
    #path('deleteDoctor/<int:pk>', views.deleteDoctor, name="deleteDoctor"), #Eliminamos 
]