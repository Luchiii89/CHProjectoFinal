from pydoc import Doc
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppCoder.models import Patient, Department, Doctor, History
from AppCoder.forms import *

# Create your views here.


def start(request):
    return render(request, 'AppCoder\index.html', {})


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


def listDoctor(request): 
    context = {}
    context["doctor"] = Doctor.objects.all()
    return render(request, "AppCoder/listDoctor.html",context) 


def listPatient(request): 
    context = {}
    context["patient"] = Patient.objects.all()
    return render(request, "AppCoder/listPatient.html",context) 


def getDoctorBySurname(request):
    if  request.GET["surname"]:
        surname = request.GET['surname'] 
        doctor = Doctor.objects.filter(surname__icontains=surname)
        return render(request, "AppCoder/doctorsById.html", {"doctores":doctor, "apellido":surname})
    else: 
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
  

def getDoctor(request):
    return render(request, "AppCoder/getDoctor.html")
  
#-------------------------------------------
# def deleteDoctor(request, pk):
#     doctor = get_object_or_404(Doctor,id=pk)
#     doctor.delete()
#     return render(request,"AppCoder/listDoctor.html")
#-------------------------------------------   