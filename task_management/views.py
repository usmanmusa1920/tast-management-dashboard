from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
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
from rest_framework import generics
from .serializers import TaskSerializer
from .models import TaskModel
from .forms import UpdateTask


User = get_user_model()


class TaskListView(generics.ListAPIView):
    """Task list view"""

    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer



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


@login_required
def logout_view(request):
    """Account logout function view"""
    
    logout(request)
    messages.success(request, f'You just logged out!')
    return redirect('login')


def landing(request):
    """Landing view"""
    
    in_progress = TaskModel.objects.filter(status='In Progress').order_by('-due_date')
    completed_task = TaskModel.objects.filter(status='Completed').order_by('-due_date')
    over_due = TaskModel.objects.filter(status='Overdue').order_by('-due_date')

    context = {
        'in_progress': in_progress,
        'completed_task': completed_task,
        'over_due': over_due,
    }
    return render(request, 'landing.html', context)


@login_required
def create_view(request):
    """Create view"""
    
    if request.method == 'POST':
        form = UpdateTask(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.assigned_to = request.user
            instance.save()

            messages.success(request, f'Your just add new task!')
            return redirect('landing')
    else:
        form = UpdateTask()
    
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def read_view(request, task_id):
    """Read view"""
    
    read_task = TaskModel.objects.get(id=task_id)

    context = {
        'read_task': read_task,
    }
    return render(request, 'read.html', context)


@login_required
def update_view(request, task_id):
    """Update view"""
    
    update_task = TaskModel.objects.get(id=task_id)

    # grant permission to update task, for the user who created it
    if update_task.assigned_to != request.user:
        return False
    
    if request.method == 'POST':
        form = UpdateTask(request.POST, instance=update_task)
        
        # form validation
        if form.is_valid():
            form.save()
            messages.success(request, f'Your task has been updated!')
            return redirect('landing')
    else:
        form = UpdateTask(instance=update_task)
    
    context = {
        'update_task': update_task,
        'form': form,
    }
    return render(request, 'update.html', context)


@login_required
def delete_view(request, task_id):
    """Delete view"""
    
    delete_task = TaskModel.objects.get(id=task_id)
    
    # grant permission to delete task, for the user who created it
    if delete_task.assigned_to != request.user:
        return False
    
    context = {
        'delete_task': delete_task,
    }
    return render(request, 'delete.html', context)


@login_required
def delete_view_api(request, task_id):
    """Delete view"""
    
    delete_api_task = TaskModel.objects.get(id=task_id)
    
    # grant permission to delete task, for the user who created it
    if delete_api_task.assigned_to != request.user:
        return False
    else:
        delete_api_task.delete()
    
    delete_api_task.delete()

    messages.success(request, f'Sucessfully deleted a task with the ID ({delete_api_task})')
    return redirect('landing')


def fetch_task(request, base_on):
    """API endpoints to fetch tasks based on their status (In Progress, Completed, Overdue)"""
    
    # ensure the the filter data to be either one of the below condition
    _status_ = ['In Progress', 'Completed', 'Overdue']
    _priorities_ = ['High', 'Medium', 'Low']
    _categories_ = ['UX Design', 'Development', 'UI Design']

    # making sure the query pattern is ineither of the above 3 list
    if base_on in _status_ or base_on in _priorities_ or base_on in _categories_:
        pass
    else:
        return False
    
    # here, fetching task base on status, priority, or category
    if base_on in _status_:
        fetch_api = TaskModel.objects.filter(status=base_on).order_by('-due_date')
    elif base_on in _priorities_:
        fetch_api = TaskModel.objects.filter(priority=base_on).order_by('-due_date')
    elif base_on in _categories_:
        fetch_api = TaskModel.objects.filter(category=base_on).order_by('-due_date')

    # pagination
    paginator = Paginator(fetch_api, 10)
    page = request.GET.get('fetch_page')
    fetch_api_page = paginator.get_page(page)

    context = {
        'base_on': base_on,
        'fetch_api_page': fetch_api_page,
    }
    return render(request, 'fetch.html', context)


def search_task(request):
    """Search tasks"""

    search_panel = request.GET.get('search_tsk')

    try:
        task_search = TaskModel.objects.filter(
            Q(title__istartswith=search_panel) | Q(title__contains=search_panel) | Q(description__istartswith=search_panel) | Q(description__contains=search_panel)).order_by('-due_date')
    except:
        task_search = TaskModel.objects.filter(Q(title=search_panel) | Q(description=search_panel)).order_by('-due_date')

    # pagination
    paginator = Paginator(task_search, 10)
    page = request.GET.get('search_page')
    task_searches = paginator.get_page(page)

    context = {
        'task_searches': task_searches,
        'search_panel': search_panel,
    }
    return render(request, 'search.html', context)
