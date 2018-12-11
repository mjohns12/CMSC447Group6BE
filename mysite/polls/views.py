from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from datetime import datetime
from geopy.geocoders import Nominatim


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#---------------------------------------------------

def getFirstResponder(request, firstResponderId):
    responder = list(FirstResponder.objects.get(id = firstRespodnerId).values())
    responder['Statuses'] = list(FirstResponderStatus.objects.filter(firstResponder_id=firstResponder_id))
    return JsonResponse(unassignedFirstResponders, safe=False)

#Get all unassigned first responders
def getUnassignedFirstResponders(request):
    unassignedFirstResponders = list(FirstResponder.objects.filter(firstresponderstatus__mission_id=None).values())
    return JsonResponse(unassignedFirstResponders, safe=False)

#Get all assigned first responders
def getAssignedFirstResponders(request, mission_id):
    assignedFirstResponders = \
        list(FirstResponder.objects.filter(firstresponderstatus__mission_id=mission_id).values())
    return JsonResponse(assignedFirstResponders, safe=False)


def getUnassignedEvents(request):
    unassignedEvents = \
        list(Event.objects.filter(eventtatus__mission_id=None).values())
    return JsonResponse(unassignedEvents, safe=False)


def getMission(request, mission_id):
    mission = list(Mission.objects.filter(id=mission_id).values())
    mission[0]['events'] =  list(Event.objects.all().filter(eventstatus__mission_id = mission_id).values())
    mission[0]['firstResponders'] = \
        list(FirstResponder.objects.all().filter(firstresponderstatus__mission_id=mission_id).values())
    mission[0]['equipment'] = \
        list(Event.objects.filter(eventstatus__mission_id = mission_id).aggregate(models.Sum(requiredequipment__quantity)))


    return JsonResponse(mission, safe=False)

#missions with events that aren't finished
def getAllMissions(request):
    pass

def getAllEquipment(request):
    equipmentList = list(Equipment.objects.all().values())
    return JsonResponse(equipmentList, safe=False)

def createFirstResponder(request, fName, lName, bName, occupation, phoneNum, emailAddress):
    newFirstResponder = FirstResponder(firstName = fName, lastName = lName, occupation = occupation,
                                         branchName = bName, phoneNumber = phoneNum, email = emailAddress)
    newFirstResponder.save()
    return HttpResponse("First Responder Status ID: {} created.".format(newFirstResponder.id))


#Creates a first responder status and links it to a first responder
def createFirstResponderStatus(request, firstResponder_id, time, status):
    newStatus = FirstResponderStatus(time = time, status = status, firstResponder_id = firstResponder_id)
    newStatus.save()
    return HttpResponse("First Responder Status ID: {} created.".format(newStatus.id))


def createEvent(request, fName, lName, streetNum, street, city, state, zipCode, phoneNum, timeCalledIn, description, priority):
    timeCalledIn = datetime.strptime(timeCalledIn, '%Y-%m-%d-%H:%M:%S.%f')
    newEvent = Event(fName = fName, lName =lName, streetNum = streetNum, street = street, city = city, state = state, zipCode = zipCode,
                        phoneNum = phoneNum, timeCalledIn = timeCalledIn, description = description, priority = priority)


    addressString = streetNum + " " +  street + " " + city + " " + state
    geolocator = Nominatim()
    location = geolocator.geocode(addressString)

    newEvent.lon = location.longitude
    newEvent.lat = location.latitude
    newEvent.save()

    #Default status
    #new_status = EventStatus(event_id = new_event, time, status)
    #new_status.create()

    return HttpResponse("Event ID:{} created.".format(new_event.id))


def changeEventPriority(request, event_id, newPriority):
    event = Event.objects.get(id = event_id)
    event.priority = newPriority
    event.save()
    return HttpResponse("Event ID: {} priority changed to {}.".format(event_id, newPriority))

def createEventTicket(request, event_id, ticketType, ticketStatus, ticketDescription):
    event = Event.objects.get(id=event_id)
    newTicket = EventTicket(event_id = event, ticketType = ticketType, ticketStatus = ticketStatus, ticketDescription =ticketDescription)
    newTicket.save()
    return HttpResponse("Event ID: {} requested made.".format(event_id))

def changeTicketStatus(request, ticket_id, new_status):
    ticket = EventTicket.objects.get(id = ticket_id)
    ticket.ticketStatus = new_status
    ticket.save()
    return HttpResponse("Ticket ID: {} status changed.".format(new_status))

def getTickets(request, event_id):
    unresolvedTickets = list(EventTicket.objects.filter(event_id = event_id, ticketStatus = 'Unresolved').values())
    return JsonResponse(unresolvedTickets, safe=False)

def createMission(request):
    newMission = Mission()
    newMission.save()
    return HttpResponse("Mission ID: {} created.".format(new_mission.id))


def addEventToMission(request, event_id, mission_id):
    statusTime = datetime.strptime(time, '%Y-%m-%d-%H:%M:%S.%f')
    event = Event.objects.get(id=event_id)
    newStatus = EventStatus(event_id=event, time=statusTime, status='', mission_id=mission_id)
    newStatus.save()
    return HttpResponse("Event ID: {} added to Mission ID: {}.".format(event_id, mission_id))


def addEventStatus(request, event_id, time, status):
    statusTime = datetime.strptime(time, '%Y-%m-%d-%H:%M:%S.%f')
    event = Event.objects.get(id = event_id)
    newStatus = EventStatus(event_id=event, time=statusTime, status='Started', mission_id = mission_id)
    newStatus.save()
    return HttpResponse("Status changed for event ID: {}.".format(event_id))


def addFirstResponderToMission(request, firstResponder_id, mission_id, time):
    addTime = datetime.strptime(time,'%Y-%m-%d-%H:%M:%S.%f')
    mission = Mission.objects.get(id=mission_id)
    firstResponder = FirstResponder.objects.get(id=firstResponder_id)
    newStatus = FirstResponderStatus(time=addTime, status='Undecided', firstResponder_id=firstResponder, mission_id = mission)
    newStatus.save()
    return HttpResponse("First Responder ID: {} was added to Mission ID: {}.".format(firstResponder_id, mission_id))

def removeFirstResponderFromMission(request, firstResponder_id, mission_id, time):
    addtime = datetime.strptime(time, '%Y-%m-%d-%H:%M:%S.%f')
    mission = Mission.objects.get(id=mission_id)
    firstResponder = FirstResponder.objects.get(id=firstResponder_id)
    newStatus = FirstResponderStatus(time=addtime, status='Unassigned', firstResponder_id=firstResponder, mission_id=None)
    newStatus.save()
    return HttpResponse("First Responder ID: {} was removed to Mission ID: {}.".format(firstResponder_id, mission_id))

def createEquipment(request, e_type, quantity):
    new_equipment = Equipment(equipmentType = e_type, quantity = quantity)
    new_equipment.save()
    return HttpResponse("Equipment ID: {} created.".format(new_equipment.id))



def addEquipmentToMission(request, equipment_id, mission_id, amount ):
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

def removeEquipmentFromMission(request, equipment_id, mission_id):
    equipment = Equipment.objects.get(id=equipment_id)
    mission = Mission.objects.get(id=mission_id)
    equipment.missions.remove(mission)
    equipment.save()
    return HttpResponse("Equipment ID: {} was removed from Mission ID.".format(equipment_id, mission_id))

