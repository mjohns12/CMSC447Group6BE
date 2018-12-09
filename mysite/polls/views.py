from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from datetime import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#-----------------Helper functions-----------------
def get_firstResponders():
    firstResponder_list = list(FirstResponder.objects.all().values())
    for responder in firstResponder_list:
        responder['statuses'] = \
                list(FirstResponderStatus.objects
                     .filter(firstResponder_id=responder['id']).all().values())
    return firstResponder_list

#---------------------------------------------------

#Get all unassigned first responders
def get_unassigned_firstResponders(request):
    unassigned_firstResponders_list = get_firstResponders()
    for responder in unassigned_firstResponders_list:
        currStatus  = responder['statuses'][-1]['status']
        if (currStatus != "Undecided"):
            unassigned_firstResponders_list.remove(responder)
    return JsonResponse(unassigned_firstResponders_list, safe=False)

#Get all assigned first responders
def get_assigned_firstResponders(request):
    assigned_firstResponders_list = get_firstResponders()
    for responder in assigned_firstResponders_list:
        currStatus = responder['statuses'][-1]['status']
        if (currStatus == "Undecided"):
            assigned_firstResponders_list.remove(responder)
    return JsonResponse(assigned_firstResponders_list, safe=False)

def get_unassigned_equipment(request):
    equipment_list = list(Equipment.objects.filter(missions=None).all().values())
    return JsonResponse(equipment_list, safe=False)

#Get a mission given a mission id
def get_mission(request, id):
    mission = Mission.objects.all().filter(id=id).all().values()
    mission_list = list(mission)

    #get the events in the mission
    mission_list[0]['events'] = list(Event.objects.filter(mission_id=id).all().values())
    #get statuses for events
    for event in mission_list[0]['events']:
        print(event['id'])
        event['equipmentNeeded'] = \
            list(Equipment.objects.filter(events=event['id']).all().values())
        event['statuses'] = \
            list(EventStatus.objects.filter(event_id=event['id']).all().values())

    #get first responders on the mission
    mission_list[0]['firstResponders'] = \
        list(FirstResponder.objects.filter(assignedMissionID=id).all().values())
    #get statuses for each first responder
    for responder in mission_list[0]['firstResponders']:
        responder['statuses'] = \
            list(FirstResponderStatus.objects.filter(firstResponder_id=responder['id']).all().values())

    #get the equipment for the mission
    mission_list[0]['equipment'] = list(Equipment.objects.filter(missions=id).all().values())

    return JsonResponse(mission_list, safe=False)

# Add a first responder to the database
def create_responder(request, ):
    pass

# Change(Add) a new status for a given first responder
def update_responder_status(request):
    pass

#Add a new event to the database
def create_event(request):
    pass

#Update the priority of a given event
def change_event_priority(request):
    pass

#Change(Add) a new status for a given event
def update_event_status(request):
    pass

#Add equipment to event
def add_equipment_to_event(request):
    pass


#Add a new mission to the database
def create_mission(request):
    pass

#Add an event to a mission
def add_event_to_mission(request):
    pass

#Add a responder to a mission
def add_responder_to_mission(request):
    pass

#Add equipment to a mission
def add_equipment_to_mission(request):
    pass

