from django import forms


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
    
    