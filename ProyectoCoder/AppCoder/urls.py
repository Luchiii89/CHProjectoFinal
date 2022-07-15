from django.urls import path
from AppCoder import views


urlpatterns = [
   
    path('', views.start, name="Start"),
    # path('patients', views.patients, name="patients"),
    # path('doctors', views.doctors, name="doctors"),
    # path('departments', views.departments, name="departments"),
    # path('histories', views.histories, name="histories"),
]