# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=100, serialize=False)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Post Categories',
                'verbose_name': 'Post Category',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='Post id', serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Post title')),
                ('snippet', models.CharField(max_length=255, verbose_name='Post snippet')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='Date published', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date modified')),
                ('publish', models.BooleanField(default=True)),
                ('body', models.TextField(verbose_name='Post body')),
                ('comments_enabled', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name_plural': 'Blog Posts',
                'verbose_name': 'Blog Post',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
