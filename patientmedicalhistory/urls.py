from django.urls import path
from . import views

app_name = 'patientmedicalhistory'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_medical_history, name='add_medical_history'),
    path('edit/<int:id>/', views.edit_medical_history, name='edit_medical_history'),
    path('delete/<int:id>/', views.delete_medical_history, name='delete_medical_history'),
    path('save/', views.saveMedHistoryInfo, name='saveMedHistoryInfo'),
]