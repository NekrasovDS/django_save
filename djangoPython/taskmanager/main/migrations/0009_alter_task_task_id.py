# Generated by Django 5.0.6 on 2024-05-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='xB5BOwkfnp8LN8gKePokEDecPwBpPhV8', editable=False, max_length=32, unique=True),
        ),
    ]
