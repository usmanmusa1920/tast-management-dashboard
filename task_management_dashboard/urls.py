"""
URL configuration for task_management_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_management.views import landing
from task_management.views import create_view
from task_management.views import read_view
from task_management.views import update_view
from task_management.views import delete_view
from task_management.views import fetch_task
from task_management.views import login_view
from task_management.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', landing, name='landing'),
    path('create/', create_view, name='create_view'),
    path('read/<int:task_id>/', read_view, name='read_view'),
    path('update/<int:task_id>/', update_view, name='update_view'),
    path('delete/<int:task_id>/', delete_view, name='delete_view'),
    path('fetch/task/', fetch_task, name='fetch_task'),
]
