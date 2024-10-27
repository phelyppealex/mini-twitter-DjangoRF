from django.db import models
from user_profile_app.models import UserProfile

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

    def liked_count(self):
        return self.liked_by.count()
    
    def __str__(self):
        return f"{self.text_content}"