from django.db import models
from django.utils.crypto import get_random_string


class Task(models.Model):
    task_id = models.CharField(max_length=32, unique=True, editable=False, default=get_random_string(length=32))
    title = models.CharField('Обращение', max_length=50)
    task = models.TextField('Данные')

    def __str__(self):
        return self.task_id

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


class TaskCheck(models.Model):
    task_tag = models.CharField(max_length=32)


class Dancer(models.Model):
    first_name = models.CharField('Имя', max_length=25)
    last_name = models.CharField('Фамилия',max_length=25)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Танцор'
        verbose_name_plural = 'Танцоры'


class DanceStyle(models.Model):
    name = models.CharField('Название танца', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'


class DancerStyle(models.Model):
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    style = models.ForeignKey(DanceStyle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Выступление'
        verbose_name_plural = 'Выступление'