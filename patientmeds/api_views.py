import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PatientMedication
import json

# Configure logging
logger = logging.getLogger(__name__)

@csrf_exempt  # Use cautiously; ensure security measures are in place
def patient_meds_api(request):
    try:
        if request.method == 'GET':
            # Fetch data from the database with optional filters
            meds_name = request.GET.get('meds_name', '').strip()
            meds_strength = request.GET.get('meds_strength', '').strip()
            meds_dir = request.GET.get('meds_dir', '').strip()
            meds_status = request.GET.get('meds_status', '').strip()
            meds_date = request.GET.get('meds_date', '').strip()

            filters = {}
            if meds_name:
                filters['meds_name__icontains'] = meds_name
            if meds_strength:
                filters['meds_strength__icontains'] = meds_strength
            if meds_dir:
                filters['meds_dir__icontains'] = meds_dir
            if meds_status:
                filters['meds_status__icontains'] = meds_status
            if meds_date:
                filters['meds_date'] = meds_date

            meds = PatientMedication.objects.filter(**filters).values()
            return JsonResponse(list(meds), safe=False)

        elif request.method == 'POST':
            try:
                data = json.loads(request.body)
                meds_name = data.get('meds_name')
                meds_strength = data.get('meds_strength')
                meds_dir = data.get('meds_dir')
                meds_status = data.get('meds_status')
                meds_date = data.get('meds_date')

                # Validate required fields
                if not meds_name or not meds_strength:
                    return JsonResponse({'error': 'Missing required fields: meds_name and meds_strength'}, status=400)

                PatientMedication.objects.create(
                    meds_name=meds_name,
                    meds_strength=meds_strength,
                    meds_dir=meds_dir,
                    meds_status=meds_status,
                    meds_date=meds_date
                )
                return JsonResponse({'message': 'Medication added successfully'}, status=201)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
            except Exception as e:
                logger.error(f"Error in POST request: {str(e)}", exc_info=True)
                return JsonResponse({'error': 'Internal Server Error', 'details': str(e)}, status=500)

        elif request.method == 'PUT':
            # Handle PUT requests (update medication)
            resource_id = request.POST.get('id')
            if not resource_id:
                return JsonResponse({'error': 'Resource ID is missing'}, status=400)

            try:
                medication = PatientMedication.objects.get(pk=resource_id)
                medication.meds_name = request.POST.get('meds_name', medication.meds_name)
                medication.meds_strength = request.POST.get('meds_strength', medication.meds_strength)
                medication.meds_dir = request.POST.get('meds_dir', medication.meds_dir)
                medication.meds_status = request.POST.get('meds_status', medication.meds_status)
                medication.meds_date = request.POST.get('meds_date', medication.meds_date)
                medication.save()
                return JsonResponse({'message': 'Medication updated successfully'})
            except PatientMedication.DoesNotExist:
                return JsonResponse({'error': 'Resource not found'}, status=404)

        elif request.method == 'DELETE':
            # Handle DELETE requests (delete medication)
            resource_id = request.POST.get('id')
            if not resource_id:
                return JsonResponse({'error': 'Resource ID is missing'}, status=400)

            try:
                medication = PatientMedication.objects.get(pk=resource_id)
                medication.delete()
                return JsonResponse({'message': 'Medication deleted successfully'})
            except PatientMedication.DoesNotExist:
                return JsonResponse({'error': 'Resource not found'}, status=404)

        else:
            return JsonResponse({'error': 'Invalid request method'}, status=405)

    except Exception as e:
        logger.error(f"Error in patient_meds_api: {str(e)}", exc_info=True)
        return JsonResponse({'error': 'Internal Server Error', 'details': str(e)}, status=500)
