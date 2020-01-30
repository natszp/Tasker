from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import View
from manager.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class MainView(View):

    def get(self, request):
        tasks_list = Task.objects.order_by('-date_created')
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

        task_counter = Task.objects.count()

        return render(request, 'tasks.html', context={'task_counter': task_counter, 'tasks': tasks})

class DetailsView(View):

    def get(self, request, id):
        id = int(id)
        tasks = Task.objects.filter(id=id)

        return render(request, 'details.html', context={'tasks':tasks})


class AddTaskView(View):

     def get(self, request):
        return render(request, 'add.html')

     def post(self, request):

        name = request.POST.get('name')
        description = request.POST.get('description')
        importance = request.POST.get('importance')
        if importance == 'on':
            importance = True
        else:
            importance = False

        Task.objects.create(name=name, description=description, importance=importance)
        return redirect('tasks')

class UpdateTaskView(View):

     def get(self, request, id):
        return render(request, 'update.html')

     def post(self, request, id):

        name = request.POST.get('name')
        description = request.POST.get('description')
        importance = request.POST.get('importance')
        if importance == 'on':
            importance = True
        else:
            importance = False

        Task.objects.filter(id=id).update(name=name, description=description, importance=importance)
        return redirect('tasks')

class DeleteTaskView(View):

    def get(self, request, id):
        Task.objects.get(id=id).delete()
        return redirect('tasks')
