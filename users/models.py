from django.db import models
from django.core.validators import MinLengthValidator


class Account(models.Model):
    username   = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=64,
        validators=[MinLengthValidator(3)]
    )
    email      = models.EmailField(max_length=256)
    password   = models.CharField(max_length=256)
    first_name = models.CharField(
        max_length=64,
        validators=[MinLengthValidator(3)]
    )
    last_name  = models.CharField(
        max_length=64,
        validators=[MinLengthValidator(3)]
    )
    bio        = models.TextField(default='')
    birth_date = models.DateField()
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
