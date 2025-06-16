from django.db import models


class GeneratedImage(models.Model):
    response = models.ForeignKey(
        "prompts.PromptResponse", on_delete=models.CASCADE
    )
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover
        return self.image_url


class SocialPost(models.Model):
    image = models.ForeignKey(GeneratedImage, on_delete=models.CASCADE)
    caption = models.TextField()
    shared_to = models.CharField(
        max_length=50, help_text="e.g., 'instagram', 'twitter'"
    )
    shared_at = models.DateTimeField(null=True, blank=True)
    was_successful = models.BooleanField(default=False)

    def __str__(self) -> str:  # pragma: no cover
        return f"Post to {self.shared_to}"

