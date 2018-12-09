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
    assignedMissionID = models.ManyToManyField('Mission', null=True, blank = True)
    occupation = models.CharField(max_length=100)

class LeadFirstResponder(FirstResponder):
    pass

class FirstResponderStatus(models.Model):
    time = models.DateTimeField()
    status = models.CharField(max_length=200)
    firstResponder_id = models.ForeignKey(FirstResponder,
        on_delete=models.CASCADE)

class Equipment(models.Model):
    equipmentType = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    events = models.ManyToManyField('Event', null=True, blank=True)
    missions = models.ManyToManyField('Mission', null=True, blank=True)


class Mission(models.Model):
    pass

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
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, null=True, blank=True)


class EventStatus(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.CharField(max_length=200)


class Map:
    pass

