from django.shortcuts import render
from Tasks.models import Task
from Tasks.serializers import TaskSerializer,TaskValidSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.db import transaction

class TaskListApiView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = TaskValidSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        title = serializer.validated_data.get('title')
        descriptions = serializer.validated_data.get('descriptions')
        completed = serializer.validated_data.get('completed')
        created = serializer.validated_data.get('created')
        with transaction.atomic():
            task = Task.objects.create(title=title,descriptions=descriptions,completed=completed,created=created)
            task.save()
            return Response(data ={'task_id' : task.id }, status = status.HTTP_201_CREATED)
        
class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'


