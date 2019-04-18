from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import View


class TaskListView(ListView):
    def get(self, request):
        data = {
            'tasks': [
                {'title': "Первая задача", 'id': 1},
                {'title': "Вторая задача", 'id': 2},
                {'title': "Третья задача", 'id': 3}
            ]
        }
        return render(request, "../../Lab4/templates/task_list/tasks.html", data)


class TaskView(View):
    def get(self, request, id):
        data = {
            'task': {
                'id': id
            }
        }
        return render(request, '../../Lab4/templates/task_list/task/task.html', data)
