from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework import views
from .models import Task
from rest_framework.response import Response

from tasks.serializers import TaskSerializer
from rest_framework import status
from rest_framework import pagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from zippee_assessment.permissions import AdminPermission, ManagerPermission, UserPermission
from django.db.models import Q

class TaskListPagination(pagination.CursorPagination):
    ordering = '-created_at'
    page_size = 10


class TaskView(views.APIView):

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [AllowAny]

        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated, UserPermission]

        elif self.request.method == 'PUT':
            permission_classes = [IsAuthenticated, ManagerPermission]

        elif self.request.method == 'DELETE':
            permission_classes = [IsAuthenticated, ManagerPermission]
        else:
            permission_classes = [IsAuthenticated, AdminPermission]
        
        return [permission() for permission in permission_classes]
    

    def get(self, request, id=None):
        if id is not None:
            try:
                task = Task.objects.get(id=id)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.all()
            
            filters = Q()
            
            completed = request.query_params.get('completed')

            if completed is not None:
                if completed.lower() in ['true', '1']:
                    filters &= Q(completed=True)

                elif completed.lower() in ['false', '0']:
                    filters &= Q(completed=False)
            
            search = request.query_params.get('search')
            if search:
                filters &= (Q(title__icontains=search) | Q(description__icontains=search))
            
            if filters:
                filtered_tasks = tasks.filter(filters)
            else:
                filtered_tasks = tasks

            total_tasks = Task.objects.count()
            completed_tasks = Task.objects.filter(completed=True).count()
            incomplete_tasks = Task.objects.filter(completed=False).count()
            paginator = TaskListPagination()
            paginated_tasks = paginator.paginate_queryset(filtered_tasks, request)
            serializer = TaskSerializer(paginated_tasks, many=True)
            response = paginator.get_paginated_response(serializer.data)
            response.data['task_summary'] = {
                'total_tasks': total_tasks,
                'completed_tasks': completed_tasks,
                'incomplete_tasks': incomplete_tasks,
                'filtered_count': filtered_tasks.count()
            }
            
            return response
        
        
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        task = get_object_or_404(Task, id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    