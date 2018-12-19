from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('createMission/', views.createMission),
    path('getMission/<int:mission_id>/', views.getMission),
    path('getAllMissions/', views.getAllMissions),

    path('createFirstResponder/', views.createFirstResponder),
    path('getFirstResponder/<int:id>/', views.getFirstResponder),
    path('getUnassignedFirstResponders/', views.getUnassignedFirstResponders),
    path('getAssignedFirstResponders/<int:mission_id>/', views.getAssignedFirstResponders),
    path('createFirstResponderStatus/<int:responder_id>/', views.createFirstResponderStatus),

    path('createEvent/', views.createEvent),
    path('getUnassignedEvents/', views.getUnassignedEvents),
    path('changeEventPriority/<int:event_id>/', views.changeEventPriority),
    path('createEventStatus/<int:event_id>/', views.createEventStatus),

    # TODO: All of these 3
    path('createEventTicket/<int:event_id>/', views.createEventTicket),
    path('getUnresolvedTickets/<int:event_id>/', views.getUnresolvedTickets),
    path('changeTicketStatus/<int:ticket_id>/', views.changeTicketStatus),
    
    path('createEquipment/', views.createEquipment),
    path('getAllEquipment/', views.getAllEquipment),
    path('requireEquipmentForEvent/<int:event_id>/', views.requireEquipmentForEvent),
    path('issueEquipmentToEvent/<int:event_id>/', views.issueEquipmentToEvent)
]
