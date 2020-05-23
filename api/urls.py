from django.urls import path 
from .views import apiOverview , taskDelete , taskUpdate , taskCreate ,taskList,taskDetail

urlpatterns = [
    path('',apiOverview , name='api-overview'),
    path('task-list/',taskList , name='task-list'),
    path('task-detail/<str:pk>/',taskDetail , name='task-detail'),
    path('task-create/', taskCreate , name='task-create'),
    path('task-update/<str:pk>/', taskUpdate , name='task-update'),
    path('task-delete/<str:pk>/', taskDelete , name='task-delete'),
]
