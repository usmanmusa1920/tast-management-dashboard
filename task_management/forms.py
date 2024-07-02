from django import forms
from .models import TaskModel


class UpdateTask(forms.ModelForm):
    """Update task form"""
    
    class Meta:
        model = TaskModel
        fields = ['description', 'title', 'status', 'priority', 'category']