from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble, Empresa, Persona, Interesado
from inmuebleslist_app.api.serializers import InmuebleSerializer, PersonaSerializer, InteresadoSerializer, EmpresaSerializer
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
#filter
from django_filters.rest_framework import DjangoFilterBackend
from inmuebleslist_app.api.filters import PersonaFilter


class PersonaFilteredList(generics.ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonaFilter

class EmpresaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    def get(self, request, *args,**kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)

class EmpresaDetail(
    mixins.RetrieveModelMixin,   # Para obtener un solo objeto (GET)
    mixins.UpdateModelMixin,     # Para actualizar un objeto (PUT/PATCH)
    mixins.DestroyModelMixin,    # Para eliminar un objeto (DELETE)
    generics.GenericAPIView
):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # Obtener empresa

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # Actualizar empresa

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # Actualización parcial

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # Eliminar empresa


class PersonaList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    def get(self, request, *args,**kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)
class PersonaDetail(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class InteresadoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer
    def get(self, request, *args,**kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args,**kwargs):
        return self.create(request, *args, **kwargs)
class InteresadoDetail(
    mixins.RetrieveModelMixin,  # Para obtener detalles (GET)
    mixins.UpdateModelMixin,    # Para actualizar (PUT)
    mixins.DestroyModelMixin,   # Para eliminar (DELETE)
    generics.GenericAPIView
):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InmuebleListAV(APIView):
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer= InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InmuebleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class InmuebleDetalleAV(APIView):

    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no entrando'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
    def put(self, request, pk):
        try:
            inmueble=Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no econtrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InmuebleSerializer(inmueble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        try:
            inmueble=Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'Inmueble no econtrado'}, status=status.HTTP_404_NOT_FOUND)
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

             
# @api_view(['GET', 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles=Inmueble.objects.all()
#         serializers = InmuebleSerializer(inmuebles, many=True)
#         return Response(serializers.data)
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error': 'el inmueble no existe'},status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#          inmueble = Inmueble.objects.get(pk=pk)
#          de_serializer = InmuebleSerializer(inmueble, data=request.data)
#          if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#          else:
#             return Response(de_serializer.errors)
#     if request.method == 'DELETE':
#         inmueble = Inmueble.objects.get(pk=pk)
#         inmueble.delete()
#         data = {
#             "resultado":True
#         }
#         return Response(data)