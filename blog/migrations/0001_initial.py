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
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Post Category',
                'verbose_name_plural': 'Post Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='Comment id', primary_key=True, serialize=False)),
                ('body', models.TextField(verbose_name='Comment body')),
                ('pub_date', models.DateTimeField(verbose_name='Date published', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Date modified', auto_now=True)),
            ],
            options={
                'verbose_name': 'Post comment',
                'verbose_name_plural': 'Post comments',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='Post id', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Post title', max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Date published', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Date modified', auto_now=True)),
                ('publish', models.BooleanField(default=True)),
                ('body', models.TextField(verbose_name='Post body')),
                ('comments_enabled', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('general_theme', models.CharField(choices=[('Lf', 'lf'), ('JS', 'JS'), ('Py', 'Py')], default='JS', max_length=2)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='blog.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_to_post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
