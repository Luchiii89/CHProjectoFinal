from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View, TemplateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView

from multiprocessing import context
from pydoc import Doc
from numpy import result_type
from yaml import DocumentStartToken

from AppCoder import models
from AppCoder.models import Patient, Department, Doctor, History
from AppCoder.forms import *



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
    form= AuthenticationForm()
    return render(request, 'AppCoder/login.html',{'form':form})

class Start(TemplateView):
    template_name = "AppCoder\index.html"
    
    
# CREAR
class newDoctor(CreateView):
    model = Doctor
    template_name = "AppCoder/newDoctor.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']
    
class newPatient(CreateView):
    model = Patient
    template_name = "AppCoder/newPatient.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'mail', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']

# LISTAR
class ListDoctor(ListView):
    model = Doctor
    template_name = "AppCoder/listDoctor.html"
    queryset = Doctor.objects.all()
    model = Doctor

    #queryset = Doctor.objects.filter(surname__icontains='surname')
    
    # def get(self, request, *args, **kwargs) -> HttpResponse:
    #     listDoctor = Doctor.objects.all()
    #     return render(request, self.template_name, {"listDoctor":listDoctor})
class ListPatient(ListView):
    model = Patient#ListPatient es el que se le pasa a URL con el .as_view()
    template_name = "AppCoder/listPatient.html"
    queryset = Patient.objects.all()
    context_object_name = 'patients' # este es el nombre que le pasamos al template para iterar, en ves del 
    #object_list

#BUSCAR
class getDoctorBySurname(ListView):
    model = Doctor
    template_name = "AppCoder/getDoctor.html"
    queryset = Doctor.objects.all()

    #def get(self, request, *args, **kwargs) -> HttpResponse:
    #    getDoctor = Doctor.objects.filter(surname__icontains='surname')
    #    return render(request, self.template_name, {"getDoctor":getDoctor})

#ELIMINAR
class deleteDoctor(DeleteView):
    model = Doctor#ListPatient es el que se le pasa a URL con el .as_view()
    template_name = "AppCoder/deleteDoctor.html"
    success_url = reverse_lazy('listDoctor')


class deletePatient(DeleteView):
    model = Patient#ListPatient es el que se le pasa a URL con el .as_view()
    template_name = "AppCoder/deletepatient.html"
    success_url = reverse_lazy('listPatient')

#EDITAR
class updateDoctor(UpdateView):
    model = Doctor
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']
    template_name = "AppCoder/newDoctor.html"
    success_url = reverse_lazy('listDoctor')

class updatePatient(UpdateView):
    model = Patient
    fields = ['name', 'surname', 'genre', 'DNI', 'mail', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']
    template_name = "AppCoder/newPatient.html"
    success_url = reverse_lazy('listPatient')