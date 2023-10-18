from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    return Response('API BASE POINT')


@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    
    return Response(serializer.data)