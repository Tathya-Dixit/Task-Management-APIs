from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

import logging

from tasks.models import Category, Task
from tasks.serializers import CategorySerializer, TaskSerializer

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        logger.info(f"User - {self.request.user} creating category")
        serializer.save(user = self.request.user)
        logger.info(f"Category created : {serializer.instance.name}")
    
    def perform_update(self, serializer):
        logger.info(f"Updating category: {serializer.instance.name}")
        serializer.save()
        logger.info(f"Category updated: {serializer.instance.name}")
    
    def perform_destroy(self, instance):
        logger.info(f"Deleting category: {instance.name}")
        instance.delete()
        logger.info(f"Category deleted: {instance.name}")
        
    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filterset_fields = ['status', 'priority', 'category']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'priority']
    ordering = ['-created_at', '-priority']

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        logger.info(f"User - {self.request.user} creating task")
        serializer.save(user = self.request.user)
        logger.info(f"Task created : {serializer.instance.title}")
    
    def perform_update(self, serializer):
        logger.info(f"Updating task: {serializer.instance.title}")
        serializer.save()
        logger.info(f"Task updated: {serializer.instance.title}")
    
    def perform_destroy(self, instance):
        logger.info(f"Deleting task: {instance.title}")
        instance.delete()
        logger.info(f"Task deleted: {instance.title}")
        

