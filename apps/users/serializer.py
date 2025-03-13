from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "phome_num",)

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_lenght = 155, write_only = True)
    password_2 = serializers.CharField(max_lenght = 155, write_only = True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_num', 'email', 'password', 'password_2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError({'password' : 'Пароль не совподает'})
        if '+996' not in attrs['phone_num']:
            raise serializers.ValidationError('Номер должен быть в формате +996')
        return attrs
        
    def create(self, values):
        user = User.objects.create(
            username = values['username'], first_name=values['first_name'], last_name=values['last_name']
            phone_num = values['phone_num'], email=values['email']
        )
        user.set_password(values{'password'})
        user.save()
        return user