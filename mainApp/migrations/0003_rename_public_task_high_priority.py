# Generated by Django 5.0.6 on 2024-06-29 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_task_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='public',
            new_name='high_priority',
        ),
    ]
