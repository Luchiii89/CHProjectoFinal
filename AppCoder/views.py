from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView, View, TemplateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

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
    
class ListDoctor(ListView):
    model = Doctor
    context_object_name = 'surname'
    template_name = "AppCoder/listDoctor.html"
    queryset = Doctor.objects.filter(surname__icontains='surname')

    # def get(self, request, *args, **kwargs) -> HttpResponse:
    #     listDoctor = Doctor.objects.all()
    #     return render(request, self.template_name, {"listDoctor":listDoctor})

class newDoctor(CreateView):
    model = Doctor
    template_name = "AppCoder/newDoctor.html"
    fields = ['name', 'surname', 'genre', 'docId', 'license', 'mail', 'tel', 'address', 'specialization']
    
class newPatient(CreateView):
    template_name = "AppCoder/newPatient.html"


def newDoctor(request):
    if request.method == 'POST':
        miFormulario = DoctorForm(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            doctor = Doctor(name=informacion['name'], 
                        surname=informacion['surname'], 
                        genre=informacion['genre'], 
                        docId=informacion['docId'],
                        license=informacion['license'],
                        mail=informacion['mail'],
                        tel=informacion['tel'],
                        address=informacion['address'],
                        specialization=informacion['specialization']) 
            doctor.save()
            return render(request, "AppCoder/index.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario = DoctorForm() #Formulario vacio para construir el html
    return render(request, "AppCoder/newDoctor.html", {"miFormulario":miFormulario})

def newPatient(request):
    if request.method == 'POST':
        miFormulario = PatientForm(request.POST) #aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:   #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            patient = Patient(name=informacion['name'], 
                        surname=informacion['surname'], 
                        genre=informacion['genre'], 
                        patId=informacion['patId'],
                        mail=informacion['mail'],
                        tel=informacion['tel'],
                        address=informacion['address'],)     
            patient.save()
            return render(request, "AppCoder/index.html") #Vuelvo al inicio o a donde quieran
    else: 
        miFormulario= PatientForm() #Formulario vacio para construir el html
    return render(request, "AppCoder/newPatient.html", {"miFormulario":miFormulario})

class ListPatient(ListView): #ListPatient es el que se le pasa a URL con el .as_view()
    template_name = "AppCoder/listPatient.html"
    queryset = Patient.objects.all()
    context_object_name = 'patients' # este es el nombre que le pasamos al template para iterar, en ves del 
    #object_list

class getDoctorBySurname(ListView):        #incompleto
    queryset = Doctor.objects.filter(surname__icontains='war')
    template_name = "AppCoder/getDoctor.html"

    def get(self, request, *args, **kwargs) -> HttpResponse:
        getDoctor = Doctor.objects.filter(surname__icontains='surname')
        return render(request, self.template_name, {"getDoctor":getDoctor})
     
