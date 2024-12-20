# Generated by Django 5.0.6 on 2024-05-23 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='DanceStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название танца')),
            ],
        ),
        migrations.CreateModel(
            name='DancerStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dancer')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dancestyle')),
            ],
        ),
    ]
