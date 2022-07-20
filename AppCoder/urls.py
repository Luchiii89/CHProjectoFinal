from django.urls import path
from django.views import View
from AppCoder import views
from AppCoder.views import *


urlpatterns = [
   
    path('', views.start, name="Start"),
    path('newDoctor/', views.newDoctor, name="newDoctor"),
    path('newPatient/', views.newPatient, name="newPatient"),
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
    path('listDoctor/', views.listDoctor, name="listDoctor"),
    path('listPatient/', views.listPatient, name="listPatient"),
    path('getDoctorBySurname/', views.getDoctorBySurname, name="AS"),
    path('getDoctor/', views.getDoctor, name="getDoctor"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
    # path('deleteDoctor/<int:pk>', views.deleteDoctor, name="deleteDoctor"), #Eliminamos 
]