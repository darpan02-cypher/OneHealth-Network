from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import PatientContact
 
class IndexView(generic.TemplateView):
    template_name = 'patientcontact/index.html'

def index(request):
    # Render a template or return a response for the index page
    return render(request, 'patientcontact/index.html')

def populate_patient_contact(pc, request):
    pc.user_name = request.session.get('member_id')
    pc.first_name = request.POST['contFirstName']
    pc.middle_name = request.POST['contMiddleName']
    pc.last_name = request.POST['contLastName']
    pc.address = request.POST['contAddress']
    pc.city = request.POST['contCity']
    pc.state = request.POST['contState']
    pc.zipCode = request.POST['contZip']
    pc.homePhone = request.POST['contPhoneMain']
    pc.cellPhone = request.POST['contPhoneCell']
    pc.email = request.POST['contEmail']
    return pc

def saveContactInfo(request):
    pc = PatientContact()
    pc = populate_patient_contact(pc, request)
    pc.save()
    return render(request, 'patientinsurance/index.html')

def add_contact(request):
    if request.method == 'POST':
        pc = PatientContact()
        pc = populate_patient_contact(pc, request)
        pc.save()
        return redirect('patientcontact:index')  # Redirect to the index page after saving
    return render(request, 'patientcontact/add.html')  # Render the add contact form

class ModifyView(generic.TemplateView):
    template_name = 'patientcontact/modify.html'
    
def readData(request):
    if request.session.get('member_id'):
        contact = PatientContact.objects \
            .filter(user_name__exact = request.session.get('member_id')).values();
        return render(request, "patientcontact/modify.html", {"contact_list": contact,})
    return render(request, "login/index.html")

def updateContactInfo(request):
    if request.session.get('member_id'):
        pc = PatientContact.objects.get(user_name=request.session.get('member_id'))
        pc = populate_patient_contact(pc, request)
        pc.save()
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'login/index.html')

def edit_contact(request, id):
    contact = get_object_or_404(PatientContact, id=id)
    if request.method == 'POST':
        contact = populate_patient_contact(contact, request)
        contact.save()
        return redirect('patientcontact:index')  # Redirect to the index page after saving
    return render(request, 'patientcontact/edit.html', {'contact': contact})  # Render the edit form

def delete_contact(request, id):
    # Fetch the contact to delete
    contact = get_object_or_404(PatientContact, id=id)
    if request.method == 'POST':
        # Delete the contact
        contact.delete()
        return redirect('patientcontact:index')  # Redirect to the index page after deletion
    return render(request, 'patientcontact/delete.html', {'contact': contact})  # Render the delete confirmation page

def readContactInfo(request):
    if request.session.get('member_id'):
        contacts = PatientContact.objects \
            .filter(user_name__exact=request.session.get('member_id')).values()
        if contacts.count() == 0:
            return render(request, "patientcontact/index.html")
        else:
            return render(request, "patientcontact/modify.html", {"contact_list": contacts})
    return render(request, "login/index.html")  # Redirect to login if no session found
