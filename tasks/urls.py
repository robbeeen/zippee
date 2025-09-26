from django.contrib import admin
from django.urls import path
from .views import TaskView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('tasks/<int:id>/', TaskView.as_view(), name='task-detail'),
]