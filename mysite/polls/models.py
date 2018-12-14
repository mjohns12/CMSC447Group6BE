from django.db import models

#Todo :add tostrings

class User(models.Model):
    phoneNumber = models.CharField(max_length=25)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    branchName = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.firstName + " " + self.lastName

class CallCenterOperator(User):
    pass

class OperationsChief(User):
    pass

class FirstResponder(User):
    occupation = models.CharField(max_length=100)

class LeadFirstResponder(FirstResponder):
    pass

class Mission(models.Model):
    pass


class FirstResponderStatus(models.Model):
    time = models.DateTimeField()
    status = models.CharField(max_length=200)
    firstResponder_id = models.ForeignKey(FirstResponder,
        on_delete=models.CASCADE)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True)

class Equipment(models.Model):
    equipmentType = models.CharField(max_length=50)

class Event(models.Model):
    fName = models.CharField(max_length=30, null=True, blank=True)
    lName = models.CharField(max_length=30, null=True, blank=True)
    streetNum = models.CharField(max_length=30, null=True,blank=True)
    street = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=30,null=True, blank=True)
    zipCode = models.PositiveIntegerField(null=True, blank=True)
    phoneNum = models.CharField(max_length=30, null=True, blank=True)
    timeCalledIn = models.DateTimeField(null=True)
    description = models.CharField(max_length=30, null=True,blank=True)
    priority = models.PositiveIntegerField(null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class RequiredEquipment(models.Model):
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class EventStatus(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField()
    status = models.CharField(max_length=200)

class EventTicket(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    statusType = (('Resolved', 'Resolved'),
              ('Unresolved', 'Unresolved'))
    ticketStatus = models.CharField(max_length=30, choices = statusType, null=True, blank=True)
    t_type = (('Priority', 'Priority'),
              ('First_Responder','First_Responder'),
              ('Equipment', 'Equipment'))

    ticketType = models.CharField(max_length=30, choices=t_type, null=True, blank=True)
    ticketDescription =  models.CharField(max_length=50, null=True, blank=True)


class Map:
    pass

