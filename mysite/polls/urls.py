from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('getFirstResponder/<int:id>/', views.getFirstResponder),
    path('getUnassignedFirstResponders/', views.getUnassignedFirstResponders),
    path('getAssignedFirstResponders/<int:mission_id>/', views.getAssignedFirstResponders),
    path('getUnassignedEvents/', views.getUnassignedEvents),
    path('getMission/<int:mission_id>/', views.getMission),
    path('getAllMissions/', views.getAllMissions),
    path('createFirstResponder/', views.createFirstResponder),
    path('createFirstResponderStatus/', views.createFirstResponderStatus),
    path('createEvent/', views.createEvent),
    path('changeEventPriority/<int:event_id>/', views.changeEventPriority),
    path('createEventTicket/<int:event_id>/<str:ticketType>/<str:ticketStatus>/<str:ticketDescription>/',
         views.createEventTicket),
    path('changeTicketStatus/<int:ticket_id>/<str:newStatus>/', views.changeTicketStatus),
    path('getTickets/<int:event_id>/', views.getTickets),
    path('createMission/', views.createMission),
    path('addEventToMission/<int:event_id>/<int:mission_id>', views.addEventToMission),
    path('addEventStatus/<int:event_id>/<str:time>/<str:status>/', views.addEventStatus),
    path('addFirstResponderToMission/<int:firstResponder_id>/<str:mission_id>/<str:time>/<str:status>/',
         views.addFirstResponderToMission),
    path('createEquipment/<str:e_type>/<int:quantity>/', views.createEquipment),
    path('removeFirstResponderFromMission/<int:firstResponder_id>/<int:mission_id>/<str:time>/',
         views.removeFirstResponderFromMission),
    path('addEquipmentToMission/<int:equipment_id>/<int:mission_id>/<int:amount>/', views.addEquipmentToMission),
    path('removeEquipmentFromMission/<int:equipment_id>/<int:mission_id>/', views.removeEquipmentFromMission),
    path('getAllEquipment/', views.getAllEquipment),


]


'''
    
path('get_event/<int:id>/', views.get_event),

    



    
'''