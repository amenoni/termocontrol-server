from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import usageLog, tempLog

class tempLogResourse(ModelResource):
    class Meta:
        always_return_data = True
        queryset = tempLog.objects.all()
        resource_name = 'templogs'
        authorization = Authorization()