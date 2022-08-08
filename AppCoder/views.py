from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, TemplateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from multiprocessing import context
from pydoc import Doc
from numpy import result_type
from yaml import DocumentStartToken

#Modelos, formularios
from AppCoder.models import *
from AppCoder.forms import *

#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Decorador por defecto
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_request(request):
    if(request.method == "POST"):
        form = AuthenticationForm(request, data = request.POST)        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if(user is not None):
                login(request, user)
                return render(request, 'AppCoder/index.html',{'mensaje':f'Bienvenido - {usuario}'})
            else:
                return render(request, 'AppCoder/index.html',{'mensaje':f'Erro Acceso Denegado'})
        else:
            return render(request, 'AppCoder/index.html',{'mensaje':'Erro Formulario Erroneo'})
    form = AuthenticationForm()
    return render(request, 'AppCoder/login.html',{'form':form})

#INICIO
class Index(TemplateView):
    template_name = "AppCoder\index.html"

class OurServices(TemplateView):
    template_name = "AppCoder\ourServices.html"
    
# CREAR
class NewDoctor(CreateView):
    model = Doctor
    template_name = "AppCoder/newDoctor.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']

   
class NewPatient(CreateView):
    model = Patient
    template_name = "AppCoder/newPatient.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'mail', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']


#DETALLE
class DoctorDetailView(DetailView):
      model = Patient
      template_name = "AppCoder/doctorDetail.html" 

    
class PatientDetailView(DetailView):
      model = Doctor
      template_name = "AppCoder/patientDetail.html"


class DepartmentDetailView(DetailView):
      model = Department
      template_name = "AppCoder/departmentDetail.html"
      

# LISTAR
class ListDoctor(ListView):
    model = Doctor
    template_name = "AppCoder/listDoctor.html"
    queryset = Doctor.objects.all()
    context_object_name = 'doctors' 
    ordering = ['surname']


class ListPatient(ListView):
    model = Patient
    template_name = "AppCoder/listPatient.html"
    queryset = Patient.objects.all()
    context_object_name = 'patients' 
    ordering = ['surname']


class ListDepartment(ListView):
    model = Department
    template_name = "AppCoder/listDepartment.html"
    queryset = Department.objects.all()
    context_object_name = 'departments' 
    ordering = ['name']
    

#BUSCAR
class GetDoctorBySurname(ListView):
    model = Doctor
    template_name = "AppCoder/getDoctor.html"
    
    def get(self, request, *args, **kwargs) -> HttpResponse:
       getDoctor = Doctor.objects.filter(surname__icontains='surname')
       return render(request, self.template_name, {"getDoctor":getDoctor})

  
#ELIMINAR
class DeleteDoctor(DeleteView):
    model = Doctor
    template_name = "AppCoder/deleteDoctor.html"
    success_url = reverse_lazy('listDoctor')


class DeletePatient(DeleteView):
    model = Patient
    template_name = "AppCoder/deletePatient.html"
    success_url = reverse_lazy('listPatient')


class DeleteDepartment(DeleteView):
    model = Department
    template_name = "AppCoder/deleteDepartment.html"
    success_url = reverse_lazy('listDepartment')
    

#EDITAR
class UpdateDoctor(UpdateView):
    model = Doctor
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']
    template_name = "AppCoder/newDoctor.html"
    success_url = reverse_lazy('listDoctor')


class UpdatePatient(UpdateView):
    model = Patient
    fields = ['name', 'surname', 'genre', 'DNI', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']
    template_name = "AppCoder/newPatient.html"
    success_url = reverse_lazy('listPatient')


class UpdateDepartment(UpdateView):
    model = Department
    fields = ['mail', 'tel', 'head_of']
    template_name = "AppCoder/newDepartment.html"
    success_url = reverse_lazy('listDepartment')