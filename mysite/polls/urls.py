from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('get_mission/<int:id>', views.get_mission),

    path('get_unassigned_firstResponders/', views.get_unassigned_firstResponders, name='get_unassigned_firstResponders'),
    path('get_assigned_firstResponders/', views.get_assigned_firstResponders, name='get_assigned_firstResponders'),

    path('create_firstResponder/<str:fName>/<str:lName>/<str:bName>/<str:occupation>/<str:phoneNum>/<str:emailAddress>/', views.create_firstResponder),
    path('delete_firstResponder/<int:firstResponder_id>/',views.delete_firstResponder),
    path('create_firstResponder_status/<int:firstResponder_id>/<str:time>/<str:status>/', views.create_firstResponder_status),
    path('delete_firstResponder_status/<int:firstResponderStatus_id>/', views.delete_firstResponder_status),

    path('create_event/<str:fName>/<str:lName>/<str:streetNum>/<str:street>/<str:city>/<str:state>/<str:zipCode>/<str:phoneNum>/<str:timeCalledIn>/<str:description>/<int:priority>/', views.create_event),
    path('delete_event/<int:event_id>/', views.delete_event),
    path('change_event_priority/<int:event_id>/<int:new_priority>/', views.change_event_priority),
    path('add_eventStatus/<int:event_id>/<str:time>/<str:status>/', views.add_eventStatus),
    path('create_event_ticket/<int:event_id>/<str:ticketType>/<str:status>/', views.send_ticket),


    path('create_mission/', views.create_mission),
    path('delete_mission/<int:id>/', views.delete_mission),
    path('add_firstResponder_to_mission/<int:firstResponder_id>/<str:mission_id>/', views.add_firstResponder_to_mission),
    path('remove_firstResponder_from_mission/<int:firstResponder_id>/<int:mission_id>/', views.remove_firstResponder_from_mission),

    path('create_equipment/<str:e_type>/<int:quantity>/', views.create_equipment),
    path('delete_equipment/<int:equipment_id>/', views.delete_equipment),
    path('add_equipment_to_mission/<int:equipment_id>/<int:mission_id>/<int:amount>/', views.add_equipment_to_mission),
    path('remove_equipment_from_mission/<int:equipment_id>/<int:mission_id>/', views.remove_equipment_from_mission),

]


   
    
