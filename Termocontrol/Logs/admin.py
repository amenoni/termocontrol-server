from django.contrib import admin
from .models import tempLog, usageLog
# Register your models here.


class tempLogAdmin(admin.ModelAdmin):
    list_display = ('pk','timestamp_UTC','temp')
    list_filter = ('timestamp_UTC',)

class usageLogAdmin(admin.ModelAdmin):
    list_display = ('pk','timestamp_UTC','weekday','hour','type',)
    list_filter = ('timestamp_UTC','weekday','hour','type')


admin.site.register(tempLog,tempLogAdmin)
admin.site.register(usageLog)