from pydoc import Doc
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppCoder.models import Patient, Department, Doctor, History
from AppCoder.forms import *

# Create your views here.

# def book(request):
#     book = Book(title="El Hobbit", genre="Fantasy novel", author="J. R. R. Tolkien", year=1937)
#     book.save()
#     txtDocument = f"---> Título: {book.title}  Género: {book.genre}  Autor: {book.author}  Año: {book.year}  "
#     return HttpResponse(txtDocument)


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

        miFormulario= DoctorForm() #Formulario vacio para construir el html

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

#-------------------------------------------
def deleteDoctor(request, pk):
    doctor = get_object_or_404(Doctor,id=pk)
    doctor.delete()
    return render(request,"AppCoder/listDoctor.html")
#-------------------------------------------   
  

# def newBook(request):
#     if request.method == 'POST':
#         newForm = BookForm(request.POST) 
#         print(newForm)
#         if newForm.is_valid:   
#             data = newForm.cleaned_data
#             book = Book(title=data['title'], genre=data['genre'], author=data['author'], year=data['year']) 
#             book.save()
#             return render(request, "AppCoder/start.html")
#     else: 
#         newForm = BookForm() 
#     return render(request, "AppCoder/books.html", {"BookForm":BookForm})


# def newAuthor(request):
#     if request.method == 'POST':
#         newForm = AuthorForm(request.POST) 
#         print(newForm)
#         if newForm.is_valid:   
#             data = newForm.cleaned_data
#             author = Author(name=data['name'], surname=data['surname'],
#             country=data['country'], email=data['email']) 
#             author.save()
#             return render(request, "AppCoder/start.html") 
#     else: 
#         newForm = AuthorForm() 
#     return render(request, "AppCoder/profesores.html", {"AuthorForm":newForm})


# def getBookByGenre(request): falta probar
#     if request.GET["genre"]:
#         genre = request.GET['genre'] 
#         books = Book.objects.filter(genre__icontains=genre)
#         return render(request, "AppCoder/start.html", {"books":books, "genre":genre})
#     else: 
#         respuesta = "No enviaste datos"
#     return HttpResponse(respuesta)