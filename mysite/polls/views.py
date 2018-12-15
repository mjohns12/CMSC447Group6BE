from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import *
from geopy.geocoders import Nominatim
<<<<<<< HEAD
from django.db.models import OuterRef, Subquery, Max, F
from django.forms.models import model_to_dict
from django.utils import timezone
import pytz

def formatEvent(event):
    event['statuses'] = list(
        EventStatus.objects
        .filter(event_id = event['id'])
        .values('status', 'time')
    )

    event['tickets'] = list(
        EventTicket.objects
        .filter(
          event_id = event['id'],
          ticketStatus = 'Unresolved'
        ).values(
          'id',
          'ticketStatus', 
          'ticketDescription', 
          'ticketType'
        )
    )

=======
from django.db.models import Max

def formatEvent(event):
    event['statuses'] = list(
            EventStatus.objects
            .filter(event_id = event['id'])
            .values('status', 'time')
        )
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
    equipment = list(
        RequiredEquipment.objects
        .filter(event_id = event['id'])
        .values(
<<<<<<< HEAD
            'equipment__equipmentType',
            'equipment_id',
=======
            'equipment_id__equipmentType',
            'id',
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
            'quantity'
        )
    )
    for e in equipment:
<<<<<<< HEAD
        e['equipmentType'] = e['equipment__equipmentType']
        del e['equipment__equipmentType']
        e['id'] = e['equipment_id']
        del e['equipment_id']
=======
        e['equipmentType'] = e['equipment_id__equipmentType']
        del e['equipment_id__equipmentType']
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

    event['equipment'] = equipment
    return event

