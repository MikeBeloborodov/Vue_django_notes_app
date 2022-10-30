from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User, Note

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class NoteSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'created', 'updated', 'user']
