from tastypie.resources import ModelResource
from artourquito.models import MonumentosQuito 
from tastypie.authorization import Authorization

from tastypie.constants import ALL

class MonumentosQuitoResource(ModelResource):
    class Meta:
        queryset = MonumentosQuito.objects.all()
        resource_name = 'monumentosquito'
        authorization = Authorization()
        filtering = {
        'mid': ['icontains']
    }

 