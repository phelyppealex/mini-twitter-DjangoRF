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
    
    def follower_count(self):
        return self.followed_set.count()
    
    def following_count(self):
        return self.following_set.count()

    def __str__(self):
        return self.username