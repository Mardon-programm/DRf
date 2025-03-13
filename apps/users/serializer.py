from rest_framework import serializers

from apps.user.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 'created_at')
        
        
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100,
        write_only = True
    )
    password2 = serializers.CharField(
        max_length=100,
        write_only = True
    )
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': "Пароли отличаются"})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")
        return attrs
    
    def create(self, values):
        user = Users.objects.create(
            username=values['username'], phone_number=values['phone_number'],
            email=values['email'],
        )
        user.set_password(values['password'])
        user.save()
        return user
