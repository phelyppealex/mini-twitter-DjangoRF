from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    created = models.DateTimeField(auto_now=True)
    system_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.username
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Post(models.Model):
    created = models.DateTimeField(auto_now=True)
    text_content = models.CharField(max_length=1000)
    author = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username'
    )

    def __str__(self):
        return f"{self.text_content}"

class Like(models.Model):
    person = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username'
    )
    post = models.ForeignKey(
        Post,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.person} liked {self.post}"

class Follow(models.Model):
    following = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
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

    def __str__(self):
        return f"{self.following} follows {self.followed}"