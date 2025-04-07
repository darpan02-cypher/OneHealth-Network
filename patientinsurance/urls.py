from django.urls import path
from . import views

app_name = 'patientinsurance'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_insurance, name='add_insurance'),
    path('edit/<int:id>/', views.edit_insurance, name='edit_insurance'),
    path('delete/<int:id>/', views.delete_insurance, name='delete_insurance'),
    path('save/', views.saveInsurInfo, name='saveInsurInfo'),
    #path('read/', views.readData, name='readData')
    
]