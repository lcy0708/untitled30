from rest_framework import serializers
from rest_framework import exceptions
from api.models import Employee
from untitled30 import settings

class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()