from django.urls import path
from django.conf.urls import include, url
from AppCoder import views


urlpatterns = [
   
    path('', views.start, name="start"),
    path('patients', views.patients, name="patients"),
    path('saludo-personalizado', views.saludo_personalizado, name="saludo"),
    # path('doctors', views.doctors, name="doctors"),
    # path('departments', views.departments, name="departments"),
    # path('histories', views.histories, name="histories"),
    path('buscar/', views.buscar_paciente),
    url('pacientes', views.ListadoPacientesListView.as_view(), name='listadoPacientes'),
]

# urlpatterns = [
   
#     path('', views.inicio, name="Inicio"), #esta era nuestra primer view
#     path('cursos', views.cursos, name="Cursos"),
#     path('profesores', views.profesores, name="Profesores"),
#     path('estudiantes', views.estudiantes, name="Estudiantes"),
#     path('entregables', views.entregables, name="Entregables"),
#     #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
#     #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
#     #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
#     path('buscar/', views.buscar),
   
# ]