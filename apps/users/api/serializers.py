from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        # Todos los campos
        fields = '__all__'
        # campos especificos
        #fields = ['name', 'last_name', 'email']


class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        # Custom Validation
        if 'develop' in value:
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')

        #print('aqui el contexto serializer')
        #print(self.context)

        return value

    def validate_email(self, value):
        # Custom Validation
        if value == '':
            raise serializers.ValidationError('Error, Tiene que indicar un correo electronico')

        #print(self.context['name'])

        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('Error, El nombre no puede estar en el correo electronico')

        return value

    def validate(self, data):
        #if data['name'] in data['email']:
        #    raise serializers.ValidationError("El email no puede contener el nombre")
        return data