def formatResponder(responder):
    responder['statuses'] = list(
        FirstResponderStatus.objects
<<<<<<< HEAD
        .filter(responder = responder['id'])
        .values(
            'mission_id',
            'event_id',
=======
        .filter(firstResponder_id = responder['id'])
        .values(
            'mission_id_id',
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
            'status',
            'time'
        )
    )
<<<<<<< HEAD
    return responder

def formatMission(mission):
    mission['events'] = list(Event.objects.annotate(
        status_time = Max('eventstatus__time')
    ).filter(
        eventstatus__mission = mission['id'],
        eventstatus__time = F('status_time')
    ).values())

    mission['firstResponders'] = list(FirstResponder.objects.annotate(
        status_time = Max('firstresponderstatus__time')
    ).filter(
        firstresponderstatus__mission = mission['id'],
        firstresponderstatus__time = F('status_time')
    ).values())

=======
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
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
    for responder in mission['firstResponders']:
        formatResponder(responder)

    totalEquip = {}
    for event in mission['events']:
        event = formatEvent(event)
        for e in event['equipment']:
            if e['id'] in totalEquip:
<<<<<<< HEAD
                totalEquip[e['id']]['quantity'] += e['quantity']
            else:
                totalEquip[e['id']] = dict(e)
=======
                totalEquip[e['id']].quantity += e['quantity']
            else:
                totalEquip[e['id']] = e
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

    mission['equipment'] = list(totalEquip.values())

    return mission

<<<<<<< HEAD
#--------------------------------------------------
=======
#---------------------------------------------------
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

<<<<<<< HEAD
#-----------------Mission Services-----------------
=======
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
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

def createMission(request):
    newMission = Mission()
    newMission.save()
    return JsonResponse(model_to_dict(newMission))

def getMission(request, mission_id):
    mission = Mission.objects.filter(id=mission_id).values()
<<<<<<< HEAD
    if len(mission):
=======
    if mission.count:
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
        mission = formatMission(mission[0])
        return JsonResponse(mission, safe=False)
    else:
        return HttpResponseBadRequest()
<<<<<<< HEAD
=======

>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

#missions with events that aren't finished
def getAllMissions(request):
    missions = list(Mission.objects.all().values())
    for mission in missions:
        formatMission(mission)
    return JsonResponse(missions, safe=False)
<<<<<<< HEAD

#-----------------First Responder Services-----------------

def createFirstResponder(request):
    values = request.GET.get
    newFirstResponder = FirstResponder(
        firstName = values('fName'), 
        lastName = values('lName'), 
        occupation = values('occupation'),
        branchName = values('branch'), 
        phoneNumber = values('phone'), 
        email = values('email')
    )
    newFirstResponder.save()
    # Default Status
    newStatus = FirstResponderStatus(
      time = timezone.now(),
      status = 'Unassigned',
      responder = newFirstResponder,
      mission = None
    )
    newStatus.save()
    return HttpResponse("First Responder ID: {} created.".format(newFirstResponder.id))
=======
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

def getFirstResponder(request, id):
    responder = FirstResponder.objects.filter(pk = id).values()
    if len(responder):
        responder = formatResponder(responder[0])
        return JsonResponse(responder, safe=False)
    else:
        return HttpResponseBadRequest("This record doesn't exist")

<<<<<<< HEAD
#Get all unassigned first responders
def getUnassignedFirstResponders(request):
    unassignedResponders = list(FirstResponder.objects.annotate(
        status_time = Max('firstresponderstatus__time')
      ).filter(
        firstresponderstatus__mission__isnull=True,
        firstresponderstatus__time = F('status_time')
      ).values())
    
    unassignedResponders = [formatResponder(a) for a in unassignedResponders]
    return JsonResponse(unassignedResponders, safe=False)
=======
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
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

#Get all assigned first responders
def getAssignedFirstResponders(request, mission_id):
    assignedResponders = list(FirstResponder.objects.annotate(
        status_time = Max('firstresponderstatus__time')
      ).filter(
        firstresponderstatus__mission__isnull=False,
        firstresponderstatus__time = F('status_time')
      ).values())
    assignedResponders = [formatResponder(a) for a in assignedResponders]
    return JsonResponse(assignedResponders, safe=False)

#Creates a first responder status and links it to a first responder
<<<<<<< HEAD
def createFirstResponderStatus(request, responder_id):
    values = request.GET.get
    responder = FirstResponder.objects.get(pk = responder_id)
    missionId = values('mission_id')
    if missionId:
        mission = Mission.objects.get(pk = missionId)
    else:
        mission = None

    eventId = values('event_id')
    if eventId:
        event = Event.objects.get(id = eventId)
    else:
        event = None

    newStatus = FirstResponderStatus(
        time = timezone.now(), 
        status = values('status', 'Unassigned'), 
        responder = responder,
        mission = mission,
        event = event
=======
def createFirstResponderStatus(request):
    values = request.GET.get
    newStatus = FirstResponderStatus(
        time = datetime.today(), 
        status = values('status', 'Unassigned'), 
        firstResponder_id = values('responder_id', ''),
        mission_id = values('mission_id', '')
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
    )
    newStatus.save()
    return HttpResponse("First Responder Status ID: {} created.".format(newStatus.id))

<<<<<<< HEAD
#-----------------Event Services-----------------

# Creates a new event from the information given in a GET request
def createEvent(request):
    values = request.GET.get
    newEvent = Event(
        fName = values('fName'),
        lName = values('lName'),
        streetNum = values('streetNum'), 
        street = values('streetName'), 
        city = values('city'), 
        state = values('state'), 
        zipCode = values('zipCode'),
        phoneNum = values('phoneNum'), 
        timeCalledIn = timezone.now(), 
        description = values('description', ''), 
        priority = values('priority')
    )
    # Geolocate Address to get its latitude and longitude
    addressString = newEvent.streetNum + " " +  newEvent.street + " " + newEvent.city + " " + newEvent.state
=======

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
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d
    geolocator = Nominatim()
    location = geolocator.geocode(addressString)
    if not location:
      location = dict(
        longitude = 0,
        latitude = 0
      )
    newEvent.lon = location['longitude']
    newEvent.lat = location['latitude']
    newEvent.save()
    # Add default status of unassigned
    newStatus = EventStatus(
        event = newEvent,
        time = timezone.now(),
        status = 'Unassigned'
    )
    newStatus.save()
    return HttpResponse("Event ID:{} created.".format(newEvent.id))

# Returns a list of all the events not associated with a mission
def getUnassignedEvents(request):
    unassignedEvents = list(Event.objects.annotate(
      status_time = Max('eventstatus__time')
    ).filter(
      eventstatus__status = 'Unassigned',
      eventstatus__time = F('status_time')
    ).values())

    unassignedEvents = [formatEvent(e) for e in unassignedEvents]
    return JsonResponse(unassignedEvents, safe=False)

# Adds a status to the event, valid ones are 
def createEventStatus(request, event_id):
    event = Event.objects.get(pk = event_id)

    missionId = request.GET.get('mission_id')
    if missionId:
        mission = Mission.objects.get(pk = missionId)
    else:
        mission = None

    newStatus = EventStatus(
        event = event,
        time = timezone.now(),
        status = request.GET.get('status'), 
        mission = mission
    )
    newStatus.save()
    return HttpResponse("Status changed for event ID: {}.".format(event_id))

def changeEventPriority(request, event_id):
<<<<<<< HEAD
    event = Event.objects.get(pk = event_id)
    newPriority = request.GET.get('priority', event.priority)
    event.priority = newPriority
    event.save()
    return HttpResponse("Event ID: {} priority changed to {}.".format(event_id, newPriority))

    
#-----------------Event Ticket Services-----------------
def createEventTicket(request, event_id):
    values = request.GET.get
    event = Event.objects.get(pk = event_id)
    newTicket = EventTicket.objects.create(
        event = event, 
        ticketStatus = 'Unresolved',
        ticketType = values('ticketType'),
        ticketDescription = values('ticketDescription')
    )
    return HttpResponse("EventTicket ID: {} created.".format(event_id))

def getUnresolvedTickets(request, event_id):
    unresolvedTickets = list(
        EventTicket.objects
        .filter(
            event_id = event_id,
            ticketStatus = 'Unresolved'
        ).values()
    )
    return JsonResponse(unresolvedTickets, safe=False)
=======
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
>>>>>>> 73ad57042004267dcb2748cb502ed8869a25db5d

def changeTicketStatus(request, ticket_id):
    ticket = EventTicket.objects.get(id = ticket_id)
    ticket.ticketStatus = request.GET.get('newStatus')
    ticket.save()
    return HttpResponse("Ticket ID: {} status changed.".format(ticket_id))


#-----------------Equipment Services-----------------

def createEquipment(request):
    new_equipment = Equipment(
        equipmentType = request.GET.get('equipmentType')
    )
    new_equipment.save()
    return HttpResponse("Equipment ID: {} created.".format(new_equipment.id))

def getAllEquipment(request):
    equipmentList = list(Equipment.objects.all().values())
    return JsonResponse(equipmentList, safe=False)

def requireEquipmentForEvent(request, event_id):
    values = request.GET.get
    equipment = Equipment.objects.get(pk = values('equipment_id'))
    event = Event.objects.get(pk = event_id)
    equip, created = RequiredEquipment.objects.get_or_create(
        equipment = equipment,
        event = event,
        defaults={'quantity': values('quantity')}
    )
    if not created:
      equip.quantity += int(values('quantity'))
      equip.save()

    return HttpResponse(
        "Event #{} requires {} {}s"
        .format(event_id, values('quantity'), equipment.equipmentType)
    )

def issueEquipmentToEvent(request, event_id):
    values = request.GET.get
    equipment = Equipment.objects.get(pk = values('equipment_id'))
    event = Event.objects.get(pk = event_id)
    required = RequiredEquipment.objects.get(
        equipment = equipment,
        event = event
    )
    quantity = int(values('quantity'))
    if required.quantity <= quantity:
        required.delete()
    else:
        required.quantity -= quantity
        required.save()

    return HttpResponse(
        "Event #{} requires {} {}s"
        .format(event_id, quantity, equipment.equipmentType)
    )