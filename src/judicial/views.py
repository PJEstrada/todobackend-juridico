from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
#from django_statsd.clients import statsd
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from judicial.models import *
from judicial.serializer import *
from rest_framework.decorators import api_view
from django.core.exceptions import MultipleObjectsReturned
<<<<<<< HEAD
import requests
import json
=======
>>>>>>> 8a20665e109348968eb9f92831e9221cad917bf4

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

# gerencia2
@api_view(['POST'])
def crear_gerencia(request):
    if request.method == 'POST':
        serializer = GerenciaSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar la gerencia
            instance.numero_instancia = instance.pk
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

@api_view(['GET'])
def obtener_expediente(request, id):
    if request.method == 'GET':
        id_expediente = id
        # Cargar expedientes de otro servicio
        expediente_servicio = requests.post('http://52.86.239.149/users/expediente_view',
                                    data=json.dumps({'correlativo': id_expediente})).json()
        expediente_encontrado = None;
        try:
            expediente_encontrado = expediente_servicio["Expediente"]
        except KeyError as error:
            # Si por alguna razon no lo encuentra devuelve vacio
            return JSONResponse([])
        try:
            expediente_local = Expediente.objects.get(pk = int(expediente_encontrado["correlativo"]))
            expediente_local.descripcion = str(expediente_encontrado)
            expediente_local.save()
            expediente = ExpedienteJuridico.objects.get(expediente=id_expediente)

            serializer = ExpedienteSerializer(expediente, many=False)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No existe el dictamen
            return JSONResponse([])

@api_view(['GET'])
def expedientes_dado_asesor(request,id):
    # TODO: Pegarle al endpoint que Neto debe para poder jalar todos los expedientes
    # Si no existe crear primero Expediente y luego Expediente Juridico.
    if request.method == 'GET':
        id_asesor = id
        try:
            expedientes = ExpedienteJuridico.objects.filter(solicitante=id_asesor)
            serializer = ExpedienteSerializer(expedientes, many=True)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist as e:
            #No hay
            return JSONResponse([])
#CREATE
@api_view(['POST'])
def crear_opinion(request):
    if request.method == 'POST':
        serializer = OpinionSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar la opinion
            instance.numero_instancia = instance.pk
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_dictamen(request):
    if request.method == 'POST':
        serializer = DictamenSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar el dictamen
            instance.numero_instancia = instance.pk
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#-------------------------------------------------------------------------------
@api_view(['POST'])
def crear_estado(request):
    if request.method == 'POST':
        serializer = EstadoSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar el estado
            instance.numero_instancia = instance.pk
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def crear_usuario(request):
    if request.method == 'POST':
        serializer = AsesorSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar el usuario
            instance.numero_instancia = instance.pk
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def emitir_providencia(request):
    if request.method == 'POST':
        serializer = ProvidenciaSerializer(data=request.data) #
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar la providencia
            instance.numero_instancia = instance.pk
            instance.save()
            #TODO cambiar el estado al expediente
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def crear_expediente(request):
    if request.method == 'POST':
        serializer = ExpedienteSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()   #gaurdar el expediente
            instance.numero_instancia = instance.pk
            instance.save()
            #statsd.incr('expedientes_sit.creados')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#UPDATE
@api_view(['PUT','POST','GET'])
def update_estado_expediente(request, id):
    try:
        expediente = ExpedienteJuridico.objects.get(id=id)
    except ObjectDoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Se obtiene el id del asesor que hace todo el tramite
        id_asesor = ExpedienteJuridico.solicitante
        id_expediente_original = ExpedienteJuridico.expediente
        # En teoria ya deberian existir la providencia, opinion y dictamen
        providencia_relacionada = Providencia.objects.get(expediente=expediente.pk)
        opinion_relacionada = Opinion.objects.get(expediente=expediente.pk)
        dictamen_relacionada = Dictamen.objects.get(expediente=expediente.pk)
        dictionario_retorno = {'providencia_texto': providencia_relacionada.descripcion, 'opinion_texto': opinion_relacionada.descripcion,
                                'dictamen_texto': dictamen_relacionada.descripcion}
        dictionario_string_retorno = str(dictionario_retorno)

        creacion_acta = requests.post('http://52.86.239.149/users/acta_new',
                                    data=json.dumps({'id_expediente': id_expediente_original, "asunto": "Revision juridica", "firma": "AsesorJuridico"+str(id_asesor)})).json()
        actualizacion_datos = requests.post('http://52.86.239.149/users/expediente_edit',
                                data=json.dumps({"documentos":dictionario_string_retorno})).json()
        # Se le pega al endopoint de neto para actualizar su log
        if 'solicitante' not in request.data:
            request.data['solicitante'] = expediente.solicitante.pk
        if 'key' not in request.data:
            request.data['key'] = expediente.key
        if 'numero' not in request.data:
            request.data['numero'] = expediente.numero
        serializer = ExpedienteSerializer(expediente, data=request.data)
        if serializer.is_valid():
            serializer.save()   #gaurdar la opinion
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
