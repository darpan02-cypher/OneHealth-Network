from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404

from simple_rest import Resource

from .models import PatientMeds, PatientMedication

def index(request):
    if request.session.get('member_id'):
        return render(request, "patientmeds/index.html")
    else:
        return render(request, "login/index.html")

def add_medication(request):
    if request.method == 'POST':
        # Save the new medication information
        medication = PatientMedication(
            user_name=request.session.get('member_id'),
            medication_name=request.POST['medicationName'],
            dosage=request.POST['dosage'],
            frequency=request.POST['frequency'],
            start_date=request.POST['startDate'],
            end_date=request.POST['endDate'],
            prescribing_doctor=request.POST['prescribingDoctor']
        )
        medication.save()
        return redirect('patientmeds:index')  # Redirect to the index page after saving
    return render(request, 'patientmeds/add.html')  # Render the add medication form

def edit_medication(request, id):
    # Fetch the medication to edit
    medication = get_object_or_404(PatientMedication, id=id)
    if request.method == 'POST':
        # Update the medication information
        medication.medication_name = request.POST['medicationName']
        medication.dosage = request.POST['dosage']
        medication.frequency = request.POST['frequency']
        medication.start_date = request.POST['startDate']
        medication.end_date = request.POST['endDate']
        medication.prescribing_doctor = request.POST['prescribingDoctor']
        medication.save()
        return redirect('patientmeds:index')  # Redirect to the index page after saving
    return render(request, 'patientmeds/edit.html', {'medication': medication})  # Render the edit form

def delete_medication(request, id):
    # Fetch the medication to delete
    medication = get_object_or_404(PatientMedication, id=id)
    if request.method == 'POST':
        # Delete the medication
        medication.delete()
        return redirect('patientmeds:index')  # Redirect to the index page after deletion
    return render(request, 'patientmeds/delete.html', {'medication': medication})  # Render the delete confirmation page

def medsapi(request):
    if request.method == 'GET':
        # Fetch all medications from the database
        meds = PatientMedication.objects.all().values()
        return JsonResponse(list(meds), safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

class Meds(Resource):

    def get(self, request):
        if request.session.get('member_id'):
            meds = PatientMeds.objects.all() \
                .filter(user_name__exact = request.session.get('member_id'));       
            return HttpResponse(self.to_json(meds), content_type = "application/json", status = 200)
        else:
            return render(request, "login/index.html")

    def post(self, request):
        if request.session.get('member_id'):
            meds = PatientMeds(
                user_name = request.session.get('member_id'),
                meds_name = request.POST.get("meds_name"),
                meds_strength = request.POST.get("meds_strength"),
                meds_dir = request.POST.get("meds_dir"),
                meds_status = request.POST.get("meds_status"),
                meds_date = request.POST.get("meds_date")
            )
            meds.save()
            meds = PatientMeds.objects.all() \
                .filter(meds_name__contains = request.POST.get("meds_name")); 
            return HttpResponse(self.to_json(meds), content_type = "application/json", status = 201)
        else:
            return render(request, "login/index.html")

    def put(self, request, patientmeds_id):
        if request.session.get('member_id'):
            meds = PatientMeds.objects.get(pk = patientmeds_id, user_name=request.session.get('member_id'))  
            meds.meds_name = request.PUT.get("meds_name")
            meds.meds_strength = request.PUT.get("meds_strength")
            meds.meds_dir = request.PUT.get("meds_dir")
            meds.meds_status = request.PUT.get("meds_status")
            meds.meds_date = request.PUT.get("meds_date")
            meds.save()
            return HttpResponse(status = 200)
        else:
            return render(request, "login/index.html")

    def delete(self, request, patientmeds_id):
        meds = PatientMeds.objects.get(pk = patientmeds_id)
        meds.delete()
        return HttpResponse(status = 200)

    def to_json(self, objects):
        return serializers.serialize("json", objects)