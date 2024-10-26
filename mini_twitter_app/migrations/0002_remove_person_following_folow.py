# Generated by Django 5.1.2 on 2024-10-26 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_twitter_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='following',
        ),
        migrations.CreateModel(
            name='Folow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_set', to='mini_twitter_app.person')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_set', to='mini_twitter_app.person')),
            ],
        ),
    ]
