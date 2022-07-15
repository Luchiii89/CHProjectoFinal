from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppCoder.models import Patient, Department, Doctor, History
from AppCoder.forms import PatientForm

# Create your views here.

# def book(request):
#     book = Book(title="El Hobbit", genre="Fantasy novel", author="J. R. R. Tolkien", year=1937)
#     book.save()
#     txtDocument = f"---> Título: {book.title}  Género: {book.genre}  Autor: {book.author}  Año: {book.year}  "
#     return HttpResponse(txtDocument)


def start(request):
    return render(request, "AppCoder/start.html")


# def patients(request):
#     return render(request, "AppCoder/patients.html")


# def doctors(request):
#     return render(request, "AppCoder/doctors.html")


# def departments(request):
#     return render(request, "AppCoder/departments.html")


# def histories(request):
#     return render(request, "AppCoder/histories.html")


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