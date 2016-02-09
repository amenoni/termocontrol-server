from __future__ import unicode_literals

from django.db import models

class tempLog(models.Model):
    timestamp = models.DateTimeField()
    temp = models.FloatField()

    def __unicode__(self):
        return str(self.pk)


class usageLog(models.Model):
    type_choices = (('st', 'Usage Started'),('fn','Usage Finished'),('nd','Not defined'))

    timestamp = models.DateTimeField()
    hour = models.IntegerField()
    weekday = models.IntegerField()
    type = models.CharField(max_length=2,choices=type_choices,default='nd')

    def __unicode__(self):
        return str(self.pk)
