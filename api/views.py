from  django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

@api_view(['GET'])
# this is just an overview of the api address
def apiOverview(request):
    app_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    
    return Response(app_urls)


@api_view(['GET'])
# """this class based api view will 
# list all the objects in 
# in our task db"""
def taskList(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)    



@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
       serializer.save()

    return Response(serializer.data)    

@api_view(['POST'])
#set an instance
def taskUpdate(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer( instance = task ,data=request.data)

    if serializer.is_valid():
       serializer.save()

    return Response(serializer.data)      

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id = pk)
    task.delete()

    return Response('item succesfully deleted')        




