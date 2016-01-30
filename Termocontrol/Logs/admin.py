from django.contrib import admin
from .models import tempLog, usageLog
# Register your models here.

admin.site.register(tempLog)
admin.site.register(usageLog)