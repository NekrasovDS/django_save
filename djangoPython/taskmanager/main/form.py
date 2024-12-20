from .models import Task, TaskCheck
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема обращения',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Обращение',
            }),
        }


class TaskIdForm(ModelForm):
    class Meta:
        model = TaskCheck
        fields = ["task_tag"]
        widgets = {
            "task_tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Индивидуальный ключ обращения',
            }),
        }
