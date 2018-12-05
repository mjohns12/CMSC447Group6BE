from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_callCenterOps(request):
    users = CallCenterOperator.objects.all().values()
    users_list = list(users)
    return JsonResponse(users_list, safe=False)

def add_Event(request):
    date = models.DateTimeField(default=datetime.now, blank=True)
    new_event = Event(firstName = None, lastName = None,
                      streetNum = None, streetName = None,
                      city = None, state = None, zipCode = None, phoneNumber = None,
                      timeCalleIn = None, description = None, priorityCode = None,
                      opChief_id = None, mission_id = None)
    new_event.save()
    events = Event.objects.all().values()
    eventsList = list(events)
    return JsonResponse(eventsList, safe=False)