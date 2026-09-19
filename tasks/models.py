from django.db import models

from users.models import Account


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

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tasks')


class Item(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
