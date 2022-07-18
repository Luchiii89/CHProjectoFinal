from django.views.generic import ListView
from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppCoder.models import Patient, Department, Doctor, History
from AppCoder.forms import PatientForm, DepartmentForm, DoctorForm

# Create your views here.

def start(request):
    return render(request, "AppCoder/index.html")


def patients(request):
    return render(request, "AppCoder/patients.html")


def saludo_personalizado(request):
    context = {}
    return(request, "AppCoder/index.html",context)


def doctors(request):
    return render(request, "AppCoder/doctors.html")


def departments(request):
    return render(request, "AppCoder/departments.html")


def histories(request):
    return render(request, "AppCoder/histories.html")


# def patient(request):
#     patient = Patient(title="El Hobbit", genre="Fantasy novel", author="J. R. R. Tolkien", year=1937)
#     patient.save()
#     txtDocument = f"---> Título: {book.title}  Género: {book.genre}  Autor: {book.author}  Año: {book.year}  "
#     return HttpResponse(txtDocument)

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

def buscar_paciente(request):

    if  request.GET["name"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        name = request.GET['name'] 
        patient = Patient.objects.filter(name__icontains=name)

        return render(request, "AppCoder/inicio.html", {"paciente":name, "surname":surname})

    else: 

        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

class ListadoPacientesListView(ListView):
	model = Patient
	template_name = 'totalPacientes.html'