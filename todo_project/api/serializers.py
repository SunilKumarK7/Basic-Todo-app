from rest_framework import serializers
from api.models import ToDo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]
        
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields="__all__"
        read_only_fields=["id","created_date","update_date","is_active","owner"]