from rest_framework import serializers
from Tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task 
        fields = 'id title descriptions completed created'.split()

class TaskValidSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    descriptions = serializers.CharField()
    completed = serializers.BooleanField()
 