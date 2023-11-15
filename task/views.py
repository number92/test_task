from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from .forms import TaskForm
from .models import Task


def home(request):
    template = 'index.html'
    context = {'task_list': Task.objects.all()}
    return render(request, template, context)


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('task:home')
