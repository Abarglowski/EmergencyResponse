from django.db import models
from django.urls import reverse
# Create your models here.
class JobCode(models.Model):
    jobCode = models.TextField()
    description = models.TextField()
    hourlyRate = models.IntegerField()
    maxHoursPerDay = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.jobCode

    def get_absolute_url(self):
        return reverse('TimeClock:###', kwargs={'pk': self.pk})

class Machine(models.Model):
    machineCode = models.TextField()
    description = models.TextField()
    hourlyRent = models.IntegerField()
    maxHoursPerDay = models.IntegerField()
    
    def __unicode__(self):
        return u'%s' % self.machineCode

    def get_absolute_url(self):
        return reverse('TimeClock:###', kwargs={'pk': self.pk})

class Timecard(models.Model):
    siteCode = models.TextField()
    contractorName = models.TextField()
    totalHours = models.IntegerField()
    totalAmount = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.siteCode

    def get_absolute_url(self):
        return reverse('TimeClock:###', kwargs={'pk': self.pk})