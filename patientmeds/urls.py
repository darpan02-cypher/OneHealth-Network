from django.urls import path
from . import views
from .api_views import patient_meds_api
from .views import Meds

app_name = 'patientmeds'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_medication, name='add_medication'),
    path('edit/<int:id>/', views.edit_medication, name='edit_medication'),
    path('delete/<int:id>/', views.delete_medication, name='delete_medication'),
    path('api/', Meds.as_view(), name='meds_api'),  # Ensure trailing slash
]