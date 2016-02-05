from __future__ import unicode_literals

from django.db import models

class tempLog(models.Model):
    timestamp_UTC = models.DateTimeField()
    temp = models.FloatField()

    def __unicode__(self):
        return self.pk


class usageLog(models.Model):
    type_choices = (('st', 'Usage Started'),('fn','Usage Finished'),('nd','Not defined'))

    timestamp_UTC = models.DateTimeField()
    hour = models.IntegerField()
    weekday = models.IntegerField()
    type = models.CharField(max_length=2,choices=type_choices,default='nd')

    def __unicode__(self):
        return self.pk