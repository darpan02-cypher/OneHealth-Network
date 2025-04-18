from django.db import models

# Create your models here.
class PatientMeds(models.Model):
    user_name = models.CharField(max_length=20, default='larryxu')
    meds_name = models.CharField(max_length=50, default='Oxi')
    meds_strength = models.CharField(max_length=30, default='40 mg p.o.')
    meds_dir = models.CharField(max_length=20, default='daily')
    meds_status = models.CharField(max_length=20, default='active')
    meds_date = models.CharField(max_length=20, default='now')

class PatientMedication(models.Model):
    user_name = models.CharField(max_length=255)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    prescribing_doctor = models.CharField(max_length=255)

    def __str__(self):
        return self.medication_name