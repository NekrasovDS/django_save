# Generated by Django 5.0.6 on 2024-05-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_dancerstyle_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='a1S0iMgyYGiQiuXORZJ1WBH8OOyHuRud', editable=False, max_length=32, unique=True),
        ),
    ]