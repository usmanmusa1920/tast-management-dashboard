from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class TaskModel(models.Model):
    """Task model"""

    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)

    status_choices = [('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Overdue', 'Overdue')]
    status = models.CharField(max_length=255, blank=False, null=False, choices=status_choices)

    priority_choices = [('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    priority = models.CharField(max_length=255, blank=False, null=False, choices=priority_choices)

    category = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return f'Task model with ID number of {self.id}'
