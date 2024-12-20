from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('create', views.create, name="create"),
    path('update', views.update, name='update'),
    path('task_tag', views.task_tag, name='task_tag'),
]
