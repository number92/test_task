# Generated by Django 4.2.7 on 2023-11-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_scheduled_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='scheduled_date',
            field=models.DateField(blank=True, verbose_name='Запланированная дата'),
        ),
    ]