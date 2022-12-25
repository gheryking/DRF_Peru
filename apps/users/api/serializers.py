from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        # Todos los campos
        fields = '__all__'
        # campos especificos
        #fields = ['name', 'last_name', 'email']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


#class TestUserSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=200)
#    email = serializers.EmailField()

        #    def validate_name(self, value):
        # Custom Validation
        #        if 'develop' in value:
        #            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')

        #print('aqui el contexto serializer')
        #print(self.context)

    #        return value

        #    def validate_email(self, value):
        # Custom Validation
        #        if value == '':
        #            raise serializers.ValidationError('Error, Tiene que indicar un correo electronico')

        #        if self.validate_name(self.context['name']) in value:
        #            raise serializers.ValidationError('Error, El correo electronico no puede contener el nombre')

    #        return value

        #    def validate(self, data):
        #if data['name'] in data['email']:
        #    raise serializers.ValidationError("El email no puede contener el nombre")
    #        return data

        #    def create(self, validated_data):
    #        return User.objects.create(**validated_data)

        #    def update(self, instance, validated_data):
        #        instance.name = validated_data.get('name', instance.name)
        #        instance.email = validated_data.get('email', instance.email)
        #        instance.save()
#        return instance