from django.shortcuts import render, redirect
from .models import PatientInsurance
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    # Render a template or return a response for the index page
    return render(request, 'patientinsurance/index.html')

def add_insurance(request):
    # Logic to add insurance
    return render(request, 'patientinsurance/add.html')

def edit_insurance(request, id):
    # Logic to edit insurance
    return render(request, 'patientinsurance/edit.html')

def delete_insurance(request, id):
    # Logic to delete insurance
    return render(request, 'patientinsurance/delete.html')
 
class IndexView(generic.TemplateView):
    template_name = 'patientinsurance/index.html'

@csrf_exempt
def saveInsurInfo(request):
    if request.method == 'POST':
        insurance = PatientInsurance(
            user_name=request.session.get('member_id'),
            insurance_provider=request.POST.get('insurComp'),
            policy_number=request.POST.get('insurPolicyNum'),
            coverage_details=request.POST.get('dependents')
        )
        insurance.save()
        return redirect('patientinsurance:index')  # Redirect to the index page after saving
    return render(request, 'patientinsurance/index.html')  # Render the index page if not POST

@csrf_exempt
def saveExInsurInfo(request):
    pi = PatientInsurance(
        user_name = request.session.get('member_id'),
        first_name = request.POST['firstNameEx'],
        last_name = request.POST['lastNameEx'],
        initial = request.POST['initialEx'],
        relationToPatient = request.POST['relationToPatientEx'],
        dob = request.POST['birthdateEx'],
        socSec = request.POST['socSecNumEx'],
        address = request.POST['addressEx'],
        city = request.POST['cityEx'],
        state = request.POST['stateEx'],
        zip = request.POST['zipEx'],
        homephone = request.POST['homePhoneEx'],
        cellphone = request.POST['cellPhoneEx'],
        email = request.POST['emailEx'],
        employerName = request.POST['employerEx'],
        employerOccupation = request.POST['employerOccuEx'],
        employerBusAddr = request.POST['employerBusAddrEx'],
        employerBusPhone = request.POST['employerBusPhoneEx'],
        employerBusEmail = request.POST['employerBusEmailEx'],
        insurComp = request.POST['insurCompEx'],
        insurCompPhone = request.POST['insurCompPhoneEx'],
        insurContNum = request.POST['insurCompContEx'],
        insurGroupNum = request.POST['insurGroupNumEx'],
        insurSubscNum = request.POST['insurPolicyNumEx'],
        dependentName = request.POST['dependentsEx'])
    pi.save()
    
class ModifyView(generic.TemplateView):
    template_name = 'patientinsurance/modify.html'

class Modify2View(generic.TemplateView):
    template_name = 'patientinsurance/modify2.html'
    
def readData(request):
    if request.session.get('member_id'):
        insinfo = PatientInsurance.objects.all() \
            .filter(user_name__exact = request.session.get('member_id')).values();
        if insinfo.count() == 0:
            return render(request, "patientinsurance/index.html");
        else:
            if insinfo.count() == 1:
                return render(request, "patientinsurance/modify.html", {"insinfo_list": insinfo,})
            else: 
                return render(request, "patientinsurance/modify2.html", 
                              {"insinfo_list": [{"ins1": insinfo[0], 
                                                 "ins2": insinfo[1]}],})
    return render(request, "login/index.html")

