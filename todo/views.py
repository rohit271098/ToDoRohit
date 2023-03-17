from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class TaskList(ListView):              # here template name is given by browser
    model = Task
    context_object_name = 'task'       # used in task_list.html line 7
        
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'       # used in task.html
    template_name = 'todo/task.html'   # to give our oun template name

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task-list')  # when we click the button redirects to 'task' in urls.py line 5.
    