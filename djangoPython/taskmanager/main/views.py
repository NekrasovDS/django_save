from django.shortcuts import render, redirect
from .models import Task, Dancer, DanceStyle, DancerStyle, TaskCheck
from .form import TaskForm, TaskIdForm
from django.http import HttpResponseRedirect


tasks = Task.objects.all()
taskchecks = TaskCheck.objects.all()


def index(request):
    dancers = Dancer.objects.all()
    styles = DanceStyle.objects.all()
    performance = DancerStyle.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'performance': performance})


def about(request):
    return render(request, 'main/about.html')


def task_tag(request):
    error = ''
    if request.method == 'POST':
        form = TaskIdForm(request.POST)
        if form.is_valid():
            for obj in Task.objects.get():
                if TaskCheck.objects.get(task_tag) == obj:
                    update(request, )
                    return redirect('update')
            form.save()
        else:
            error = 'Форма была неверной'

    form = TaskIdForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/task_tag.html', context)


def update(request, task_id):
    if task_id is None:
        return redirect('home')  # Перенаправить на список задач, если task_id отсутствует

    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task_id': task_id,
    }
    return render(request, 'update.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)


