"""
Definition of urls for EMR.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('login.urls')),
    path('patientcontact/', include('patientcontact.urls')),
    path('patientmedicalhistory/', include('patientmedicalhistory.urls')),
    path('patientinsurance/', include('patientinsurance.urls')),
    path('patientmeds/', include('patientmeds.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
