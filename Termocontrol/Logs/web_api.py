from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import usageLog, tempLog

class tempLogResourse(ModelResource):
    class Meta:
        queryset = tempLog.objects.all()
        resource_name = 'templogs'
        #todo: implement autorization
        authorization = Authorization()

class usageLogResourse(ModelResource):
    class Meta:
        queryset = usageLog.objects.all()
        resource_name = "usagelogs"
        #todo: Implement autorization
        authorization = Authorization()