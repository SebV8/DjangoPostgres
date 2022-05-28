from django.urls import path
from .views import create_task, delete_task, list_task
urlpatterns = [
    path('', list_task),
    path('new/', create_task, name='create_task'),
    path('delete/<int:task_id>/',delete_task, name='delete_task')
]