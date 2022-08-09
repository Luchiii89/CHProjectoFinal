from django.contrib import admin
from  .models import *

# Register your models here.

admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Department)

admin.site.register(History)

# Crear el usuario para administrar, lo que se llama un super usuario:
# python manage.py createsuperuser
# Ingresamos a /admin/ y probamos el super usuario: