from django.urls import path
from django.views import View
from AppCoder import views
from AppCoder.views import *


urlpatterns = [
   
    path('', views.start, name="Start"),
    # path('patients', views.patients, name="patients"),
    path('newDoctor/', views.newDoctor, name="newDoctor"),
    path('listDoctor/', views.listDoctor, name="listDoctor"),
    path('listPatient/', views.listPatient, name="listPatient"),
    # path('departments', views.departments, name="departments"),
    # path('histories', views.histories, name="histories"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
]