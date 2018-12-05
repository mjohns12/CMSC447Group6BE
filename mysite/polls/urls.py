from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_callCenterOps', views.get_callCenterOps, name='get_callCenterOps'),
    path('add_Event', views.add_Event, name='add_Event')
]