from django.db import models
from user_profile_app.models import UserProfile
from post_app.models import Post

class Like(models.Model):
    person = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        to_field='username'
    )
    post = models.ForeignKey(
        Post,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='liked_by'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['person', 'post'], name='unique_like')
        ]

    def __str__(self):
        return f"{self.person} liked {self.post}"