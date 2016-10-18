from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from judicial.models import AsesorJuridico
from judicial.serializer import AsesorSerializer

# 52aaa  cambio 589
class JSONResponse(HttpResponse):
    """
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def snippet_list(request):
    if request.method == 'GET':
        snippets = AsesorJuridico.objects.all()
        serializer = AsesorSerializer(snippets, many=True)
        return JSONResponse(serializer.data)


#hola muchis 
