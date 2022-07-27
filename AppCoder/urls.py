from operator import imod
from django.urls import path, include
from django.views import View
from AppCoder import views
from AppCoder.views import *
from .views import ListView

urlpatterns = [
   
    path('', views.Start.as_view(), name="Start"),
    path('newDoctor/', views.newDoctor.as_view(), name="newDoctor"),
    path('newPatient/', views.newPatient, name="newPatient"),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    
    path('listDoctor/', views.ListDoctor.as_view(), name="listDoctor"), #Clase Vista, name="listDoctor" ->tiene que coincidir con el TP
    path('listPatient/', views.ListPatient.as_view(), name="listPatient"),

    path('getDoctorBySurname/', views.getDoctorBySurname.as_view(), name="AS"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
    #path('deleteDoctor/<int:pk>', views.deleteDoctor, name="deleteDoctor"), #Eliminamos 
]