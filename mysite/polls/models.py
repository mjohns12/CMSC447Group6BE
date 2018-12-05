from django.db import models

#Todo :add tostrings

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    branchName = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=25)

    class Meta:
        abstract = True

    def __str__(self):
        return self.firstName + " " + self.lastName

class CallCenterOperator(User):
    pass

class OperationsChief(User):
    pass

class FirstResponder(User):
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    missions = models.ManyToManyField('Mission')

class LeadFirstResponder(FirstResponder):
    pass

class FirstResponderStatus(models.Model):
    time = models.DateTimeField()
    status = models.CharField(max_length=200)
    firstResponder_id = models.ForeignKey(FirstResponder,
        on_delete=models.CASCADE)

class Equipment(models.Model):
    equipmentType = models.CharField(max_length=50)
    numberAvailable = models.PositiveIntegerField()
    events = models.ManyToManyField('Event')
    missions = models.ManyToManyField('Mission')


class Mission(models.Model):
    pass

class Event(models.Model):
    firstName = models.CharField(max_length=30, null=True, blank=True)
    lastName = models.CharField(max_length=30, null=True, blank=True)
    streetNum = models.CharField(max_length=30, null=True,blank=True)
    streetName = models.CharField(max_length=30, null=True,blank=True)
    city = models.CharField(max_length=30, null=True,blank=True)
    state = models.CharField(max_length=30,null=True, blank=True)
    zipCode = models.PositiveIntegerField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=30, null=True, blank=True)
    timeCalleIn = models.DateTimeField(null=True)
    description = models.CharField(max_length=30, null=True,blank=True)
    priorityCode = models.PositiveIntegerField(null=True)

    opChief_id = models.ForeignKey(OperationsChief, on_delete=models.CASCADE, null=True, blank=True)
    mission_id = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=True)


class EventStatus(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.CharField(max_length=200)



class Map:
    pass

