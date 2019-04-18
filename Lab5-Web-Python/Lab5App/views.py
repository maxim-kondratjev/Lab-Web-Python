from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import View

from Lab5App.models import Task


class TaskListView(ListView):
    def get(self, request):
        data = {
            'tasks': Task.objects.all().order_by('id')
        }
        return render(request, "task_list/tasks.html", data)


class TaskView(View):
    def get(self, request, id):
        print("tralalal1")
        data = {
            'task': Task.objects.get(id=id)
        }
        print("tralalal2")
        return render(request, 'task_list/task/task.html', data)
