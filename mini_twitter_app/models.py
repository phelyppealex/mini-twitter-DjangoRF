from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=320, blank=False)
    password = models.CharField(max_length=30)

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
        Person,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username'
    )

    def __str__(self):
        return f"{self.text_content}"

class Like(models.Model):
    person = models.ForeignKey(
        Person,
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
        Person,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='following_set',
        
    )
    followed = models.ForeignKey(
        Person,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='followed_set'
    )

    def __str__(self):
        return f"{self.following} follows {self.followed}"