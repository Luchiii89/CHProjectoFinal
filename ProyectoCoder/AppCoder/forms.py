from django import forms


class PatientForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    genre = forms.CharField(max_length=60)
    patId = forms.IntegerField()
    mail = forms.EmailField()
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)


class DepartmentForm(forms.Form):
    depId = forms.IntegerField()
    name = forms.CharField(max_length=40)
    mail = forms.EmailField()
    tel = forms.IntegerField()
    head = forms.CharField(max_length=60)


class DoctorForm(forms.Form):
    name = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=60)
    genre = forms.CharField(max_length=60)
    docId = forms.IntegerField()
    license = forms.CharField(max_length=20)
    mail = forms.EmailField()
    tel = forms.IntegerField()
    address = forms.CharField(max_length=60)
    specialization = forms.CharField(max_length=40)
    # department = Department.name


# class HistoryForm(forms.Form):
#     patient = Patient.name
#     doctor = Doctor.name
#     numId = models.IntegerField()
    
    