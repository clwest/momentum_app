from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extended profile information for a user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=64)
    bio = models.TextField(blank=True)
    streak_count = models.IntegerField(default=0)
    last_active = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return self.display_name or self.user.username

