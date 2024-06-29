from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.models import Task
from mainApp.serializers import TaskSerializer

class MyTasksAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user).order_by('high_priority')
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

            title_search = request.query_params.get('title', None)
            created_day_order = request.query_params.get('created_at', None)
            status_order = request.query_params.get('created_at', None)

            if title_search is not None:
                tasks = tasks.filter(title__icontains=title_search)
            if created_day_order is not None:
                if created_day_order == "new":
                    tasks = tasks.order_by('-created_at')
                elif created_day_order == "old":
                    tasks = tasks.order_by('created_at')
            if status_order is not None:
                if status_order == "new":
                    tasks = tasks.filter(status="new")
                elif status_order == "in progress":
                    tasks = tasks.filter(status="In_Progress")
                elif status_order == 'complited':
                    tasks = tasks.filter(status="Complited")
        return Response(status=401)

class TaskListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

