from re import A
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.request import Request
from .serializers import RegistrarUsuarioSerializer, RegistroSerializer, MostrarFigurasSerializer
from rest_framework.response import Response
from rest_framework import status
from .enviar_correos import enviar_correo_validacion
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permisons import PermisoPersonalizado, EsAdministrador
from .models import Registro

class RegistroUsuarioView(CreateAPIView):
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdministrador]

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()

        enviar_correo_validacion(data.data.get('correo'))

        return Response(data={
            'message': 'Usuario creado exitosamente',
            'content': ''
        }, status=status.HTTP_201_CREATED)

class RegistroFiguritasView(ListCreateAPIView):
    permission_classes = [PermisoPersonalizado]
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    def get(self, request):
        id_usuario = request.user.id
        registros = self.get_queryset().filter(usuario = id_usuario).all()
        print(registros)

        return Response(data={
            'message': 'Tu coleccion es:',
            'content': MostrarFigurasSerializer(instance=registros, many=True).data
        })
    
    def post(self, request):
        id_usuario = request.user.id
        data = {**request.data, **{'usuario': id_usuario}}
        registroSerializado = self.serializer_class(data=data)
        registroSerializado.is_valid(raise_exception=True)
        nuevoRegistro = registroSerializado.save()

        return Response(data={
            'message': 'Registro creado exitosamente',
            'content': self.serializer_class(instance=nuevoRegistro).data
        })
