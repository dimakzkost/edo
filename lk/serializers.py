from lk.models import lk
from rest_framework import serializers


class lkSerializer(serializers.ModelSerializer):
    time_add = serializers.DateTimeField()
    user_id = serializers.CharField(source='users.id', read_only=True)

    class Meta:
        model = lk
        fields = ['time_add', 'user_id']
