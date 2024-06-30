from django.utils.html import format_html
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth import get_user_model
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from .models import TaskModel


User = get_user_model()


def login_view(request):
    """Account login view function"""
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticating user
        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, f'You are logged in!')
            login(request, user)
            return redirect('landing')
        
        messages.warning(request, f'Re-check your login credentials, note that both fields may be case-sensitive.')
        return redirect('login')
    
    context = {
        'None': None,
    }
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logout_view(request):
    """Account logout function view"""
    
    logout(request)
    messages.success(request, f'You just logged out!')
    return redirect('login')


def landing(request):
    """Landing view"""
    
    context = {
        'None': None,
    }
    return render(request, 'landing.html', context)


def create_view(request):
    """Create view"""
    
    context = {
        'None': None,
    }
    return render(request, 'create.html', context)


def read_view(request, task_id):
    """Read view"""
    
    context = {
        'None': None,
    }
    return render(request, 'read.html', context)


def update_view(request, task_id):
    """Update view"""
    
    context = {
        'None': None,
    }
    return render(request, 'update.html', context)


def delete_view(request, task_id):
    """Delete view"""
    
    context = {
        'None': None,
    }
    return render(request, 'delete.html', context)


def fetch_task(request):
    """API endpoints to fetch tasks based on their status (In Progress, Completed, Overdue)"""
    
    context = {
        'None': None,
    }
    return render(request, 'fetch.html', context)
