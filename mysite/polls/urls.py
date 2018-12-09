from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('create_responder/<int:id>/', views.create_responder, name='create_responder'), #Change params
    path('update_responder_status/<int:id>/', views.update_responder_status, name='update_responder_status'), #Change params
    path('get_unassigned_firstResponders/', views.get_unassigned_firstResponders, name='get_unassigned_firstResponders'),
    path('get_assigned_firstResponders/', views.get_assigned_firstResponders, name='get_assigned_firstResponders'),

    path('create_mission/<int:id>/', views.create_mission, name='get_mission'),  # Add params to path
    path('add_event_to_mission/<int:id>', views.add_event_to_mission, name='add_event_to_mission'), #Change params
    path('add_responder_to_mission/<int:id>', views.add_responder_to_mission, name='add_responder_to_mission'), #Change params
    path('add_equipment_to_mission/<int:id>', views.add_equipment_to_mission, name='add_equipment_to_mission'), #Change params
    path('get_mission/<int:id>/', views.get_mission, name='get_mission'),


    path('create_event/<int:id>/', views.create_event, name='create_event'), #Add params to path
    path('update_event_status/<int:id>/', views.update_event_status, name='update_event_status'), #Add params to path
    path('change_event_priority/<int:id>/', views.change_event_priority, name='change_event_priority'),  # Add params to path
    path('add_equipment_to_event/<int:id>', views.add_equipment_to_mission, name='add_equipment_to_mission'), #Change params


    path('get_unassigned_equipment/', views.get_unassigned_equipment, name='get_unassigned_equipment')


    ]