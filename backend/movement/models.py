from django.db import models
from django.contrib.auth.models import User


class MovementChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover
        return self.title


class MovementSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(
        MovementChallenge,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    duration = models.IntegerField(help_text="Minutes moved")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:  # pragma: no cover
        return f"Session for {self.user} ({self.duration} min)"

