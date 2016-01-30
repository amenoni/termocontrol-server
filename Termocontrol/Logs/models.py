from __future__ import unicode_literals

from django.db import models

class tempLog(models.Model):
    timestamp_UTC = models.DateTimeField()
    temp = models.IntegerField()


class usageLog(models.Model):
    timestamp_UTC = models.DateTimeField()
    hour = models.IntegerField()
    weekday = models.IntegerField()
