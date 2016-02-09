from django.contrib import admin
from .models import tempLog, usageLog
# Register your models here.


class tempLogAdmin(admin.ModelAdmin):
    list_display = ('pk','timestamp','temp')
    list_filter = ('timestamp',)

class usageLogAdmin(admin.ModelAdmin):
    list_display = ('pk','timestamp','weekday','hour','type',)
    list_filter = ('timestamp','weekday','hour','type')


admin.site.register(tempLog,tempLogAdmin)
admin.site.register(usageLog,usageLogAdmin)
