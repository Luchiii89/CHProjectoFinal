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
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)        
        if form.is_valid():
            data = form.cleaned_data
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/index.html',{'mensaje':f'Bienvenido - {usuario}'})
            else:
                return render(request, 'AppCoder/login_error.html',{'mensaje':f'Error Acceso Denegado'})
        else:
            return render(request, 'AppCoder/login_error.html',{'mensaje':'Error Formulario Erróneo'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppCoder/login.html',{'form':form})


def logout_request(request):
    logout(request)
    return redirect("inicio")
  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()     
    return render(request,"AppCoder/register.html" ,  {"form":form})


class UserProfile(DetailView):
    model = User
    template_name = "AppCoder/profile.html"
    

@method_decorator(login_required, name='dispatch')
class EditProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "AppCoder/edit_profile.html" #chequear y posiblemente mejorar o corregir
    fields = ["username", "email", "first_name", "last_name"]
    # success_url = reverse_lazy('listPatient')

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.id})

    
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES) 
        if miFormulario.is_valid(): 
                u = User.objects.get(username=request.user)
                avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                avatar.save()
                return render(request, "AppCoder/index.html") 
    else: 
        miFormulario= AvatarFormulario()
    return render(request, "AppCoder/add_avatar.html", {"miFormulario":miFormulario})


#INICIO
@login_required
def Index(request):
    return render(request, "AppCoder/index.html")


class OurServices(TemplateView):
    template_name = "AppCoder\our_services.html"
    

class About(TemplateView):
    template_name = "AppCoder\\about.html"
    

# CREAR
class NewDoctor(LoginRequiredMixin, CreateView):
    model = Doctor
    template_name = "AppCoder/new_doctor.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']

   
class NewPatient(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "AppCoder/new_patient.html"
    fields = ['name', 'surname', 'genre', 'DNI', 'mail', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']


class NewDepartment(LoginRequiredMixin, CreateView):
    model = Department
    template_name = "AppCoder/new_department.html"
    fields = ['name', 'mail', 'tel', 'head_of']


class NewHistory(LoginRequiredMixin, CreateView):
    model = History
    template_name = "AppCoder/new_history.html"
    fields = ['date', 'patient', 'doctor', 'comments']
    

#DETALLE
class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "AppCoder/doctor_detail.html" 

    
class PatientDetailView(DetailView):
    model = Patient
    template_name = "AppCoder/patient_detail.html"


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "AppCoder/department_detail.html"


class HistoryDetailView(DetailView):
    model = History
    template_name = "AppCoder/history_detail.html"   


# LISTAR
class ListDoctor(ListView):
    model = Doctor
    template_name = "AppCoder/list_doctor.html"
    queryset = Doctor.objects.all()
    context_object_name = 'doctors' 
    ordering = ['surname']


class ListPatient(ListView):
    model = Patient
    template_name = "AppCoder/list_patient.html"
    queryset = Patient.objects.all()
    context_object_name = 'patients' 
    ordering = ['surname']


class ListDepartment(ListView):
    model = Department
    template_name = "AppCoder/list_department.html"
    queryset = Department.objects.all()
    context_object_name = 'departments' 
    ordering = ['name']


class ListHistory(ListView):
    model = History
    template_name = "AppCoder/list_history.html"
    queryset = History.objects.all()
    context_object_name = 'histories' 
    ordering = ['nro']


#BUSCAR
class GetDoctorBySurname(ListView):
    model = Doctor
    template_name = "AppCoder/get_doctor.html"
    
    def get(self, request, *args, **kwargs) -> HttpResponse:
       getDoctor = Doctor.objects.filter(surname__icontains='surname')
       return render(request, self.template_name, {"getDoctor":getDoctor})


def getDoctorBySurname(request):
    return render(request, 'AppCoder/get_doctor.html')


def getDoctor(request):
    if  request.GET["surname"]:
        surname = request.GET['surname'] 
        doctores = Doctor.objects.filter(surname__icontains=surname)
        return render(request, "AppCoder/index.html", {"doctores":doctores, "surname":surname})
    else: 
        respuesta = "No enviaste datos"
    return render(request, "AppCoder/index.html", {"respuesta":respuesta})
  
  
#ELIMINAR
class DeleteDoctor(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = "AppCoder/delete_doctor.html"
    success_url = reverse_lazy('listDoctor')


class DeletePatient(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "AppCoder/delete_patient.html"
    success_url = reverse_lazy('listPatient')


class DeleteDepartment(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = "AppCoder/delete_department.html"
    success_url = reverse_lazy('listDepartment')


class DeleteHistory(LoginRequiredMixin, DeleteView):
    model = History
    template_name = "AppCoder/delete_history.html"
    success_url = reverse_lazy('listHistory')
    

#EDITAR
class UpdateDoctor(LoginRequiredMixin, UpdateView):
    model = Doctor
    fields = ['name', 'surname', 'genre', 'DNI', 'license', 'mail', 'tel', 'address', 'department']
    template_name = "AppCoder/new_doctor.html"
    success_url = reverse_lazy('listDoctor')


class UpdatePatient(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['name', 'surname', 'genre', 'DNI', 'register_date','birth_date', 'photo', 'personal_files', 'mail', 'tel', 'address']
    template_name = "AppCoder/new_patient.html"
    success_url = reverse_lazy('listPatient')


class UpdateDepartment(LoginRequiredMixin, UpdateView):
    model = Department
    fields = ['name','mail', 'tel', 'head_of']
    template_name = "AppCoder/new_department.html"
    success_url = reverse_lazy('listDepartment')


class UpdateHistory(LoginRequiredMixin, UpdateView):
    model = History
    fields = ['comments']
    template_name = "AppCoder/new_history.html"
    success_url = reverse_lazy('listHistory')
    