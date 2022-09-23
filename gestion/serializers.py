from rest_framework import serializers
from .models import Usuario, Registro

class RegistrarUsuarioSerializer(serializers.ModelSerializer):
    def save(self):
        nuevoUsuario = Usuario(**self.validated_data)
        nuevoUsuario.set_password(self.validated_data.get('password'))
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = Usuario
        # fields = '__all__'
        exclude = ['groups', 'user_permissions']

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'

class MostrarFigurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        exclude = ['usuario']
        depth = 2
