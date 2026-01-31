from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Task(models.Model):

    class Priority(models.IntegerChoices):
        LOW = 0, 'Low'
        NORMAL = 1, 'Normal'
        HIGH = 2, 'High'

    class Status(models.TextChoices):
        PENDING = 'PE', 'Pending'
        IN_PROGRESS = 'IP', 'In Progress'
        DONE = 'DO', 'Done'
        ARCHIVED = 'AR', 'Archived'

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='tasks')
    priority = models.IntegerField(choices=Priority.choices, default=Priority.NORMAL)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
    

