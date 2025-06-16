from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return self.text[:50]


class PromptResponse(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField()
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover
        return f"Response by {self.user} to {self.prompt}"

