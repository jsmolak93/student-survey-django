from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Survey
import json

@csrf_exempt
def get_all_surveys(request):
    if request.method == 'GET':
        surveys = list(Survey.objects.values())
        return JsonResponse(surveys, safe=False)

@csrf_exempt
def get_survey_by_id(request, id):
    survey = get_object_or_404(Survey, pk=id)
    return JsonResponse(model_to_dict(survey))

@csrf_exempt
def create_survey(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        survey = Survey.objects.create(**data)
        return JsonResponse({'id': survey.id})

@csrf_exempt
def update_survey(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        survey = get_object_or_404(Survey, pk=id)
        for key, value in data.items():
            setattr(survey, key, value)
        survey.save()
        return JsonResponse({'updated': True})

@csrf_exempt
def delete_survey(request, id):
    if request.method == 'DELETE':
        survey = get_object_or_404(Survey, pk=id)
        survey.delete()
        return JsonResponse({'deleted': True})
