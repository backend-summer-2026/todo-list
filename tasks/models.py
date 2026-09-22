from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    class PriorityChoices(models.TextChoices):
        low    = 'low', 'Past'
        middle = 'middle', 'O\'rta'
        high   = 'high', 'Yuqori'

    title        = models.CharField(max_length=127)
    description = models.TextField(help_text='taskni tarifini kiriting...')
    completed   = models.BooleanField(default=False, blank=True)
    priority    = models.CharField(max_length=20, blank=True, choices=PriorityChoices, default=PriorityChoices.middle, verbose_name='muhumlik darajasi')
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'user': self.user.username
        }
