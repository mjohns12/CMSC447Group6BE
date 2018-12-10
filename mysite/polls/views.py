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
    unassigned_firstResponders= list(FirstResponder.objects.all().filter(assignedMissionID=None).values())
    return JsonResponse(unassigned_firstResponders, safe=False)

#Get all assigned first responders
def get_assigned_firstResponders(request):
    assigned_firstResponders= list(FirstResponder.objects.all().exclude(assignedMissionID__isnull=True).values())
    return JsonResponse(assigned_firstResponders, safe=False)

def get_unassigned_equipment(request):
    equipment_list = list(Equipment.objects.filter(missions=None).all().values())
    return JsonResponse(equipment_list, safe=False)



#Get a mission given a mission id
def get_mission(request, id):
    mission = Mission.objects.all().filter(id=id).values()
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

def create_firstResponder(request, fName, lName, bName, occupation, phoneNum, emailAddress):
    new_first_responder = FirstResponder(firstName = fName, lastName = lName, occupation = occupation,
                                         branchName = bName, phoneNumber = phoneNum, email = emailAddress)
    new_first_responder.save()
    return HttpResponse("First Responder Status ID: {} created.".format(new_first_responder.id))

def delete_firstResponder(request, id):
    FirstResponder.objects.filter(id=id).delete()
    return HttpResponse("First Responder ID: {} deleted.".format(id))

#Creates a first responder status and links it to a first responder
def create_firstResponder_status(request, firfirstResponder_id, time, status):
    new_status = FirstResponderStatus(time = time, status = status, firfirstResponder_id = firfirstResponder_id)
    new_status.save()
    return HttpResponse("First Responder Status ID: {} created.".format(new_status.id))

def delete_firstResponder_status(request, id):
    FirstResponderStatus.objects.filter(id=id).delete()
    return HttpResponse("First Responder Status ID: {} deleted.".format(id))

def create_event(request, fName, lName, streetNum, street, city, state, zipCode, phoneNum, timeCalledIn, description, priority):
    timeCalledIn = datetime.strptime(timeCalledIn, '%Y-%m-%d-%H:%M:%S.%f')
    new_event = Event(fName = fName, lName =lName, streetNum = streetNum, street = street, city = city, state = state, zipCode = zipCode,
                        phoneNum = phoneNum, timeCalledIn = timeCalledIn, description = description, priority = priority)
    new_event.save()

    #Default status
    #new_status = EventStatus(event_id = new_event, time, status)
    #new_status.create()

    return HttpResponse("Event ID:{} created.".format(new_event.id))

def delete_event(request, event_id):
    Event.objects.filter(id=event_id).delete()
    return HttpResponse("Evemt ID: {} deleted.".format(event_id))

def change_event_priority(request, event_id, new_priority):
    event = Event.objects.get(id = event_id)
    event.priority = new_priority
    event.save()
    return HttpResponse("Event ID: {} priority changed to {}.".format(event_id, new_priority))

def create_event_ticket(request, event_id, ticketType, ticketStatus):
    new_ticket = EventTicket(event_id = event_id, ticketType = ticketType, ticketStatus = ticketStatus)
    new_ticket.add()
    return HttpResponse("Event ID: {} request sent").format(event_id)

def get_ticket(request, event_id):
    unresolved_tickets = list(ticket.objects.filter(id = event_id, ticketStatus = 'Unresolved').values())
    print(unresolved_tickets)
    return JsonResponse(unresolved_tickets, safe=False)

def get_event_map(request):

    pass

def add_eventStatus(request, event_id, time, status):
    statusTime = datetime.strptime(time, '%Y-%m-%d-%H:%M:%S.%f')
    event = Event.objects.get(id = event_id)
    new_status = EventStatus(event_id=event, time=statusTime, status=status)
    new_status.save()
    return HttpResponse("Status changed for event ID: {}.".format(event_id))

def create_mission(request):
    new_mission = Mission()
    new_mission.save()
    return HttpResponse("Mission ID: {} created.".format(new_mission.id))

def delete_mission(request, id):
    Mission.objects.filter(id=id).delete()
    return HttpResponse("Mission ID: {} deleted.".format(id))

def add_firstResponder_to_mission(request, firstResponder_id, mission_id):
    mission = Mission.objects.get(id=mission_id)
    firstResponder = FirstResponder.objects.get(id=firstResponder_id)
    firstResponder.assignedMissionID.set([mission])
    firstResponder.save()
    return HttpResponse("First Responder ID: {} was added to Mission ID: {}.".format(firstResponder_id, mission_id))

def remove_firstResponder_from_mission(request, firstResponder_id, mission_id):
    mission = Mission.objects.get(id=mission_id)
    firstResponder = FirstResponder.objects.get(id=firstResponder_id)
    firstResponder.assignedMissionID.remove(mission)
    firstResponder.save()
    return HttpResponse("First Responder ID: {} was removed to Mission ID: {}.".format(firstResponder_id, mission_id))

def create_equipment(request, e_type, quantity):
    new_equipment = Equipment(equipmentType = e_type, quantity = quantity)
    new_equipment.save()
    return HttpResponse("Equipment ID: {} created.".format(new_equipment.id))

def delete_equipment(request, equipment_id):
    Equipment.objects.filter(id=equipment_id).delete()
    return HttpResponse("Equipment ID: {} deleted.".format(id))

def add_equipment_to_mission(request, equipment_id, mission_id, amount ):
    equipment = Equipment.objects.get(id=equipment_id)
    mission = Mission.objects.get(id=mission_id)

    if (equipment.quantity - amount) < 0:
        return HttpResponse("Cannot add Equipment ID: {} to Mission ID {}.".format(equipment_id, mission_id))

    #Decrement quantity
    equipment.missions.add(mission)
    new_quantity = equipment.quantity - amount
    equipment.quantity = new_quantity
    equipment.save()
    return HttpResponse("Equipment ID: {} was added to Mission ID {}.".format(equipment_id, mission_id))

def remove_equipment_from_mission(request, equipment_id, mission_id):
    equipment = Equipment.objects.get(id=equipment_id)
    mission = Mission.objects.get(id=mission_id)
    equipment.missions.remove(mission)
    equipment.save()
    return HttpResponse("Equipment ID: {} was removed from Mission ID.".format(equipment_id, mission_id))

