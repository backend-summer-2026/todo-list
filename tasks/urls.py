from django.urls import path

from .views import tasks_view, task_details_view

urlpatterns = [
    path('', tasks_view, name='tasks'), # tasks/
    path('<int:id>', task_details_view, name='task-details') # tasks/id
]

