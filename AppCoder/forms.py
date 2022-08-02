from django import forms


class PatientForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    birth_date = forms.DateInput()
    genre = forms.CharField(max_length=60)
    DNI = forms.IntegerField()
    mail = forms.EmailField()
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)
    register_date = forms.DateField()
    photo = forms.FileField()
    personal_files = forms.FileField()


class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=40)
    mail = forms.EmailField()
    tel = forms.IntegerField()
    head_of = forms.CharField(max_length=60)


class DoctorForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    genre = forms.CharField(max_length=60)
    DNI = forms.IntegerField()
    license = forms.CharField(max_length=20)
    mail = forms.EmailField()
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)
    department = forms.CharField(max_length=40)


# class HistoryForm(forms.Form):
#     patient = Patient.name
#     doctor = Doctor.name
#     numId = models.IntegerField()
    
    