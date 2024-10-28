from django.db import models
from user_profile_app.models import UserProfile

class Follow(models.Model):
    following = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='following_set',
    )
    followed = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='followed_set'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following', 'followed'], name='unique_follow')
        ]

    def __str__(self):
        return f"{self.following} follows {self.followed}"