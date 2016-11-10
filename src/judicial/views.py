from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from judicial.models import *
from judicial.serializer import *
from rest_framework.decorators import api_view

# cambio asd658886645455552aaa  cambio 589

parser_classes = (FileUploadParser,)

class JSONResponse(HttpResponse):
    """
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#class AsesorViewSet(viewsets.ModelViewSet):
#    queryset = AsesorJuridico.objects.all()
#    serializer_class = AsesorSerializer

#class AsesorViewSet2(viewsets.ModelViewSet):
@api_view(['GET'])
def asesores(request):
    if request.method == 'GET':
        snippets = AsesorJuridico.objects.all()
        serializer = AsesorSerializer(snippets, many=True)
        return JSONResponse(serializer.data)


#TODO
#Demas funciones requeridas por el API SIT de microservicios
#La verificacion se hara mediante comunicacion con el Subdominio Correspondiente!
@api_view(['GET'])
def estados(request):
    if request.method == 'GET':
        estados = EstadoExpediente.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return JSONResponse(serializer.data)

#READ
@api_view(['GET'])
def dictamen_dado_expediente(request, id):
    if request.method == 'GET':
        id_expediente = id
        try:
            dictamen = Dictamen.objects.get(expediente_id=id_expediente)
            serializer = DictamenSerializer(dictamen, many=False)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No existe el dictamen
            return JSONResponse([])

@api_view(['GET'])
def opinion_dado_expediente(request, id):
    if request.method == 'GET':
        id_expediente = id
        try:
            opinion = OpinionJuridica.objects.get(expediente_id=id_expediente)
            serializer = OpinionSerializer(opinion, many=False)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No existe el dictamen
            return JSONResponse([])

@api_view(['GET'])
def obtener_expediente(request, id):
    if request.method == 'GET':
        id_expediente = id
        try:
            opinion = ExpedienteJuridico.objects.get(id=id_expediente)
            serializer = ExpedienteSerializer(opinion, many=False)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No existe el dictamen
            return JSONResponse([])

@api_view(['GET'])
def providencia_dado_expediente(request, id):
    if request.method == 'GET':
        id_expediente = id
        try:
            providencia = Providencia.objects.get(expediente_id=id_expediente)
            serializer = ProvidenciaSerializer(providencia, many=False)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No existe la providencia
            return JSONResponse([])
#CREATE
@api_view(['POST'])
def crear_opinion(request):
    if request.method == 'POST':
        serializer = OpinionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #gaurdar la opinion
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def expedientes_dado_asesor(request,id):
    if request.method == 'GET':
        id_asesor = id
        try:
            expedientes = ExpedienteJuridico.objects.filter(solicitante=id_asesor)
            serializer = ExpedienteSerializer(expedientes, many=True)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No hay
            return JSONResponse([])

@api_view(['POST'])
def crear_dictamen(request):
    if request.method == 'POST':
        serializer = DictamenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #gaurdar el dicatamen
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def emitir_providencia():
    if request.method == 'POST':
        serializer = ProvidenciaSerializer(data=request.data) #
        if serializer.is_valid():
            serializer.save()   #gaurdar la providencia
            #TODO cambiar el estado al expediente
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_expediente(request):
    if request.method == 'POST':
        serializer = ExpedienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #gaurdar el expediente
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



#UPDATE
@api_view(['PUT'])
def update_estado_expediente(request, id):
    try:
        expediente = ExpedienteJuridico.objects.get(id=id)
    except ObjectDoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ExpedienteSerializer(expediente, data=request.data)
        if serializer.is_valid():
            serializer.save()   #gaurdar la opinion
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
