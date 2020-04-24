from tastypie.resources import ModelResource
from inicio.models import *

class ArchivoResource(ModelResource):
    class Meta:
        queryset = Archivo.objects.all()
        resource_name = 'archivo'