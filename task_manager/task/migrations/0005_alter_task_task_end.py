# Generated by Django 4.0.4 on 2022-06-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_task_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_end',
            field=models.DateTimeField(null=True),
        ),
    ]
