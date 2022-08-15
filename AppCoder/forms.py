from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    birth_date = forms.DateInput()
    DNI = forms.IntegerField()
    genre = forms.CharField(max_length=60)
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)
    mail = forms.EmailField()
    photo = forms.FileField()
    personal_files = forms.FileField()
    register_date = forms.DateField()


class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=40)
    head_of = forms.CharField(max_length=60)
    tel = forms.IntegerField()
    mail = forms.EmailField()


class DoctorForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    DNI = forms.IntegerField()
    genre = forms.CharField(max_length=60)
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)
    mail = forms.EmailField()
    license = forms.CharField(max_length=20)
    department = forms.CharField(max_length=40)


class HistoryForm(forms.Form):
    date = forms.DateInput()
    patient = forms.CharField(max_length=60)
    doctor = forms.CharField(max_length=60)
    comments = forms.TextInput()


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="E-mail")
    username = forms.CharField(label="Usuario")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput) 
    imagen_avatar = forms.ImageField(required=False,label="Foto de perfil")
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
    
    