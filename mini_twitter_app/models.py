from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=30)
    following = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='followed_users'
    )

    def __str__(self):
        return self.username

class Post(models.Model):
    created = models.DateTimeField(auto_now=True)
    text_content = models.CharField(max_length=1000)
    author = models.ForeignKey(
        Person,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

class Like(models.Model):
    person = models.ForeignKey(
        Person,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
