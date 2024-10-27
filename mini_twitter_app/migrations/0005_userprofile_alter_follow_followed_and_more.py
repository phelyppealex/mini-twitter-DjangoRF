# Generated by Django 5.1.2 on 2024-10-27 15:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_twitter_app', '0004_person_created'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='follow',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_set', to='mini_twitter_app.userprofile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_set', to='mini_twitter_app.userprofile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_twitter_app.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_twitter_app.userprofile'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