@csrf_exempt
def modifyInsurInfo(request):
    if request.session.get('member_id'):
        pi = PatientInsurance.objects.all() \
            .filter(user_name__exact = request.session.get('member_id')).values();
        if pi.count() == 2:
            pi0 = PatientInsurance.objects.get(pk=request.POST['pkPrimary'])
            pi0.first_name = request.POST['firstName']
            pi0.last_name = request.POST['lastName']
            pi0.initial = request.POST['initial']
            pi0.relationToPatient = request.POST['relationToPatient']
            pi0.dob = request.POST['birthdate']
            pi0.socSec = request.POST['socSecNum']
            pi0.address = request.POST['address']
            pi0.city = request.POST['city']
            pi0.state = request.POST['state']
            pi0.zip = request.POST['zip']
            pi0.homephone = request.POST['homePhone']
            pi0.cellphone = request.POST['cellPhone']
            pi0.email = request.POST['email']
            pi0.employerName = request.POST['employer']
            pi0.employerOccupation = request.POST['employerOccu']
            pi0.employerBusAddr = request.POST['employerBusAddr']
            pi0.employerBusPhone = request.POST['employerBusPhone']
            pi0.employerBusEmail = request.POST['employerBusEmail']
            pi0.insurComp = request.POST['insurComp']
            pi0.insurCompPhone = request.POST['insurCompPhone']
            pi0.insurContNum = request.POST['insurCompCont']
            pi0.insurGroupNum = request.POST['insurGroupNum']
            pi0.insurSubscNum = request.POST['insurPolicyNum']
            pi0.dependentName = request.POST['dependents']
            pi0.save()

            pi1 = PatientInsurance.objects.get(pk=request.POST['pkAdditional'])
            pi1.first_name = request.POST['firstNameEx']
            pi1.last_name = request.POST['lastNameEx']
            pi1.initial = request.POST['initialEx']
            pi1.relationToPatient = request.POST['relationToPatientEx']
            pi1.dob = request.POST['birthdateEx']
            pi1.socSec = request.POST['socSecNumEx']
            pi1.address = request.POST['addressEx']
            pi1.city = request.POST['cityEx']
            pi1.state = request.POST['stateEx']
            pi1.zip = request.POST['zipEx']
            pi1.homephone = request.POST['homePhoneEx']
            pi1.cellphone = request.POST['cellPhoneEx']
            pi1.email = request.POST['emailEx']
            pi1.employerName = request.POST['employerEx']
            pi1.employerOccupation = request.POST['employerOccuEx']
            pi1.employerBusAddr = request.POST['employerBusAddrEx']
            pi1.employerBusPhone = request.POST['employerBusPhoneEx']
            pi1.employerBusEmail = request.POST['employerBusEmailEx']
            pi1.insurComp = request.POST['insurCompEx']
            pi1.insurCompPhone = request.POST['insurCompPhoneEx']
            pi1.insurContNum = request.POST['insurCompContEx']
            pi1.insurGroupNum = request.POST['insurGroupNumEx']
            pi1.insurSubscNum = request.POST['insurPolicyNumEx']
            pi1.dependentName = request.POST['dependentsEx']
            pi1.save()
            return render(request, "dashboard/index.html")
        else:
            pi0 = PatientInsurance.objects.get(pk=request.POST['pkPrimary'])
            pi0.first_name = request.POST['firstName']
            pi0.last_name = request.POST['lastName']
            pi0.initial = request.POST['initial']
            pi0.relationToPatient = request.POST['relationToPatient']
            pi0.dob = request.POST['birthdate']
            pi0.socSec = request.POST['socSecNum']
            pi0.address = request.POST['address']
            pi0.city = request.POST['city']
            pi0.state = request.POST['state']
            pi0.zip = request.POST['zip']
            pi0.homephone = request.POST['homePhone']
            pi0.cellphone = request.POST['cellPhone']
            pi0.email = request.POST['email']
            pi0.employerName = request.POST['employer']
            pi0.employerOccupation = request.POST['employerOccu']
            pi0.employerBusAddr = request.POST['employerBusAddr']
            pi0.employerBusPhone = request.POST['employerBusPhone']
            pi0.employerBusEmail = request.POST['employerBusEmail']
            pi0.insurComp = request.POST['insurComp']
            pi0.insurCompPhone = request.POST['insurCompPhone']
            pi0.insurContNum = request.POST['insurCompCont']
            pi0.insurGroupNum = request.POST['insurGroupNum']
            pi0.insurSubscNum = request.POST['insurPolicyNum']
            pi0.dependentName = request.POST['dependents']
            pi0.save()
            
            if request.POST['exInsurInfoYes'] == "yes":
                saveExInsurInfo(request)
            return render(request, "dashboard/index.html")
    return render(request, "login/index.html")

@csrf_exempt
def deleteInsurInfo(request):
    if request.session.get('member_id'):
        pi = PatientInsurance.objects.all() \
            .filter(user_name__exact = request.session.get('member_id')).values();
        if pi.count() == 2:
            pi0 = PatientInsurance.objects.get(pk=request.POST['pkPrimary'])
            pi0.delete()

            pi1 = PatientInsurance.objects.get(pk=request.POST['pkAdditional'])
            pi1.delete()
        else:
            pi0 = PatientInsurance.objects.get(pk=request.POST['pkPrimary'])
            pi0.delete()

        return render(request, "dashboard/index.html")
    return render(request, "login/index.html")

def readInsuranceInfo(request):
    if request.session.get('member_id'):
        insinfo = PatientInsurance.objects.all() \
            .filter(user_name__exact=request.session.get('member_id')).values()
        if insinfo.count() == 1:
            return render(request, "patientinsurance/modify.html", {"insinfo_list": insinfo,})
        elif insinfo.count() > 1:
            return render(request, "patientinsurance/modify2.html", 
                          {"insinfo_list": [{"ins1": insinfo[0], 
                                             "ins2": insinfo[1]}],})
        else:
            return render(request, "patientinsurance/index.html")
    return render(request, "login/index.html")  
# The above function reads the additional insurance information if it exists

@csrf_exempt  # Use cautiously; ensure security measures are in place
def api_handler(request):
    if request.method == 'POST':
        # Handle POST requests
        # ...existing logic...
        return JsonResponse({'message': 'POST request handled successfully'})
    elif request.method == 'DELETE':
        # Handle DELETE requests
        resource_id = request.POST.get('id')  # Ensure 'id' is passed in the request
        if not resource_id:
            return JsonResponse({'error': 'Resource ID is missing'}, status=400)
        try:
            # Logic to delete the resource
            # Example: PatientInsurance.objects.get(pk=resource_id).delete()
            return JsonResponse({'message': 'Resource deleted successfully'})
        except PatientInsurance.DoesNotExist:
            return JsonResponse({'error': 'Resource not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

