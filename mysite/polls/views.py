from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import *
from datetime import datetime
from geopy.geocoders import Nominatim
from django.db.models import Max

def formatEvent(event):
    event['statuses'] = list(
            EventStatus.objects
            .filter(event_id = event['id'])
            .values('status', 'time')
        )
    equipment = list(
        RequiredEquipment.objects
        .filter(event_id = event['id'])
        .values(
            'equipment_id__equipmentType',
            'id',
            'quantity'
        )
    )
    for e in equipment:
        e['equipmentType'] = e['equipment_id__equipmentType']
        del e['equipment_id__equipmentType']

    event['equipment'] = equipment
    return event

def formatResponder(responder):
    responder['statuses'] = list(
        FirstResponderStatus.objects
        .filter(firstResponder_id = responder['id'])
        .values(
            'mission_id_id',
            'status',
            'time'
        )
    )
    for r in responder['statuses']:
        r['mission_id'] = r['mission_id_id']
        del r['mission_id_id']
    return responder

def formatMission(mission):
    mission['events'] =  list(Event.objects
        .filter(eventstatus__mission_id = mission['id'])
        .values()
    )
    mission['firstResponders'] = list(
        FirstResponder.objects
        .filter(firstresponderstatus__mission_id=mission['id'])
        .values()
        .distinct()
    )
    for responder in mission['firstResponders']:
        formatResponder(responder)

    totalEquip = {}
    for event in mission['events']:
        event = formatEvent(event)
        for e in event['equipment']:
            if e['id'] in totalEquip:
                totalEquip[e['id']].quantity += e['quantity']
            else:
                totalEquip[e['id']] = e

    mission['equipment'] = list(totalEquip.values())

    return mission

#---------------------------------------------------

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#---------------------------------------------------

def getFirstResponder(request, id):
    responder = FirstResponder.objects.filter(pk = id).values()
    if responder.count:
        responder = formatResponder(responder[0])
        return JsonResponse(responder, safe=False)
    else:
        return HttpResponseBadRequest("This record doesn't exist")

#Get all unassigned first responders
def getUnassignedFirstResponders(request):
    unassignedResponders = list(
        FirstResponder.objects
        .filter(firstresponderstatus__mission_id=None)
        .values()
    )
    unassignedResponders = [formatResponder(a) for a in unassignedResponders]
    return JsonResponse(unassignedResponders, safe=False)

#Get all assigned first responders
def getAssignedFirstResponders(request, mission_id):
    assignedResponders = list(
        FirstResponder.objects
        .filter(firstresponderstatus__mission_id=mission_id)
        .values()
    )
    assignedResponders = [formatResponder(a) for a in assignedResponders]
    return JsonResponse(assignedResponders, safe=False)

def getUnassignedEvents(request):
    unassignedEvents = list(
        Event.objects
        .filter(eventstatus__mission_id=None)
        .values()
    )
    unassignedEvents = [formatEvent(e) for e in unassignedEvents]
    return JsonResponse(unassignedEvents, safe=False)


def getMission(request, mission_id):
    mission = Mission.objects.filter(id=mission_id).values()
    if mission.count:
        mission = formatMission(mission[0])
        return JsonResponse(mission, safe=False)
    else:
        return HttpResponseBadRequest()


#missions with events that aren't finished
def getAllMissions(request):
    missions = list(Mission.objects.all().values())
    for mission in missions:
        formatMission(mission)
    return JsonResponse(missions, safe=False)

def getAllEquipment(request):
    equipmentList = list(Equipment.objects.all().values())
    return JsonResponse(equipmentList, safe=False)

def createFirstResponder(request):
    values = request.GET.get
    newFirstResponder = FirstResponder(
        firstName = values('fName', ''), 
        lastName = values('lName', ''), 
        occupation = values('occupation', ''),
        branchName = values('branch', ''), 
        phoneNumber = values('phone', ''), 
        email = values('email', '')
    )
    newFirstResponder.save()
    return HttpResponse("First Responder Status ID: {} created.".format(newFirstResponder.id))


#Creates a first responder status and links it to a first responder
def createFirstResponderStatus(request):
    values = request.GET.get
    newStatus = FirstResponderStatus(
        time = datetime.today(), 
        status = values('status', 'Unassigned'), 
        firstResponder_id = values('responder_id', ''),
        mission_id = values('mission_id', '')
    )
    newStatus.save()
    return HttpResponse("First Responder Status ID: {} created.".format(newStatus.id))


def createEvent(request):
    values = request.GET.get
    newEvent = Event(
        fName = values('fName', ''),
        lName = values('lName', ''),
        streetNum = values('streetNum', ''), 
        street = values('street', ''), 
        city = values('city', ''), 
        state = values('state', ''), 
        zipCode = values('zipCode', ''),
        phoneNum = values('phoneNum', ''), 
        timeCalledIn = datetime.today(), 
        description = values('description', ''), 
        priority = values('priority', '')
    )

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


def changeEventPriority(request, event_id):
    event = Event.objects.get(id = event_id)
    event.priority = request.GET.get('priority', event.priority)
    event.save()
    return HttpResponse("Event ID: {} priority changed to {}.".format(event_id, newPriority))

def createEventTicket(request, event_id):
    values = request.GET.get
    # TODO: Put a test in here to make sure that the event exists
    newTicket = EventTicket(
        event_id = event_id, 
        ticketType = values('type', 'Other'),
        ticketStatus = values('status', ''),
        ticketDescription = values('description', '')
    )
    newTicket.save()
    return HttpResponse("EventTicket ID: {} created.".format(event_id))

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

