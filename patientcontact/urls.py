from django.urls import path
from . import views

app_name = 'patientcontact'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('read/', views.readContactInfo, name='readContactInfo'),
    path('update/', views.updateContactInfo, name='updateContactInfo'),
    #path('read/', views.read_contact, name='read_contact')


    

]