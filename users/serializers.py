from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=100)
    patronymic = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    FIO = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'patronymic', 'surname', 'FIO']
