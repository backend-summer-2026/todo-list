from django.urls import path

from .views import tasks_view

urlpatterns = [
    path('', tasks_view, name='tasks')
]

