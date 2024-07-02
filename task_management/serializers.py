from rest_framework import serializers
from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer"""
    
    class Meta:
        model = TaskModel
        fields = '__all__'
