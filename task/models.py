from django.conf import settings
from django.db import models
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(
        'Название',
        max_length=settings.TASK_NAME_LEGHT
    )
    created_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        editable=False
    )
    updated_date = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
        blank=True,
    )
    scheduled_date = models.DateField(
        'Запланированная дата',
        blank=True
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('edit_task', args=[str(self.id)])
