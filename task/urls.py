from django.urls import path

from .views import TaskCreateView, home

app_name = 'task'


urlpatterns = [
    path('', home, name='home'),
    path('new_task/', TaskCreateView.as_view(), name='new_task'),
]
