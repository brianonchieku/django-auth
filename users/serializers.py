from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    
        
        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])  # Hash password
            return User.objects.create(**validated_data)
 