# Generated by Django 3.2.16 on 2022-12-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-02-12'),
            preserve_default=False,
        ),
    ]
