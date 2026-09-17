from django.db import models

from users.models import Account


class Task(models.Model):
    name        = models.CharField(max_length=127)
    description = models.TextField()
    completed   = models.BooleanField(default=False, blank=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
