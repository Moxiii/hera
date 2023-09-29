from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='user'
    )
    def __str__(self):
        return f"name: {self.username}, token: {str(self.token)}"