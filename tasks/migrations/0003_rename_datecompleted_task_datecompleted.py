# Generated by Django 5.1.4 on 2024-12-05 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_datecompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dateCompleted',
            new_name='datecompleted',
        ),
    ]
